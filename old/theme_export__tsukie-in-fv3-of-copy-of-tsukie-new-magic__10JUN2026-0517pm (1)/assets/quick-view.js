// import { Component } from '@theme/component';
// import { onAnimationEnd } from '@theme/utilities';

// /**
//  * A custom element that manages a quick view dialog for product cards.
//  *
//  * @typedef {object} Refs
//  * @property {HTMLDialogElement} dialog – The dialog element.
//  * @property {HTMLElement} dialogContent – The dialog content container.
//  *
//  * @extends Component<Refs>
//  */
// export class QuickViewComponent extends Component {
//   requiredRefs = ['dialog', 'dialogContent'];

//   connectedCallback() {
//     super.connectedCallback();
//   }

//   disconnectedCallback() {
//     super.disconnectedCallback();
//   }

//   /**
//    * Opens the quick view dialog and loads product information.
//    * @param {string} productUrl - The URL of the product to load.
//    */
//   async openQuickView(productUrl) {
//     const { dialog, dialogContent } = this.refs;

//     if (dialog.open) return;

//     // Show loading state
//     dialogContent.innerHTML = '<div class="quick-view__loading">Loading...</div>';

//     // Lock scroll
//     document.body.style.width = '100%';
//     const scrollY = window.scrollY;
//     document.body.style.position = 'fixed';
//     document.body.style.top = `-${scrollY}px`;

//     dialog.showModal();

//     // Add event listeners
//     setTimeout(() => {
//       this.addEventListener('click', this.#handleClick);
//       this.addEventListener('keydown', this.#handleKeyDown);
//     });

//     try {
//       // Fetch the full product page
//       const response = await fetch(productUrl);
//       const html = await response.text();
      
//       const parser = new DOMParser();
//       const doc = parser.parseFromString(html, 'text/html');
      
//       // Extract the entire product-information section including all child elements
//       const productInfo = doc.querySelector('.product-information');
      
//       if (productInfo) {
//         // Clone the entire section with all its content
//         const clonedContent = /** @type {HTMLElement} */ (productInfo.cloneNode(true));

//         // Clear and insert the content
//         dialogContent.innerHTML = '';
//         dialogContent.appendChild(clonedContent);

//         // Re-run any scripts that might be needed for interactive elements
//         const scripts = clonedContent.querySelectorAll('script');
//         scripts.forEach((oldScript) => {
//           const newScript = document.createElement('script');
//           Array.from(oldScript.attributes).forEach(attr => {
//             newScript.setAttribute(attr.name, attr.value);
//           });
//           newScript.textContent = oldScript.textContent;
//           oldScript.parentNode?.replaceChild(newScript, oldScript);
//         });

//         // Initialize delivery date in quick view modal
//         this.#initDeliveryDate(dialogContent);

//         // Trigger any custom elements to initialize
//         if (typeof window !== 'undefined' && typeof window.Shopify !== 'undefined' && window.Shopify && /** @type {any} */ (window.Shopify).PaymentButton) {
//           /** @type {any} */ (window.Shopify).PaymentButton.init();
//         }

//         // Dispatch a custom event for other scripts to reinitialize
//         if (typeof window !== 'undefined') {
//           window.dispatchEvent(new CustomEvent('quickview:loaded', {
//             detail: { container: dialogContent }
//           }));
//         }
//       } else {
//         dialogContent.innerHTML = '<div class="quick-view__error">Product information not available.</div>';
//       }
//     } catch (error) {
//       console.error('Failed to load product:', error);
//       dialogContent.innerHTML = '<div class="quick-view__error">Failed to load product information.</div>';
//     }
//   }

//   /**
//    * Closes the quick view dialog.
//    */
//   closeDialog = async () => {
//     const { dialog } = this.refs;

//     if (!dialog.open) return;

//     this.removeEventListener('click', this.#handleClick);
//     this.removeEventListener('keydown', this.#handleKeyDown);

//     dialog.classList.add('dialog-closing');

//     await onAnimationEnd(dialog, undefined, {
//       subtree: false,
//     });

//     // Unlock scroll
//     document.body.style.width = '';
//     const scrollY = document.body.style.top;
//     document.body.style.position = '';
//     document.body.style.top = '';
//   window.scrollTo({ top: parseInt(scrollY) * -1, behavior: 'auto' });

//     dialog.close();
//     dialog.classList.remove('dialog-closing');
//   };

//   /**
//    * Handle click events
//    * @param {MouseEvent} event - The click event
//    */
//   #handleClick = (event) => {
//     const { dialog } = this.refs;
//     const rect = dialog.getBoundingClientRect();
//     const isInDialog = (
//       rect.top <= event.clientY &&
//       event.clientY <= rect.top + rect.height &&
//       rect.left <= event.clientX &&
//       event.clientX <= rect.left + rect.width
//     );

//     if (!isInDialog) {
//       this.closeDialog();
//     }
//   };

//   /**
//    * Handle keydown events
//    * @param {KeyboardEvent} event - The keyboard event
//    */
//   #handleKeyDown = (event) => {
//     if (event.key === 'Escape') {
//       event.preventDefault();
//       this.closeDialog();
//     }
//   };

