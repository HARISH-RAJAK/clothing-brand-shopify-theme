import { Component } from '@theme/component';
import { ThemeEvents, VariantUpdateEvent, ZoomMediaSelectedEvent, SlideshowSelectEvent } from '@theme/events';

/**
 * A custom element that renders a media gallery.
 *
 * @typedef {object} Refs
 * @property {import('./zoom-dialog').ZoomDialog} [zoomDialogComponent] - The zoom dialog component.
 * @property {import('./slideshow').Slideshow} [slideshow] - The slideshow component.
 * @property {HTMLElement[]} [media] - The media elements.
 *
 * @extends Component<Refs>
 */
export class MediaGallery extends Component {
  connectedCallback() {
    super.connectedCallback();

    const { signal } = this.#controller;
    const target = this.closest('.shopify-section, dialog');

    target?.addEventListener(ThemeEvents.variantUpdate, this.#handleVariantUpdate, { signal });
    this.refs.zoomDialogComponent?.addEventListener(ThemeEvents.zoomMediaSelected, this.#handleZoomMediaSelected, {
      signal,
    });

    // Prevent image reload flickering on mobile carousel
    this.#preventImageReload();

    this.#setupThumbnailInteractions();
  }

  updatedCallback() {
    super.updatedCallback();
    this.#setupThumbnailInteractions();
  }

  /**
   * Prevents images from reloading when scrolling on mobile
   */
  #preventImageReload() {
    // Only run on mobile
    if (window.innerWidth >= 750) return;

    const slides = this.querySelectorAll('slideshow-slide');
    if (!slides || slides.length === 0) return;

    // Force all images to load eagerly and stay in cache
    slides.forEach((slide) => {
      const images = slide.querySelectorAll('img');
      images.forEach((img) => {
        // Set loading to eager to prevent browser from unloading
        img.setAttribute('loading', 'eager');

        // If image is already loaded, mark it to stay in cache
        if (img.complete && img.naturalHeight > 0) {
          img.setAttribute('decoding', 'sync');
        }

        // Prevent image from being unloaded during scroll
        img.style.contentVisibility = 'visible';
      });
    });

    // Ensure carousel stops at boundaries
    const slideshow = this.querySelector('slideshow-component');
    if (slideshow) {
      const slideshowSlides = slideshow.querySelector('slideshow-slides');
      if (slideshowSlides instanceof HTMLElement) {
        // Prevent overscroll bounce effect
        slideshowSlides.style.overscrollBehaviorX = 'contain';
      }
    }

