import { Component } from '@theme/component';
import {
  fetchConfig,
  debounce,
  onAnimationEnd,
  prefersReducedMotion,
  resetShimmer,
  startViewTransition,
} from '@theme/utilities';
import { morphSection, sectionRenderer } from '@theme/section-renderer';
import {
  ThemeEvents,
  CartUpdateEvent,
  QuantitySelectorUpdateEvent,
  CartAddEvent,
  DiscountUpdateEvent,
} from '@theme/events';
import { cartPerformance } from '@theme/performance';

/** @typedef {import('./utilities').TextComponent} TextComponent */

/**
 * A custom element that displays a cart items component.
 *
 * @typedef {object} Refs
 * @property {HTMLElement[]} quantitySelectors - The quantity selector elements.
 * @property {HTMLTableRowElement[]} cartItemRows - The cart item rows.
 * @property {TextComponent} cartTotal - The cart total.
 *
 * @extends {Component<Refs>}
 */
class CartItemsComponent extends Component {
  #debouncedOnChange = debounce(this.#onQuantityChange, 300).bind(this);

  connectedCallback() {
    super.connectedCallback();

    document.addEventListener(ThemeEvents.cartUpdate, this.#handleCartUpdate);
    document.addEventListener(ThemeEvents.discountUpdate, this.handleDiscountUpdate);
    document.addEventListener(ThemeEvents.quantitySelectorUpdate, this.#debouncedOnChange);

    this.addEventListener('click', this.#onCartOptionClick);
    this.#initializeAllCartOptionAvailabilities();
  }

  disconnectedCallback() {
    super.disconnectedCallback();

    document.removeEventListener(ThemeEvents.cartUpdate, this.#handleCartUpdate);
    document.removeEventListener(ThemeEvents.discountUpdate, this.handleDiscountUpdate);
    document.removeEventListener(ThemeEvents.quantitySelectorUpdate, this.#debouncedOnChange);

    this.removeEventListener('click', this.#onCartOptionClick);
  }

  /**
   * Handles QuantitySelectorUpdateEvent change event.
   * @param {QuantitySelectorUpdateEvent} event - The event.
   */
  #onQuantityChange(event) {
    if (!(event.target instanceof Node) || !this.contains(event.target)) return;

    const { quantity, cartLine: line } = event.detail;

    // Cart items require a line number
    if (!line) return;

    if (quantity === 0) {
      return this.onLineItemRemove(line);
    }

    this.updateQuantity({
      line,
      quantity,
      action: 'change',
    });
    const lineItemRow = this.refs.cartItemRows[line - 1];

    if (!lineItemRow) return;

    const textComponent = /** @type {TextComponent | undefined} */ (lineItemRow.querySelector('text-component'));
    textComponent?.shimmer();
  }

  /**
   * Handles the line item removal.
   * @param {number} line - The line item index.
   */
  onLineItemRemove(line) {
    this.updateQuantity({
      line,
      quantity: 0,
      action: 'clear',
    });

    const cartItemRowToRemove = this.refs.cartItemRows[line - 1];

    if (!cartItemRowToRemove) return;

    const rowsToRemove = [
      cartItemRowToRemove,
      // Get all nested lines of the row to remove
      ...this.refs.cartItemRows.filter((row) => row.dataset.parentKey === cartItemRowToRemove.dataset.key),
    ];

    // If the cart item row is the last row, optimistically trigger the cart empty state
    const isEmptyCart = rowsToRemove.length == this.refs.cartItemRows.length;

    const template = document.getElementById('empty-cart-template');
    if (isEmptyCart && template instanceof HTMLTemplateElement) {
      const clone = document.importNode(template.content, true);

      startViewTransition(() => {
        this.replaceChildren(clone);
      }, [this.isDrawer ? 'empty-cart-drawer' : 'empty-cart-page']);

      return;
    }

    // Add class to the row to trigger the animation
    rowsToRemove.forEach((row) => {
      const remove = () => row.remove();

      if (prefersReducedMotion()) return remove();

      row.style.setProperty('--row-height', `${row.clientHeight}px`);
      row.classList.add('removing');

      // Remove the row after the animation ends
      onAnimationEnd(row, remove);
    });
  }

  /**
   * Updates the quantity.
   * @param {Object} config - The config.
   * @param {number} config.line - The line.
   * @param {number} config.quantity - The quantity.
   * @param {string} config.action - The action.
   */
  updateQuantity(config) {
    const cartPerformaceUpdateMarker = cartPerformance.createStartingMarker(`${config.action}:user-action`);

    this.#disableCartItems();

    const { line, quantity } = config;
    const { cartTotal } = this.refs;

    const cartItemsComponents = document.querySelectorAll('cart-items-component');
    const sectionsToUpdate = new Set([this.sectionId]);
    cartItemsComponents.forEach((item) => {
      if (item instanceof HTMLElement && item.dataset.sectionId) {
        sectionsToUpdate.add(item.dataset.sectionId);
      }
    });

    const body = JSON.stringify({
      line: line,
      quantity: quantity,
      sections: Array.from(sectionsToUpdate).join(','),
      sections_url: window.location.pathname,
    });

    cartTotal?.shimmer();

    fetch(`${Theme.routes.cart_change_url}`, fetchConfig('json', { body }))
      .then((response) => {
        return response.text();
      })
      .then((responseText) => {
        const parsedResponseText = JSON.parse(responseText);

        resetShimmer(this);

        if (parsedResponseText.errors) {
          this.#handleCartError(line, parsedResponseText);
          return;
        }

        const newSectionHTML = new DOMParser().parseFromString(
          parsedResponseText.sections[this.sectionId],
          'text/html'
        );

        // Grab the new cart item count from a hidden element
        const newCartHiddenItemCount = newSectionHTML.querySelector('[ref="cartItemCount"]')?.textContent;
        const newCartItemCount = newCartHiddenItemCount ? parseInt(newCartHiddenItemCount, 10) : 0;

        // Update data-cart-quantity for all matching variants
        this.#updateQuantitySelectors(parsedResponseText);

        this.dispatchEvent(
          new CartUpdateEvent(parsedResponseText, this.sectionId, {
            itemCount: newCartItemCount,
            source: 'cart-items-component',
            sections: parsedResponseText.sections,
          })
        );

        morphSection(this.sectionId, parsedResponseText.sections[this.sectionId], { mode: this.isDrawer ? 'hydration' : 'full' });

        this.#updateCartQuantitySelectorButtonStates();
      })
      .catch((error) => {
        console.error(error);
      })
      .finally(() => {
        this.#enableCartItems();
        cartPerformance.measureFromMarker(cartPerformaceUpdateMarker);
      });
  }

  /**
   * Updates the variant at a specific line item.
   * @param {number} line - The line item number (1-indexed).
   * @param {number} variantId - The new variant ID to set.
   * @param {string|null} [sellingPlan] - The selling plan ID if subscription.
   * @param {Function} [revertCallback] - Callback to revert UI on error.
   */
  updateVariant(line, variantId, sellingPlan = null, revertCallback = null) {
    this.#disableCartItems();

    const row = this.refs.cartItemRows[line - 1];
    const selectorsContainer = row?.querySelector('.cart-item-selectors');
    if (selectorsContainer) {
      selectorsContainer.classList.add('is-loading');
    }

    const { cartTotal } = this.refs;
    const cartItemsComponents = document.querySelectorAll('cart-items-component');
    const sectionsToUpdate = new Set([this.sectionId]);
    cartItemsComponents.forEach((item) => {
      if (item instanceof HTMLElement && item.dataset.sectionId) {
        sectionsToUpdate.add(item.dataset.sectionId);
      }
    });

    // We get the current quantity of that line item
    const qtyInput = row?.querySelector('quantity-selector-component input');
    const quantity = qtyInput ? parseInt(qtyInput.value, 10) : 1;

    const bodyObj = {
      line: line,
      id: variantId,
      quantity: quantity,
      sections: Array.from(sectionsToUpdate).join(','),
      sections_url: window.location.pathname,
    };

    if (sellingPlan) {
      bodyObj.selling_plan = parseInt(sellingPlan, 10);
    }

    const body = JSON.stringify(bodyObj);

    cartTotal?.shimmer();

    fetch(`${Theme.routes.cart_change_url}`, fetchConfig('json', { body }))
      .then((response) => response.text())
      .then((responseText) => {
        const parsedResponseText = JSON.parse(responseText);
        resetShimmer(this);

        if (parsedResponseText.errors) {
          this.#handleCartError(line, parsedResponseText);
          if (typeof revertCallback === 'function') revertCallback();
          return;
        }

        const newSectionHTML = new DOMParser().parseFromString(
          parsedResponseText.sections[this.sectionId],
          'text/html'
        );

        const newCartHiddenItemCount = newSectionHTML.querySelector('[ref="cartItemCount"]')?.textContent;
        const newCartItemCount = newCartHiddenItemCount ? parseInt(newCartHiddenItemCount, 10) : 0;

        this.#updateQuantitySelectors(parsedResponseText);

        this.dispatchEvent(
          new CartUpdateEvent(parsedResponseText, this.sectionId, {
            itemCount: newCartItemCount,
            source: 'cart-items-component',
            sections: parsedResponseText.sections,
          })
        );

        morphSection(this.sectionId, parsedResponseText.sections[this.sectionId], { mode: this.isDrawer ? 'hydration' : 'full' });
        this.#updateCartQuantitySelectorButtonStates();
      })
      .catch((error) => {
        console.error(error);
        if (typeof revertCallback === 'function') revertCallback();
      })
      .finally(() => {
        this.#enableCartItems();
        if (selectorsContainer) {
          selectorsContainer.classList.remove('is-loading');
        }
      });
  }

  /**
   * Handles the discount update.
   * @param {DiscountUpdateEvent} event - The event.
   */
  handleDiscountUpdate = (event) => {
    this.#handleCartUpdate(event);
  };

  /**
   * Handles the cart error.
   * @param {number} line - The line.
   * @param {Object} parsedResponseText - The parsed response text.
   * @param {string} parsedResponseText.errors - The errors.
   */
  #handleCartError = (line, parsedResponseText) => {
    const quantitySelector = this.refs.quantitySelectors[line - 1];
    const quantityInput = quantitySelector?.querySelector('input');

    if (!quantityInput) throw new Error('Quantity input not found');

    quantityInput.value = quantityInput.defaultValue;

    const cartItemError = this.refs[`cartItemError-${line}`];
    const cartItemErrorContainer = this.refs[`cartItemErrorContainer-${line}`];

    if (!(cartItemError instanceof HTMLElement)) throw new Error('Cart item error not found');
    if (!(cartItemErrorContainer instanceof HTMLElement)) throw new Error('Cart item error container not found');

    cartItemError.textContent = parsedResponseText.errors;
    cartItemErrorContainer.classList.remove('hidden');
  };

  /**
   * Handles the cart update.
   *
   * @param {DiscountUpdateEvent | CartUpdateEvent | CartAddEvent} event
   */
  #handleCartUpdate = (event) => {
    if (event instanceof DiscountUpdateEvent) {
      sectionRenderer.renderSection(this.sectionId, { cache: false }).then(() => {
        this.#initializeAllCartOptionAvailabilities();
      });
      return;
    }
    if (event.target === this) {
      this.#initializeAllCartOptionAvailabilities();
      return;
    }

    const cartItemsHtml = event.detail.data.sections?.[this.sectionId];
    if (cartItemsHtml) {
      morphSection(this.sectionId, cartItemsHtml);

      // Update button states for all cart quantity selectors after morph
      this.#updateCartQuantitySelectorButtonStates();
      this.#initializeAllCartOptionAvailabilities();
    } else {
      sectionRenderer.renderSection(this.sectionId, { cache: false }).then(() => {
        this.#initializeAllCartOptionAvailabilities();
      });
    }
  };

  /**
   * Disables the cart items.
   */
  #disableCartItems() {
    this.classList.add('cart-items-disabled');
  }

  /**
   * Enables the cart items.
   */
  #enableCartItems() {
    this.classList.remove('cart-items-disabled');
  }

  /**
   * Updates quantity selectors for all matching variants in the cart.
   * @param {Object} updatedCart - The updated cart object.
   * @param {Array<{variant_id: number, quantity: number}>} [updatedCart.items] - The cart items.
   */
  #updateQuantitySelectors(updatedCart) {
    if (!updatedCart.items) return;

    for (const item of updatedCart.items) {
      const variantId = item.variant_id.toString();
      const selectors = document.querySelectorAll(`quantity-selector-component[data-variant-id="${variantId}"]`);

      for (const selector of selectors) {
        const input = selector.querySelector('input[data-cart-quantity]');
        if (!input) continue;

        input.setAttribute('data-cart-quantity', item.quantity.toString());

        // Update the quantity selector's internal state
        if ('updateCartQuantity' in selector && typeof selector.updateCartQuantity === 'function') {
          selector.updateCartQuantity();
        }
      }
    }
  }