//   /**
//    * Initialize delivery date in quick view modal
//    * @param {HTMLElement} container - The container element
//    */
//   #initDeliveryDate = (container) => {
//     const deliveryDateEl = container.querySelector('#deliveryDate, .delivery-date-value');
//     if (!deliveryDateEl) return;

//     // Calculate delivery dates using native JavaScript (no datejs dependency)
//     const today = new Date();
    
//     /**
//      * @param {Date} date
//      * @param {number} days
//      * @returns {Date}
//      */
//     const addDays = (date, days) => {
//       const result = new Date(date);
//       result.setDate(result.getDate() + days);
//       return result;
//     };

//     /**
//      * @param {Date} date
//      * @returns {string}
//      */
//     const formatDate = (date) => {
//       const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
//       const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
//       return `${days[date.getDay()]}, ${date.getDate()} ${months[date.getMonth()]}`;
//     };

//     const minDeliveryDate = addDays(today, 4);
//     const maxDeliveryDate = addDays(today, 7);

//     const minDateStr = formatDate(minDeliveryDate);
//     const maxDateStr = formatDate(maxDeliveryDate);

//     deliveryDateEl.innerHTML = `${minDateStr} - ${maxDateStr}`;
//   };
// }

// customElements.define('quick-view-component', QuickViewComponent);



import { Component } from '@theme/component';
import { onAnimationEnd } from '@theme/utilities';

/**
 * A custom element that manages a quick view dialog for product cards.
 *
 * @typedef {object} Refs
 * @property {HTMLDialogElement} dialog – The dialog element.
 * @property {HTMLElement} dialogContent – The dialog content container.
 *
 * @extends Component<Refs>
 */
export class QuickViewComponent extends Component {
  requiredRefs = ['dialog', 'dialogContent'];
  
  /** @type {Function[]} */
  #cleanupFunctions = [];

  connectedCallback() {
    super.connectedCallback();
  }

  disconnectedCallback() {
    super.disconnectedCallback();
    // Clean up any event listeners
    this.#cleanupFunctions.forEach(cleanup => cleanup());
    this.#cleanupFunctions = [];
  }

