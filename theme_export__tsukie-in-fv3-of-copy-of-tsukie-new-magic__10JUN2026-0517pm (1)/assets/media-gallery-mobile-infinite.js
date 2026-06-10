document.addEventListener('DOMContentLoaded', () => {
    const mediaGallery = document.querySelector('media-gallery.media-gallery--custom-layout');
    if (!mediaGallery) return;

    const slideshow = mediaGallery.querySelector('slideshow-component');
    if (!slideshow) return;

    const slidesContainer = slideshow.querySelector('slideshow-slides');
    if (!slidesContainer) return;
    if (!(slidesContainer instanceof HTMLElement)) return;

    const slides = Array.from(slidesContainer.children);
    if (slides.length <= 1) return;

    const firstSlide = slides[0];
    const lastSlide = slides[slides.length - 1];

    if (!(firstSlide instanceof HTMLElement) || !(lastSlide instanceof HTMLElement)) return;

    // Clone first and last slides
    const firstSlideClone = firstSlide.cloneNode(true);
    if (firstSlideClone instanceof HTMLElement) {
        firstSlideClone.setAttribute('aria-hidden', 'true');
        firstSlideClone.setAttribute('data-clone', 'true');
        firstSlideClone.removeAttribute('slide-id');
        firstSlideClone.removeAttribute('ref'); // Remove ref attribute so it's not tracked by slideshow component
        firstSlideClone.classList.add('clone', 'clone-first');
    }

    const lastSlideClone = lastSlide.cloneNode(true);
    if (lastSlideClone instanceof HTMLElement) {
        lastSlideClone.setAttribute('aria-hidden', 'true');
        lastSlideClone.setAttribute('data-clone', 'true');
        lastSlideClone.removeAttribute('slide-id');
        lastSlideClone.removeAttribute('ref'); // Remove ref attribute so it's not tracked by slideshow component
        lastSlideClone.classList.add('clone', 'clone-last');
    }

    // Add clones to the DOM
    slidesContainer.appendChild(firstSlideClone);
    slidesContainer.insertBefore(lastSlideClone, firstSlide);

    const gap = parseInt(window.getComputedStyle(slidesContainer).gap, 10) || 16;

    const selectFirstSlide = () => {
        // Ensure the slideshow starts on the first real slide regardless of control style
        try {
            // Only proceed if the custom element is upgraded and has a select method
            /** @type {any} */
            const slideshowEl = slideshow;
            if (typeof slideshowEl.select === 'function') {
                slideshowEl.select(0, undefined, { animate: false });
            } else {
                // Fallback: nudge initial-slide attribute to force internal re-sync
                const current = slideshow.getAttribute('initial-slide') ?? '0';
                slideshow.setAttribute('initial-slide', current);
            }
        } catch (_) {
            // no-op; defensive
        }
    };

    const setInitialPosition = () => {
        if (lastSlideClone instanceof HTMLElement) {
            slidesContainer.scrollLeft = lastSlideClone.offsetWidth + gap;
        }
        // After positioning, explicitly select the first slide to avoid off-by-one in some pagination styles
        // Delay a tick to let scroll positioning apply
        requestAnimationFrame(() => selectFirstSlide());
    };

    // Set initial position after a brief delay to ensure elements are rendered
    setTimeout(setInitialPosition, 100);

    // Recalculate on resize
    /** @type {number|undefined} */
    let resizeTimeout = undefined;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(() => {
            setInitialPosition();
            // Make sure first slide remains selected after resize reflow
            selectFirstSlide();
        }, 100);
    });

    let isScrolling = false;
    let isJumping = false;

    const handleScroll = () => {
        if (isScrolling || isJumping) return;
        isScrolling = true;

        requestAnimationFrame(() => {
            if (!(firstSlideClone instanceof HTMLElement) || !(lastSlideClone instanceof HTMLElement)) {
                isScrolling = false;
                return;
            }
            const scrollLeft = slidesContainer.scrollLeft;
            const totalWidth = slidesContainer.scrollWidth;
            const containerWidth = slidesContainer.clientWidth;

            // When scrolled to the last clone (which is a copy of the first slide)
            if (scrollLeft >= totalWidth - containerWidth - gap) {
                isJumping = true;
                slidesContainer.style.scrollBehavior = 'auto';
                slidesContainer.scrollLeft = lastSlideClone.offsetWidth + gap; // Jump to the first real slide
                setTimeout(() => {
                    slidesContainer.style.scrollBehavior = 'smooth';
                    isJumping = false;
                }, 50);
            }
            // When scrolled to the first clone (which is a copy of the last slide)
            else if (scrollLeft <= 0) {
                isJumping = true;
                slidesContainer.style.scrollBehavior = 'auto';
                slidesContainer.scrollLeft = totalWidth - (firstSlideClone.offsetWidth + gap) - containerWidth; // Jump to the last real slide
                setTimeout(() => {
                    slidesContainer.style.scrollBehavior = 'smooth';
                    isJumping = false;
                }, 50);
            }
            isScrolling = false;
        });
    };

    slidesContainer.addEventListener('scroll', handleScroll);

    // In case the slideshow upgrades after DOMContentLoaded, ensure the first slide is selected
    if (customElements && typeof customElements.whenDefined === 'function') {
        customElements.whenDefined('slideshow-component').then(() => {
            // Small timeout to allow the component's own setup to run first
            setTimeout(selectFirstSlide, 50);
        });
    } else {
        // Fallback if Custom Elements API is not available
        setTimeout(selectFirstSlide, 150);
    }
});
