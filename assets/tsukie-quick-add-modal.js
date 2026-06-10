// Tsukie Custom Quick Add Modal
(function() {
  // Inject CSS Styles for the Modal
  const styles = `
    .tsukie-modal {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 10000;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease;
      font-family: 'Montserrat', sans-serif;
      box-sizing: border-box;
    }
    .tsukie-modal.is-open {
      opacity: 1;
      pointer-events: auto;
    }
    .tsukie-modal-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(30, 42, 56, 0.6);
      backdrop-filter: blur(4px);
    }
    .tsukie-modal-container {
      position: relative;
      background: #FDFBF7;
      width: 90%;
      max-width: 440px;
      padding: 30px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
      z-index: 1;
      transform: translateY(20px);
      transition: transform 0.3s ease;
      border: 1px solid #1E2A38;
      box-sizing: border-box;
    }
    .tsukie-modal.is-open .tsukie-modal-container {
      transform: translateY(0);
    }
    .tsukie-modal-close {
      position: absolute;
      top: 15px;
      right: 15px;
      background: none;
      border: none;
      cursor: pointer;
      padding: 5px;
      color: #1E2A38;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: opacity 0.2s ease;
    }
    .tsukie-modal-close:hover {
      opacity: 0.7;
    }
    .tsukie-modal-close svg {
      width: 16px;
      height: 16px;
    }
    
    /* Modal Header & Content */
    .tsukie-modal-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 14px;
      font-weight: 600;
      color: #1E2A38;
      margin: 0 0 8px 0;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      line-height: 1.4;
    }
    .tsukie-modal-price {
      font-family: 'Montserrat', sans-serif;
      font-size: 13px;
      color: #1E2A38;
      margin-bottom: 24px;
      font-weight: 500;
    }
    .tsukie-modal-price s {
      color: #8a8a8a;
      margin-left: 8px;
      font-size: 11px;
    }
    
    .tsukie-modal-option-wrapper {
      margin-bottom: 20px;
    }
    .tsukie-modal-option-label {
      display: block;
      font-family: 'Montserrat', sans-serif;
      font-size: 12px;
      font-weight: 600;
      color: #1E2A38;
      margin-bottom: 8px;
      text-transform: uppercase;
      letter-spacing: 0.02em;
    }
    .tsukie-modal-options-list {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }
    
    /* Size Pills */
    .tsukie-modal-pill {
      font-family: 'Montserrat', sans-serif;
      font-size: 12px;
      color: #1E2A38;
      background: transparent;
      border: 1px solid #1E2A38;
      padding: 8px 16px;
      cursor: pointer;
      transition: all 0.2s ease;
      outline: none;
      border-radius: 0;
      line-height: 1.2;
    }
    .tsukie-modal-pill.is-active {
      border-width: 2px;
      font-weight: 600;
    }
    .tsukie-modal-pill:disabled {
      opacity: 0.3;
      cursor: not-allowed;
      text-decoration: line-through;
    }
    
    /* Colour Swatches */
    .tsukie-modal-swatch {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      border: 1px solid #1E2A38;
      cursor: pointer;
      position: relative;
      padding: 0;
      outline: none;
      transition: all 0.2s ease;
      box-shadow: inset 0 0 0 2px #fff;
    }
    .tsukie-modal-swatch.is-active {
      border: 2px solid #A08766;
    }
    .tsukie-modal-swatch:disabled {
      opacity: 0.3;
      cursor: not-allowed;
    }
    .tsukie-modal-swatch:disabled::after {
      content: '';
      position: absolute;
      top: 50%;
      left: 50%;
      width: 100%;
      height: 1px;
      background: #1E2A38;
      transform: translate(-50%, -50%) rotate(45deg);
    }
    
    /* Submit Button */
    .tsukie-modal-submit-btn {
      font-family: 'Montserrat', sans-serif;
      font-size: 12px;
      font-weight: 600;
      color: #A08766;
      background: #1E2A38;
      border: none;
      width: 100%;
      padding: 15px;
      cursor: pointer;
      transition: all 0.2s ease;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      margin-top: 15px;
      border-radius: 0;
    }
    .tsukie-modal-submit-btn:hover:not(:disabled) {
      opacity: 0.95;
    }
    .tsukie-modal-submit-btn:disabled {
      background: #e0d9cd;
      color: #8a8a8a;
      cursor: not-allowed;
    }
    
    /* Mobile Drawer Layout */
    @media screen and (max-width: 749px) {
      .tsukie-modal {
        align-items: flex-end;
      }
      .tsukie-modal-container {
        width: 100%;
        max-width: 100%;
        height: auto;
        max-height: 80%;
        transform: translateY(100%);
        padding: 40px 20px 30px 20px;
        border: none;
        border-top: 1px solid #1E2A38;
        border-top-left-radius: 8px;
        border-top-right-radius: 8px;
      }
      .tsukie-modal.is-open .tsukie-modal-container {
        transform: translateY(0);
      }
      .tsukie-modal-close {
        top: 15px;
        right: 15px;
      }
    }
  `;

  const styleEl = document.createElement('style');
  styleEl.textContent = styles;
  document.head.appendChild(styleEl);

  const productCache = new Map();
  let activeProductData = null;
  let selectedOptions = []; // Array of selected option values

  // Helper mapping for swatches
  function getSwatchColor(colorName) {
    const bg_color = colorName.toLowerCase().replace(/ /g, '');
    switch(bg_color) {
      case 'navyblue':
      case 'navy':
        return '#001935';
      case 'offwhite':
        return '#faf6f0';
      case 'beige':
        return '#ebdcc7';
      case 'black':
        return '#111111';
      case 'white':
        return '#ffffff';
      case 'olive':
      case 'olivegreen':
        return '#556b2f';
      case 'rust':
        return '#b76e50';
      case 'dustypink':
      case 'rose':
        return '#dcaeaf';
      case 'mustard':
        return '#e1ad01';
      case 'lavender':
        return '#e6e6fa';
      case 'grey':
      case 'gray':
        return '#808080';
      case 'skyblue':
      case 'blue':
        return '#87ceeb';
      default:
        return bg_color;
    }
  }

  // Helper to get active cart sections to update
  function getCartSectionsToUpdate() {
    const cartItemsComponents = document.querySelectorAll('cart-items-component');
    const sections = [];
    cartItemsComponents.forEach((item) => {
      if (item.dataset.sectionId) {
        sections.push(item.dataset.sectionId);
      }
    });
    return sections;
  }

  // Helper to format money (simple fallback if theme helper not loaded)
  function formatMoney(cents) {
    if (window.Theme?.moneyFormat) {
      // simple format replacement
      return window.Theme.moneyFormat.replace('{{amount}}', (cents / 100).toFixed(2));
    }
    // standard fallback
    return '$' + (cents / 100).toFixed(2);
  }

  // Dispatch theme native update event to refresh and open the drawer
  function dispatchCartUpdate(cartJson) {
    document.dispatchEvent(
      new CustomEvent('cart:update', {
        bubbles: true,
        detail: {
          resource: cartJson,
          sourceId: 'tsukie-quick-add',
          data: {
            itemCount: cartJson.item_count,
            sections: cartJson.sections,
            source: 'product-form-component'
          }
        }
      })
    );
  }

  // Create the modal DOM element
  function getOrCreateModal() {
    let modal = document.getElementById('tsukie-quick-add-modal');
    if (modal) return modal;

    modal = document.createElement('div');
    modal.id = 'tsukie-quick-add-modal';
    modal.className = 'tsukie-modal';
    modal.setAttribute('aria-hidden', 'true');
    modal.innerHTML = `
      <div class="tsukie-modal-overlay"></div>
      <div class="tsukie-modal-container">
        <button type="button" class="tsukie-modal-close" aria-label="Close">
          <svg viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>
        <div class="tsukie-modal-content"></div>
      </div>
    `;

    document.body.appendChild(modal);

    modal.querySelector('.tsukie-modal-overlay').addEventListener('click', closeModal);
    modal.querySelector('.tsukie-modal-close').addEventListener('click', closeModal);

    return modal;
  }

  function openModal() {
    const modal = getOrCreateModal();
    modal.classList.add('is-open');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    const modal = document.getElementById('tsukie-quick-add-modal');
    if (modal) {
      modal.classList.remove('is-open');
      modal.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }
  }

  // Render modal content for a product
  function renderModalContent(product) {
    activeProductData = product;
    selectedOptions = Array(product.options.length).fill(null);

    const modal = getOrCreateModal();
    const contentContainer = modal.querySelector('.tsukie-modal-content');

    // Build options HTML
    let optionsHtml = '';
    product.options.forEach((option, optionIdx) => {
      const isColor = option.name.toLowerCase() === 'color' || option.name.toLowerCase() === 'colour';
      let valuesHtml = '';
      
      option.values.forEach(val => {
        if (isColor) {
          const swatchColor = getSwatchColor(val);
          valuesHtml += `<button type="button" class="tsukie-modal-swatch" data-option-index="${optionIdx}" data-value="${val.replace(/"/g, '&quot;')}" style="background-color: ${swatchColor};" title="${val}"></button>`;
        } else {
          valuesHtml += `<button type="button" class="tsukie-modal-pill" data-option-index="${optionIdx}" data-value="${val.replace(/"/g, '&quot;')}">${val}</button>`;
        }
      });

      optionsHtml += `
        <div class="tsukie-modal-option-wrapper" data-option-name="${option.name}">
          <span class="tsukie-modal-option-label">${option.name}</span>
          <div class="tsukie-modal-options-list">
            ${valuesHtml}
          </div>
        </div>
      `;
    });

    const initialPrice = formatMoney(product.price);
    const initialComparePrice = product.compare_at_price > product.price ? `<s>${formatMoney(product.compare_at_price)}</s>` : '';

    contentContainer.innerHTML = `
      <h3 class="tsukie-modal-title">${product.title}</h3>
      <div class="tsukie-modal-price" id="tsukie-modal-price-display">
        <span class="price-value">${initialPrice}</span>
        ${initialComparePrice}
      </div>
      <div class="tsukie-modal-options-container">
        ${optionsHtml}
      </div>
      <button type="button" class="tsukie-modal-submit-btn" id="tsukie-modal-submit" disabled>Select Options</button>
    `;

    // Bind option click handlers
    const buttons = contentContainer.querySelectorAll('.tsukie-modal-pill, .tsukie-modal-swatch');
    buttons.forEach(btn => {
      btn.addEventListener('click', function() {
        const optIdx = parseInt(this.getAttribute('data-option-index'), 10);
        const val = this.getAttribute('data-value');

        // Toggle selection or select
        selectedOptions[optIdx] = val;

        // Update active UI classes
        const siblings = this.parentNode.querySelectorAll('.tsukie-modal-pill, .tsukie-modal-swatch');
        siblings.forEach(s => s.classList.remove('is-active'));
        this.classList.add('is-active');

        // Re-evaluate state
        updateOptionAvailability();
        checkSelectedVariant();
      });
    });

    // Run initial check to disable/grey out options that are globally sold out
    updateOptionAvailability();

    openModal();
  }

  // Disable options that are unavailable under current selection
  function updateOptionAvailability() {
    if (!activeProductData) return;

    const modal = getOrCreateModal();
    const optionLists = modal.querySelectorAll('.tsukie-modal-options-list');

    optionLists.forEach(list => {
      const optIdx = parseInt(list.getAttribute('data-option-index'), 10);
      const buttons = list.querySelectorAll('.tsukie-modal-pill, .tsukie-modal-swatch');

      buttons.forEach(btn => {
        const val = btn.getAttribute('data-value');

        // Test if selecting 'val' for option 'optIdx' has any available variant in combination with other selections
        const isAvailable = activeProductData.variants.some(variant => {
          // Must match the value under test
          if (variant.options[optIdx] !== val) return false;

          // Must match all other already selected options
          for (let i = 0; i < selectedOptions.length; i++) {
            if (i !== optIdx && selectedOptions[i] !== null) {
              if (variant.options[i] !== selectedOptions[i]) return false;
            }
          }

          // And variant itself must be in stock / available
          return variant.available;
        });

        // Toggle disabled attribute
        btn.disabled = !isAvailable;
      });
    });
  }

  // Check if current options resolve to a valid variant and update submit button
  function checkSelectedVariant() {
    if (!activeProductData) return;

    const submitBtn = document.getElementById('tsukie-modal-submit');
    const priceDisplay = document.getElementById('tsukie-modal-price-display');
    if (!submitBtn || !priceDisplay) return;

    // Check if all options are selected
    const allSelected = selectedOptions.every(val => val !== null);
    if (!allSelected) {
      // Find which options are missing
      const missingOptions = [];
      activeProductData.options.forEach((opt, idx) => {
        if (selectedOptions[idx] === null) {
          missingOptions.push(opt.name);
        }
      });
      submitBtn.disabled = true;
      submitBtn.textContent = `Select ${missingOptions.join(' & ')}`;
      return;
    }

    // Find matching variant
    const matchedVariant = activeProductData.variants.find(variant => {
      return variant.options.every((optVal, idx) => optVal === selectedOptions[idx]);
    });

    if (!matchedVariant) {
      submitBtn.disabled = true;
      submitBtn.textContent = 'Unavailable';
      return;
    }

    // Update Price Display in modal
    const matchedPrice = formatMoney(matchedVariant.price);
    const matchedComparePrice = matchedVariant.compare_at_price > matchedVariant.price ? `<s>${formatMoney(matchedVariant.compare_at_price)}</s>` : '';
    priceDisplay.innerHTML = `<span class="price-value">${matchedPrice}</span> ${matchedComparePrice}`;

    if (!matchedVariant.available) {
      submitBtn.disabled = true;
      submitBtn.textContent = 'Sold Out';
    } else {
      submitBtn.disabled = false;
      submitBtn.textContent = 'Add to Cart';
      submitBtn.setAttribute('data-variant-id', matchedVariant.id);
    }
  }

  // Handle addition from modal
  async function submitModalAdd() {
    const submitBtn = document.getElementById('tsukie-modal-submit');
    if (!submitBtn || submitBtn.disabled) return;

    const variantId = submitBtn.getAttribute('data-variant-id');
    if (!variantId) return;

    submitBtn.disabled = true;
    submitBtn.textContent = 'Adding...';

    try {
      const sectionsToUpdate = getCartSectionsToUpdate();
      const bodyData = new URLSearchParams();
      bodyData.append('id', variantId);
      bodyData.append('quantity', '1');
      if (sectionsToUpdate.length > 0) {
        bodyData.append('sections', sectionsToUpdate.join(','));
      }

      const response = await fetch('/cart/add.js', {
        method: 'POST',
        body: bodyData,
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        }
      });

      const cartJson = await response.json();
      if (cartJson.status) {
        alert(cartJson.description || cartJson.message);
        submitBtn.disabled = false;
        submitBtn.textContent = 'Add to Cart';
      } else {
        closeModal();
        dispatchCartUpdate(cartJson);
      }
    } catch (err) {
      console.error(err);
      submitBtn.disabled = false;
      submitBtn.textContent = 'Add to Cart';
    }
  }

  // Direct AJAX addition for single-variant products
  async function addSingleVariantDirectly(variantId, form) {
    const submitBtn = form.querySelector('.tsukie-quick-add-btn');
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.textContent = 'ADDING...';
    }

    try {
      const sectionsToUpdate = getCartSectionsToUpdate();
      const bodyData = new URLSearchParams();
      bodyData.append('id', variantId);
      bodyData.append('quantity', '1');
      if (sectionsToUpdate.length > 0) {
        bodyData.append('sections', sectionsToUpdate.join(','));
      }

      const response = await fetch('/cart/add.js', {
        method: 'POST',
        body: bodyData,
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        }
      });

      const cartJson = await response.json();
      if (cartJson.status) {
        alert(cartJson.description || cartJson.message);
      } else {
        dispatchCartUpdate(cartJson);
      }
    } catch (err) {
      console.error(err);
    } finally {
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.textContent = 'QUICK ADD';
      }
    }
  }

  // Global submit interception
  document.addEventListener('submit', async function(e) {
    const form = e.target.closest('.tsukie-quick-add-form');
    if (!form) return;

    e.preventDefault();
    e.stopPropagation();

    const handle = form.getAttribute('data-product-handle');
    const variantsCount = parseInt(form.getAttribute('data-variants-count'), 10) || 1;
    const variantId = form.querySelector('input[name="id"]').value;

    if (variantsCount <= 1) {
      // Add directly
      await addSingleVariantDirectly(variantId, form);
    } else {
      // Show modal
      const submitBtn = form.querySelector('.tsukie-quick-add-btn');
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = 'LOADING...';
      }

      try {
        let product = productCache.get(handle);
        if (!product) {
          const res = await fetch(`/products/${handle}.js`);
          product = await res.json();
          productCache.set(handle, product);
        }

        renderModalContent(product);
      } catch (err) {
        console.error('Failed to load product data', err);
        // Fallback: if fetch fails, try to submit original form
        form.submit();
      } finally {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.textContent = 'QUICK ADD';
        }
      }
    }
  });

  // Modal submit action listener
  document.addEventListener('click', function(e) {
    if (e.target && e.target.id === 'tsukie-modal-submit') {
      submitModalAdd();
    }
  });
})();
