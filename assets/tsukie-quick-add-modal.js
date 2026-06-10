// Tsukie Custom Quick Add Modal
(function() {
  // Inject CSS Styles for the Modal
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
      width: 95%;
      max-width: 1200px;
      height: auto;
      max-height: 90vh;
      padding: 40px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
      z-index: 1;
      transform: translateY(20px);
      transition: transform 0.3s ease;
      border: 1px solid #1E2A38;
      box-sizing: border-box;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
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
      z-index: 10;
    }
    .tsukie-modal-close:hover {
      opacity: 0.7;
    }
    .tsukie-modal-close svg {
      width: 18px;
      height: 18px;
    }
    .tsukie-modal-content {
      flex: 1;
      width: 100%;
    }
    
    /* Loading and Error States */
    .quick-view__loading,
    .quick-view__error {
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 400px;
      font-size: 16px;
      color: #1E2A38;
      font-family: 'Montserrat', sans-serif;
      text-transform: uppercase;
      letter-spacing: 2px;
      font-weight: 500;
    }
    .quick-view__loading::after {
      content: '';
      margin-left: 12px;
      width: 20px;
      height: 20px;
      border: 2px solid rgba(30, 42, 56, 0.1);
      border-top-color: #1E2A38;
      border-radius: 50%;
      animation: quick-view-spin 0.8s linear infinite;
    }
    @keyframes quick-view-spin {
      to { transform: rotate(360deg); }
    }
    
    /* Scoped PDP UI Adjustments inside Modal */
    .tsukie-modal-content .tsukie-product {
      background: transparent !important;
      padding: 0 !important;
    }
    .tsukie-modal-content .tsukie-product-container {
      padding: 0 !important;
      gap: 30px !important;
      max-width: 100% !important;
    }
    .tsukie-modal-content .tsukie-thumbnails {
      max-height: 400px !important;
    }
    .tsukie-modal-content .tsukie-thumbnails-wrapper {
      width: 70px !important;
    }
    .tsukie-modal-content .tsukie-thumb {
      width: 70px !important;
      height: 70px !important;
    }
    
    /* Mobile Drawer Layout */
    @media screen and (max-width: 989px) {
      .tsukie-modal-container {
        padding: 30px 20px;
      }
    }
    @media screen and (max-width: 749px) {
      .tsukie-modal {
        align-items: flex-end;
      }
      .tsukie-modal-container {
        width: 100%;
        max-width: 100%;
        height: 100%;
        max-height: 100%;
        transform: translateY(100%);
        padding: 50px 16px 20px 16px;
        border: none;
        border-top: 1px solid #1E2A38;
      }
      .tsukie-modal.is-open .tsukie-modal-container {
        transform: translateY(0);
      }
      .tsukie-modal-close {
        top: 15px;
        right: 15px;
        background: #ffffff;
        border-radius: 50%;
        width: 32px;
        height: 32px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15);
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

  // Render modal content for a product using fetched PDP HTML
  function renderModalContent(html) {
    const modal = getOrCreateModal();
    const contentContainer = modal.querySelector('.tsukie-modal-content');

    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');

    // Extract the PDP section wrapper
    const pdpWrapper = doc.querySelector('.tsukie-product')?.parentElement;

    if (pdpWrapper) {
      const clonedContent = pdpWrapper.cloneNode(true);

      // Clear previous content and append
      contentContainer.innerHTML = '';
      contentContainer.appendChild(clonedContent);

      // Lock scroll and open modal
      openModal();

      // Intercept the PDP form inside the modal to run AJAX cart add
      const modalForm = contentContainer.querySelector('.tsukie-product-form');
      if (modalForm) {
        modalForm.addEventListener('submit', function(e) {
          e.preventDefault();
          e.stopPropagation();
          submitModalForm(modalForm);
        });
      }

      // Re-run any scripts in the cloned content so variant picker and image gallery initialize
      const scripts = clonedContent.querySelectorAll('script');
      scripts.forEach((oldScript) => {
        const newScript = document.createElement('script');
        Array.from(oldScript.attributes).forEach(attr => {
          newScript.setAttribute(attr.name, attr.value);
        });
        newScript.textContent = oldScript.textContent;
        oldScript.parentNode?.replaceChild(newScript, oldScript);
      });

      // Dispatch load event
      window.dispatchEvent(new CustomEvent('quickview:loaded', {
        detail: { container: contentContainer }
      }));
    } else {
      contentContainer.innerHTML = '<div class="quick-view__error">Product details not available.</div>';
      openModal();
    }
  }

  // Intercept PDP form submit within the modal
  async function submitModalForm(form) {
    const submitBtn = form.querySelector('#tsukie-add-to-cart-btn');
    const submitTxt = form.querySelector('#tsukie-add-btn-text');
    const variantInput = form.querySelector('#tsukie-variant-id');
    const variantId = variantInput ? variantInput.value : null;

    if (!variantId) return;

    if (submitBtn) submitBtn.disabled = true;
    if (submitTxt) submitTxt.textContent = 'ADDING...';

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
        if (submitBtn) submitBtn.disabled = false;
        if (submitTxt) submitTxt.textContent = 'ADD TO BAG';
      } else {
        closeModal();
        dispatchCartUpdate(cartJson);
      }
    } catch (err) {
      console.error('Modal add to cart failed:', err);
      if (submitBtn) submitBtn.disabled = false;
      if (submitTxt) submitTxt.textContent = 'ADD TO BAG';
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

    const card = form.closest('.tsukie-product-card');
    const submitBtn = form.querySelector('.tsukie-quick-add-btn');
    const handle = (card && card.getAttribute('data-product-handle')) || 
                   (submitBtn && submitBtn.getAttribute('data-product-handle')) || 
                   form.getAttribute('data-product-handle');
    const variantsCount = parseInt(
      (card && card.getAttribute('data-variants-count')) || 
      (submitBtn && submitBtn.getAttribute('data-variants-count')) || 
      form.getAttribute('data-variants-count'), 10
    ) || 1;
    const variantId = form.querySelector('input[name="id"]').value;

    if (variantsCount <= 1) {
      // Add directly
      await addSingleVariantDirectly(variantId, form);
    } else {
      // Show loading in modal
      const submitBtn = form.querySelector('.tsukie-quick-add-btn');
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = 'LOADING...';
      }

      const modal = getOrCreateModal();
      const contentContainer = modal.querySelector('.tsukie-modal-content');
      contentContainer.innerHTML = '<div class="quick-view__loading">Loading...</div>';
      openModal();

      try {
        const res = await fetch(`/products/${handle}`);
        if (!res.ok) throw new Error('Failed to fetch product page');
        const html = await res.text();
        renderModalContent(html);
      } catch (err) {
        console.error('Failed to load product page', err);
        contentContainer.innerHTML = '<div class="quick-view__error">Failed to load product details.</div>';
      } finally {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.textContent = 'QUICK ADD';
        }
      }
    }
  });
})();