  /**
   * Opens the quick view dialog and loads product information.
   * @param {string} productUrl - The URL of the product to load.
   */
  async openQuickView(productUrl) {
    const { dialog, dialogContent } = this.refs;

    if (dialog.open) return;

    // Show loading state
    dialogContent.innerHTML = '<div class="quick-view__loading">Loading...</div>';

    // Lock scroll
    this.#lockScroll();

    dialog.showModal();

    // Add event listeners
    setTimeout(() => {
      this.addEventListener('click', this.#handleClick);
      this.addEventListener('keydown', this.#handleKeyDown);
    });

    try {
      // Fetch the full product page
      const response = await fetch(productUrl);
      const html = await response.text();
      
      const parser = new DOMParser();
      const doc = parser.parseFromString(html, 'text/html');
      
      // Extract the entire product-information section including all child elements
      const productInfo = doc.querySelector('.product-information');
      
      if (productInfo) {
        // Clone the entire section with all its content
        const clonedContent = /** @type {HTMLElement} */ (productInfo.cloneNode(true));

        // Clear and insert the content
        dialogContent.innerHTML = '';
        dialogContent.appendChild(clonedContent);

        // Re-run any scripts that might be needed for interactive elements
        const scripts = clonedContent.querySelectorAll('script');
        scripts.forEach((oldScript) => {
          const newScript = document.createElement('script');
          Array.from(oldScript.attributes).forEach(attr => {
            newScript.setAttribute(attr.name, attr.value);
          });
          newScript.textContent = oldScript.textContent;
          oldScript.parentNode?.replaceChild(newScript, oldScript);
        });

        // Initialize delivery date in quick view modal
        this.#initDeliveryDate(dialogContent);

        // Setup accordion moving functionality
        this.#setupAccordionMoving(dialogContent);

        // Initialize any Shopify components
        this.#initShopifyComponents();

        // Dispatch a custom event for other scripts to reinitialize
        window.dispatchEvent(new CustomEvent('quickview:loaded', {
          detail: { container: dialogContent }
        }));
      } else {
        dialogContent.innerHTML = '<div class="quick-view__error">Product information not available.</div>';
      }
    } catch (error) {
      console.error('Failed to load product:', error);
      dialogContent.innerHTML = '<div class="quick-view__error">Failed to load product information.</div>';
    }
  }

  /**
   * Setup accordion moving functionality for responsive design
   * @param {HTMLElement} container - The container element
   */
  #setupAccordionMoving = (container) => {
    const productDetails = container.querySelector('.product-details');
    const mediaContainer = container.querySelector('.product-information__media');
    
    if (!productDetails || !mediaContainer) return;

    // Create container in media if not exists
    let accordionContainer = container.querySelector('#desktop-accordion-container');
    if (!accordionContainer) {
      accordionContainer = document.createElement('div');
      accordionContainer.id = 'desktop-accordion-container';
      accordionContainer.style.marginTop = '20px';
      accordionContainer.style.width = '100%';
      mediaContainer.appendChild(accordionContainer);
    }

    const accordions = Array.from(productDetails.querySelectorAll('.accordion'));
    const placeholders = [];

    /**
     * Move accordions based on screen size
     */
    const moveAccordions = () => {
      const isDesktop = window.innerWidth >= 750;
      
      accordions.forEach((accordion, index) => {
        if (isDesktop) {
          // Move to desktop container
          if (accordion.parentElement !== accordionContainer) {
            // Create placeholder if not exists
            if (!placeholders[index]) {
              const placeholder = document.createElement('div');
              placeholder.className = 'accordion-placeholder';
              placeholder.style.display = 'none';
              accordion.parentNode.insertBefore(placeholder, accordion);
              placeholders[index] = placeholder;
            }
            accordionContainer.appendChild(accordion);
          }
        } else {
          // Move back to original position
          if (accordion.parentElement === accordionContainer) {
            const placeholder = placeholders[index];
            if (placeholder && placeholder.parentNode) {
              placeholder.parentNode.insertBefore(accordion, placeholder);
            } else {
              // Fallback if placeholder is gone
              productDetails.appendChild(accordion);
            }
          }
        }
      });
    };

    // Initial move
    moveAccordions();

    // Listen for resize
    const handleResize = () => moveAccordions();
    window.addEventListener('resize', handleResize);
    
    // Store cleanup function
    this.#cleanupFunctions.push(() => {
      window.removeEventListener('resize', handleResize);
    });
  };

  /**
   * Initialize Shopify components
   */
  #initShopifyComponents = () => {
    if (typeof window !== 'undefined' && typeof window.Shopify !== 'undefined' && window.Shopify && /** @type {any} */ (window.Shopify).PaymentButton) {
      /** @type {any} */ (window.Shopify).PaymentButton.init();
    }
  };

  /**
   * Lock body scroll when dialog is open
   */
  #lockScroll = () => {
    document.body.style.width = '100%';
    const scrollY = window.scrollY;
    document.body.style.position = 'fixed';
    document.body.style.top = `-${scrollY}px`;
  };

  /**
   * Closes the quick view dialog.
   */
  closeDialog = async () => {
    const { dialog } = this.refs;

    if (!dialog.open) return;

    this.removeEventListener('click', this.#handleClick);
    this.removeEventListener('keydown', this.#handleKeyDown);

    dialog.classList.add('dialog-closing');

    await onAnimationEnd(dialog, undefined, {
      subtree: false,
    });

    // Unlock scroll
    this.#unlockScroll();

    dialog.close();
    dialog.classList.remove('dialog-closing');
    
    // Run cleanup functions
    this.#cleanupFunctions.forEach(cleanup => cleanup());
    this.#cleanupFunctions = [];
  };

  /**
   * Unlock body scroll when dialog is closed
   */
  #unlockScroll = () => {
    document.body.style.width = '';
    const scrollY = document.body.style.top;
    document.body.style.position = '';
    document.body.style.top = '';
    window.scrollTo({ top: parseInt(scrollY || '0') * -1, behavior: 'auto' });
  };

  /**
   * Handle click events
   * @param {MouseEvent} event - The click event
   */
  #handleClick = (event) => {
    const { dialog } = this.refs;
    const rect = dialog.getBoundingClientRect();
    const isInDialog = (
      rect.top <= event.clientY &&
      event.clientY <= rect.top + rect.height &&
      rect.left <= event.clientX &&
      event.clientX <= rect.left + rect.width
    );

    if (!isInDialog) {
      this.closeDialog();
    }
  };

  /**
   * Handle keydown events
   * @param {KeyboardEvent} event - The keyboard event
   */
  #handleKeyDown = (event) => {
    if (event.key === 'Escape') {
      event.preventDefault();
      this.closeDialog();
    }
  };

  /**
   * Initialize delivery date in quick view modal
   * @param {HTMLElement} container - The container element
   */
  #initDeliveryDate = (container) => {
    const deliveryDateEl = container.querySelector('#deliveryDate, .delivery-date-value');
    if (!deliveryDateEl) return;

    // Calculate delivery dates using native JavaScript (no datejs dependency)
    const today = new Date();
    
    /**
     * @param {Date} date
     * @param {number} days
     * @returns {Date}
     */
    const addDays = (date, days) => {
      const result = new Date(date);
      result.setDate(result.getDate() + days);
      return result;
    };

    /**
     * @param {Date} date
     * @returns {string}
     */
    const formatDate = (date) => {
      const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
      const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
      return `${days[date.getDay()]}, ${date.getDate()} ${months[date.getMonth()]}`;
    };

    const minDeliveryDate = addDays(today, 4);
    const maxDeliveryDate = addDays(today, 7);

    const minDateStr = formatDate(minDeliveryDate);
    const maxDateStr = formatDate(maxDeliveryDate);

    deliveryDateEl.innerHTML = `${minDateStr} - ${maxDateStr}`;
  };
}

customElements.define('quick-view-component', QuickViewComponent);