    // Setup adaptive dot pagination
    this.#setupAdaptiveDotPagination();
  }

  #setupThumbnailInteractions() {
    const thumbnails = this.#getThumbnailItems();
    if (!thumbnails.length || !this.slideshow) return;

    if (!this.#thumbnailsBound) {
      this.slideshow.addEventListener(SlideshowSelectEvent.eventName, this.#handleSlideshowSelect, {
        signal: this.#controller.signal,
      });
      this.#thumbnailsBound = true;
    }

    const initialIndex = typeof this.slideshow.current === 'number' ? this.slideshow.current : 0;
    this.#updateThumbnailSelection(initialIndex);
  }

  /**
   * Sets up adaptive dot pagination that syncs with carousel scrolling
   */
  #setupAdaptiveDotPagination() {
    const slideshow = this.querySelector('slideshow-component');
    const slideshowSlides = slideshow?.querySelector('slideshow-slides');
    const dots = this.querySelectorAll('.media-gallery__mobile-controls .slideshow-controls__dot');

    if (!slideshowSlides || !dots || dots.length === 0) return;

    // Update dots based on scroll position
    const updateDots = () => {
      if (!(slideshowSlides instanceof HTMLElement)) return;

      const scrollLeft = slideshowSlides.scrollLeft;
      const slideWidth = slideshowSlides.clientWidth * 0.8 + 16; // 80% width + gap
      const currentIndex = Math.round(scrollLeft / slideWidth);

      dots.forEach((dot, index) => {
        if (dot instanceof HTMLElement) {
          dot.setAttribute('aria-selected', index === currentIndex ? 'true' : 'false');
        }
      });
    };

    // Listen to scroll events
    slideshowSlides.addEventListener('scroll', updateDots, { passive: true });

    // Initial update
    updateDots();

    // Make dots clickable to navigate
    dots.forEach((dot, index) => {
      dot.addEventListener('click', () => {
        if (slideshowSlides instanceof HTMLElement) {
          const slideWidth = slideshowSlides.clientWidth * 0.8 + 16;
          slideshowSlides.scrollTo({
            left: slideWidth * index,
            behavior: 'smooth'
          });
        }
      });
    });
  }

  /**
   * Handles thumbnail click/tap selection.
   * @param {number} index
   * @param {MouseEvent | PointerEvent} event
   */
  /**
   * @param {number} index
   * @param {MouseEvent | PointerEvent} event
   */
  handleThumbnailClick(index, event) {
    const parsedIndex = typeof index === 'number' ? index : Number(index);
    if (Number.isNaN(parsedIndex)) return;

    this.slideshow?.select(parsedIndex, event);
  }

  /**
   * Handles keyboard interaction for thumbnails.
   * @param {number} index
   * @param {KeyboardEvent} event
   */
  handleThumbnailKeyDown(index, event) {
    const { key } = event;
    if (key !== 'Enter' && key !== ' ' && key !== 'Spacebar') return;

    event.preventDefault();
    const parsedIndex = typeof index === 'number' ? index : Number(index);
    if (Number.isNaN(parsedIndex)) return;

    this.slideshow?.select(parsedIndex, event);
  }

  /** @param {SlideshowSelectEvent} event */
  #handleSlideshowSelect = (event) => {
    const index = event.detail?.index;
    if (typeof index !== 'number') return;

    this.#updateThumbnailSelection(index);
  };

  /**
   * @param {number} index
   */
  #updateThumbnailSelection(index) {
    const thumbnails = this.#getThumbnailItems();
    if (!thumbnails.length) return;

    thumbnails.forEach((thumbnail, position) => {
      const isActive = position === index;
      thumbnail.setAttribute('aria-pressed', String(isActive));
    });

    const activeThumbnail = thumbnails[index];
    const hasIndexChanged = this.#currentThumbnailIndex !== index;
    this.#currentThumbnailIndex = index;

    if (activeThumbnail && hasIndexChanged) {
      activeThumbnail.scrollIntoView({ block: 'nearest', inline: 'nearest' });
    }
  }

  /** @returns {HTMLElement[]} */
  #getThumbnailItems() {
    return /** @type {HTMLElement[]} */ (Array.from(this.querySelectorAll('[data-thumbnail-index]')));
  }

  #controller = new AbortController();
  #thumbnailsBound = false;
  /** @type {number | null} */
  #currentThumbnailIndex = null;

  disconnectedCallback() {
    super.disconnectedCallback();

    this.#controller.abort();
  }

  /**
   * Handles a variant update event by replacing the current media gallery with a new one.
   *
   * @param {VariantUpdateEvent} event - The variant update event.
   */
  #handleVariantUpdate = (event) => {
    const source = event.detail.data.html;

    if (!source) return;
    const newMediaGallery = source.querySelector('media-gallery');

    if (!newMediaGallery) return;

    this.replaceWith(newMediaGallery);
  };

  /**
   * Handles the 'zoom-media:selected' event.
   * @param {ZoomMediaSelectedEvent} event - The zoom-media:selected event.
   */
  #handleZoomMediaSelected = async (event) => {
    this.slideshow?.select(event.detail.index, undefined, { animate: false });
  };

  /**
   * Zooms the media gallery.
   *
   * @param {number} index - The index of the media to zoom.
   * @param {PointerEvent} event - The pointer event.
   */
  zoom(index, event) {
    this.refs.zoomDialogComponent?.open(index, event);
  }

  get slideshow() {
    return this.refs.slideshow;
  }

  get media() {
    return this.refs.media;
  }

  get presentation() {
    return this.dataset.presentation;
  }
}

if (!customElements.get('media-gallery')) {
  customElements.define('media-gallery', MediaGallery);
}