  /**
   * Updates button states for all cart quantity selector components.
   */
  #updateCartQuantitySelectorButtonStates() {
    for (const selector of document.querySelectorAll('cart-quantity-selector-component')) {
      /** @type {any} */ (selector).updateButtonStates?.();
    }
  }

  /**
   * Gets the section id.
   * @returns {string} The section id.
   */
  get sectionId() {
    const { sectionId } = this.dataset;

    if (!sectionId) throw new Error('Section id missing');

    return sectionId;
  }

  /**
   * @returns {boolean} Whether the component is a drawer.
   */
  get isDrawer() {
    return this.dataset.drawer !== undefined;
  }
  #onCartOptionClick = (event) => {
    const button = event.target.closest('.cart-item-pill, .cart-item-swatch');
    if (!button || button.disabled) return;

    const container = button.closest('.cart-item-selectors');
    if (!container) return;

    const list = button.closest('.cart-item-options-list');
    const optionIndex = parseInt(list.getAttribute('data-option-index'), 10);
    const value = button.getAttribute('data-value');

    // Store previous selections in case we need to revert
    const activeButtons = container.querySelectorAll('.cart-item-pill.is-active, .cart-item-swatch.is-active');
    const previousSelections = Array.from(activeButtons).map(btn => ({
      btn,
      parentList: btn.closest('.cart-item-options-list')
    }));

    // Update active class on siblings
    const siblings = list.querySelectorAll('.cart-item-pill, .cart-item-swatch');
    siblings.forEach(s => s.classList.remove('is-active'));
    button.classList.add('is-active');

    // Re-evaluate other options
    this.#updateCartOptionAvailability(container);

    // Get currently selected options
    const selectedOptions = [];
    const optionLists = container.querySelectorAll('.cart-item-options-list');
    optionLists.forEach(optList => {
      const idx = parseInt(optList.getAttribute('data-option-index'), 10);
      const activeBtn = optList.querySelector('.cart-item-pill.is-active, .cart-item-swatch.is-active');
      selectedOptions[idx] = activeBtn ? activeBtn.getAttribute('data-value') : null;
    });

    const variantsJson = JSON.parse(container.querySelector('.cart-item-variants-json').textContent);
    const matchedVariant = variantsJson.find(v => {
      return (!v.option1 || v.option1 === selectedOptions[0]) &&
             (!v.option2 || v.option2 === selectedOptions[1]) &&
             (!v.option3 || v.option3 === selectedOptions[2]);
    });

    if (matchedVariant) {
      const currentVariantId = parseInt(container.getAttribute('data-current-variant'), 10);
      if (matchedVariant.id !== currentVariantId) {
        const line = parseInt(container.getAttribute('data-line'), 10);
        const sellingPlan = container.getAttribute('data-selling-plan');
        
        this.updateVariant(line, matchedVariant.id, sellingPlan, () => {
          // Revert callback: restore active state of previously selected buttons
          siblings.forEach(s => s.classList.remove('is-active'));
          previousSelections.forEach(sel => {
            sel.btn.classList.add('is-active');
          });
          this.#updateCartOptionAvailability(container);
        });
      }
    }
  };

  #updateCartOptionAvailability(container) {
    const variantsJson = JSON.parse(container.querySelector('.cart-item-variants-json').textContent);
    const optionLists = container.querySelectorAll('.cart-item-options-list');
    
    // Get currently selected options
    const selectedOptions = [];
    optionLists.forEach(optList => {
      const idx = parseInt(optList.getAttribute('data-option-index'), 10);
      const activeBtn = optList.querySelector('.cart-item-pill.is-active, .cart-item-swatch.is-active');
      selectedOptions[idx] = activeBtn ? activeBtn.getAttribute('data-value') : null;
    });

    optionLists.forEach(optList => {
      const optIdx = parseInt(optList.getAttribute('data-option-index'), 10);
      const buttons = optList.querySelectorAll('.cart-item-pill, .cart-item-swatch');

      buttons.forEach(btn => {
        const val = btn.getAttribute('data-value');

        const isAvailable = variantsJson.some(variant => {
          if (variant.options[optIdx] !== val) return false;

          for (let i = 0; i < selectedOptions.length; i++) {
            if (i !== optIdx && selectedOptions[i] !== null) {
              if (variant.options[i] !== selectedOptions[i]) return false;
            }
          }
          return variant.available;
        });

        btn.disabled = !isAvailable;
      });
    });
  }

  #initializeAllCartOptionAvailabilities() {
    const containers = this.querySelectorAll('.cart-item-selectors');
    containers.forEach(container => {
      this.#updateCartOptionAvailability(container);
    });
  }
}

if (!customElements.get('cart-items-component')) {
  customElements.define('cart-items-component', CartItemsComponent);
}

// Global handler placeholder (kept for compatibility)
window.tsukieCartOptionChange = function(selectEl) {};
