import json

path = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\templates\index.json'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
    
json_start = content.find('{')
comment = content[:json_start]
json_content = content[json_start:]
data = json.loads(json_content)

hero_code = """<style>
.tsukie-hero-slider {
  position: relative;
  width: 100vw;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  height: 600px;
  overflow: hidden;
  background-color: #f5f1ea;
}
.tsukie-hero-slides {
  width: 100%;
  height: 100%;
  position: relative;
}
.tsukie-hero-slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 1s ease-in-out;
  display: flex;
  align-items: center;
  justify-content: center;
  background-size: cover;
  background-position: center;
  z-index: 1;
}
.tsukie-hero-slide.is-active {
  opacity: 1;
  z-index: 2;
}
.tsukie-hero-slide::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0,0,0,0.25);
  z-index: 1;
}
.tsukie-hero-slide-content {
  position: relative;
  z-index: 2;
  text-align: center;
  color: #ffffff;
  max-width: 800px;
  padding: 0 20px;
  transform: translateY(20px);
  transition: transform 0.8s ease;
}
.tsukie-hero-slide.is-active .tsukie-hero-slide-content {
  transform: translateY(0);
}
.tsukie-hero-slide-eyebrow {
  font-family: 'Montserrat', sans-serif;
  font-size: 12px;
  letter-spacing: 4px;
  text-transform: uppercase;
  margin: 0 0 16px;
  font-weight: 600;
  color: #d4c5a9;
}
.tsukie-hero-slide-title {
  font-family: 'Playfair Display', serif;
  font-size: 56px;
  font-style: italic;
  font-weight: 600;
  line-height: 1.15;
  margin: 0 0 24px;
  color: #ffffff;
}
.tsukie-hero-slide-desc {
  font-family: 'Montserrat', sans-serif;
  font-size: 15px;
  line-height: 1.7;
  max-width: 600px;
  margin: 0 auto 36px;
  color: #e5e5e5;
}
.tsukie-hero-slide-cta {
  display: inline-block;
  background: #1e2a38;
  color: #d4c5a9;
  padding: 16px 40px;
  font-family: 'Montserrat', sans-serif;
  font-size: 12px;
  letter-spacing: 2px;
  text-transform: uppercase;
  text-decoration: none;
  font-weight: 600;
  border: none;
  transition: all 0.3s ease;
}
.tsukie-hero-slide-cta:hover {
  background: #2a3a4a;
  transform: translateY(-2px);
}
.tsukie-slider-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 48px;
  height: 48px;
  background: rgba(255,255,255,0.15);
  border: 1px solid rgba(255,255,255,0.25);
  backdrop-filter: blur(4px);
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 10;
  transition: all 0.3s ease;
  font-size: 20px;
}
.tsukie-slider-btn:hover {
  background: rgba(255,255,255,0.3);
  color: #d4c5a9;
}
.tsukie-slider-btn--prev { left: 30px; }
.tsukie-slider-btn--next { right: 30px; }
.tsukie-slider-dots {
  position: absolute;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 12px;
  z-index: 10;
}
.tsukie-slider-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: rgba(255,255,255,0.4);
  cursor: pointer;
  transition: all 0.3s ease;
}
.tsukie-slider-dot.is-active {
  background: #d4c5a9;
  transform: scale(1.2);
}
@media(max-width: 749px) {
  .tsukie-hero-slider { height: 450px; }
  .tsukie-hero-slide-title { font-size: 34px; margin: 0 0 16px; }
  .tsukie-hero-slide-desc { font-size: 13px; margin: 0 auto 24px; }
  .tsukie-hero-slide-eyebrow { font-size: 10px; margin: 0 0 12px; }
  .tsukie-hero-slide-cta { padding: 12px 30px; font-size: 11px; }
  .tsukie-slider-btn { width: 36px; height: 36px; font-size: 16px; }
  .tsukie-slider-btn--prev { left: 15px; }
  .tsukie-slider-btn--next { right: 15px; }
}
</style>

<div class="tsukie-hero-slider">
  <div class="tsukie-hero-slides">
    <div class="tsukie-hero-slide is-active" style="background-image: url('{{ 'hero_banner_1.png' | asset_url }}');">
      <div class="tsukie-hero-slide-content">
        <p class="tsukie-hero-slide-eyebrow">SUMMER 2026 COLLECTION</p>
        <h1 class="tsukie-hero-slide-title">Dressed for the woman you already are</h1>
        <p class="tsukie-hero-slide-desc">
          Premium silhouettes crafted for the modern Indian woman — luxurious fabrics, thoughtful fit, and enduring style. Starting at ₹1,499.
        </p>
        <a href="/collections/new-arrivals" class="tsukie-hero-slide-cta">SHOP NEW ARRIVALS</a>
      </div>
    </div>
    
    <div class="tsukie-hero-slide" style="background-image: url('{{ 'hero_banner_2.png' | asset_url }}');">
      <div class="tsukie-hero-slide-content">
        <p class="tsukie-hero-slide-eyebrow">CHIC & ELEGANT</p>
        <h2 class="tsukie-hero-slide-title" style="margin: 0 0 24px;">Style in Peplum & Flared Tops</h2>
        <p class="tsukie-hero-slide-desc">
          Discover curated sets and tops designed for comfort, grace, and premium everyday wear.
        </p>
        <a href="/collections/all" class="tsukie-hero-slide-cta">EXPLORE BEST SELLERS</a>
      </div>
    </div>
    
    <div class="tsukie-hero-slide" style="background-image: url('{{ 'hero_banner_3.png' | asset_url }}');">
      <div class="tsukie-hero-slide-content">
        <p class="tsukie-hero-slide-eyebrow">ESSENTIAL LUXURY</p>
        <h2 class="tsukie-hero-slide-title" style="margin: 0 0 24px;">Timeless Pieces For Your Wardrobe</h2>
        <p class="tsukie-hero-slide-desc">
          Crafted with love, highlighting the natural body shape in sizes from XS to 4XL.
        </p>
        <a href="/collections" class="tsukie-hero-slide-cta">VIEW ALL COLLECTIONS</a>
      </div>
    </div>
  </div>
  
  <button class="tsukie-slider-btn tsukie-slider-btn--prev" aria-label="Previous Slide">‹</button>
  <button class="tsukie-slider-btn tsukie-slider-btn--next" aria-label="Next Slide">›</button>
  
  <div class="tsukie-slider-dots">
    <span class="tsukie-slider-dot is-active" data-index="0"></span>
    <span class="tsukie-slider-dot" data-index="1"></span>
    <span class="tsukie-slider-dot" data-index="2"></span>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const slider = document.querySelector('.tsukie-hero-slider');
  if (!slider) return;
  
  const slides = slider.querySelectorAll('.tsukie-hero-slide');
  const dots = slider.querySelectorAll('.tsukie-slider-dot');
  const prevBtn = slider.querySelector('.tsukie-slider-btn--prev');
  const nextBtn = slider.querySelector('.tsukie-slider-btn--next');
  
  let currentIndex = 0;
  let slideInterval;
  
  function showSlide(index) {
    slides[currentIndex].classList.remove('is-active');
    dots[currentIndex].classList.remove('is-active');
    
    currentIndex = (index + slides.length) % slides.length;
    
    slides[currentIndex].classList.add('is-active');
    dots[currentIndex].classList.add('is-active');
  }
  
  function nextSlide() {
    showSlide(currentIndex + 1);
  }
  
  function prevSlide() {
    showSlide(currentIndex - 1);
  }
  
  function startAutoPlay() {
    stopAutoPlay();
    slideInterval = setInterval(nextSlide, 5000);
  }
  
  function stopAutoPlay() {
    if (slideInterval) clearInterval(slideInterval);
  }
  
  prevBtn.addEventListener('click', () => { prevSlide(); startAutoPlay(); });
  nextBtn.addEventListener('click', () => { nextSlide(); startAutoPlay(); });
  
  dots.forEach(dot => {
    dot.addEventListener('click', function() {
      const index = parseInt(this.getAttribute('data-index'), 10);
      showSlide(index);
      startAutoPlay();
    });
  });
  
  slider.addEventListener('mouseenter', stopAutoPlay);
  slider.addEventListener('mouseleave', startAutoPlay);
  
  startAutoPlay();
});
</script>"""

data['sections']['custom_liquid_39iRXh']['settings']['custom_liquid'] = hero_code

with open(path, 'w', encoding='utf-8') as f:
    f.write(comment + json.dumps(data, indent=2, ensure_ascii=False))
    
print("Successfully updated custom_liquid_39iRXh hero section.")
