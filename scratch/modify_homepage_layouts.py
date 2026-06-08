import json

path = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\templates\index.json'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
    
json_start = content.find('{')
comment = content[:json_start]
json_content = content[json_start:]
data = json.loads(json_content)

# ----------------- SECTION 1: custom_liquid_pLiMzL (Shop by Collection) -----------------
pLiMzL_code = """<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,400;1,600&family=Montserrat:wght@400;500&display=swap');

.tsukie-collection-head{
  background:#f5f1ea;
  padding:80px 0 0;
  text-align:center;
}
.tsukie-collection-inner{
  max-width:1400px;
  margin:0 auto;
  padding:0 40px;
}
.tsukie-collection-eyebrow{
  color:#a08766;
  font-size:10px;
  letter-spacing:2.5px;
  text-transform:uppercase;
  margin:0 0 8px;
  font-weight:500;
  font-family:'Montserrat',sans-serif;
}
.tsukie-collection-heading{
  font-family:'Playfair Display',serif;
  font-size:52px;
  font-style:italic;
  font-weight:600;
  line-height:1.15;
  margin:0 0 16px;
  padding-bottom:4px;
  color:#1e2a38;
  display:inline-block;
}
.tsukie-collection-subtext{
  font-size:14px;
  line-height:1.4;
  margin:0 auto;
  font-family:'Montserrat',sans-serif;
  color:#6b6b6b;
}

@media(max-width:749px){
  .tsukie-collection-head{padding:50px 0 0}
  .tsukie-collection-inner{padding:0 20px}
  .tsukie-collection-eyebrow{font-size:9px;margin:0 0 6px}
  .tsukie-collection-heading{font-size:36px;margin:0 0 12px;line-height:1.2;padding-bottom:3px}
  .tsukie-collection-subtext{font-size:13px}
}
</style>

<div class="tsukie-collection-head">
  <div class="tsukie-collection-inner">
    <p class="tsukie-collection-eyebrow">CURATED FOR YOU</p>
    <h2 class="tsukie-collection-heading">Shop by Collection</h2>
    <p class="tsukie-collection-subtext">
      Every collection tells a story — find yours.
    </p>
  </div>
</div>"""

# ----------------- SECTION 2: custom_liquid_nJYiF7 (New Arrivals Head) -----------------
nJYiF7_code = """<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,400;1,600&family=Montserrat:wght@400;500&display=swap');

.tsukie-newarrivals-head{
  background:#f5f1ea;
  padding:80px 0 0;
  text-align:center;
}
.tsukie-newarrivals-inner{
  max-width:1400px;
  margin:0 auto;
  padding:0 40px;
}
.tsukie-newarrivals-eyebrow{
  color:#a08766;
  font-size:10px;
  letter-spacing:2.5px;
  text-transform:uppercase;
  margin:0 0 12px;
  font-weight:500;
  font-family:'Montserrat',sans-serif;
}
.tsukie-newarrivals-heading{
  font-family:'Playfair Display',serif;
  font-size:52px;
  font-style:italic;
  font-weight:600;
  line-height:1.15;
  margin:0 0 16px;
  color:#1e2a38;
}
.tsukie-newarrivals-subtext{
  font-size:14px;
  line-height:1.5;
  margin:0 auto;
  max-width:520px;
  font-family:'Montserrat',sans-serif;
  color:#6b6b6b;
}

@media(max-width:749px){
  .tsukie-newarrivals-head{padding:50px 0 0}
  .tsukie-newarrivals-inner{padding:0 20px}
  .tsukie-newarrivals-eyebrow{font-size:9px;margin:0 0 10px}
  .tsukie-newarrivals-heading{font-size:36px;margin:0 0 12px;line-height:1.2}
  .tsukie-newarrivals-subtext{font-size:13px}
}
</style>

<div class="tsukie-newarrivals-head">
  <div class="tsukie-newarrivals-inner">
    <p class="tsukie-newarrivals-eyebrow">JUST DROPPED</p>
    <h2 class="tsukie-newarrivals-heading">New Arrivals</h2>
    <p class="tsukie-newarrivals-subtext">
      Fresh silhouettes every week — discover what's new this season before it sells out.
    </p>
  </div>
</div>"""

# ----------------- SECTION 3: custom_liquid_YqjbNx (New Arrivals Grid) -----------------
YqjbNx_code = """<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,400&family=Montserrat:wght@400;500;600&display=swap');

.tsukie-newarrivals-section{
  background:#f5f1ea;
  padding:24px 0 80px;
}
.tsukie-newarrivals-inner{
  max-width:1400px;
  margin:0 auto;
  padding:0 40px;
}
.tsukie-newarrivals-grid{
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:32px;
  margin-bottom:48px;
}
.tsukie-product-card{
  position:relative;
}
.tsukie-product-link{
  text-decoration:none;
  display:block;
}
.tsukie-product-media{
  position:relative;
  overflow:hidden;
  background:#fff;
  aspect-ratio:3/4;
}
.tsukie-product-img{
  width:100%;
  height:100%;
  object-fit:cover;
  transition:transform 0.5s ease;
  display:block;
}
.tsukie-product-card:hover .tsukie-product-img{
  transform:scale(1.05);
}
.tsukie-product-badge{
  position:absolute;
  top:12px;
  left:12px;
  background:#1e2a38;
  color:#d4c5a9;
  font-size:10px;
  letter-spacing:1.5px;
  text-transform:uppercase;
  padding:6px 12px;
  font-weight:600;
  z-index:2;
  border-radius:2px;
}
.tsukie-quick-add-btn{
  position:absolute;
  bottom:0;
  left:0;
  right:0;
  background:#1e2a38;
  color:#d4c5a9;
  text-align:center;
  padding:14px;
  font-size:11px;
  letter-spacing:2px;
  text-transform:uppercase;
  border:none;
  cursor:pointer;
  transform:translateY(100%);
  transition:transform 0.3s ease;
  width:100%;
}
.tsukie-product-card:hover .tsukie-quick-add-btn{
  transform:translateY(0);
}
.tsukie-product-info{
  margin-top:16px;
  display:flex;
  flex-direction:column;
  gap:10px;
}
.tsukie-product-title{
  font-family:'Playfair Display',serif;
  font-size:16px;
  color:#1a1a1a;
  margin:0;
  font-weight:400;
  line-height:1.3;
}
.tsukie-color-swatches{
  display:flex;
  gap:6px;
  margin:0;
  align-items:center;
}
.tsukie-color-swatch{
  width:18px;
  height:18px;
  border-radius:50%;
  border:1px solid #c9c9c9;
  cursor:default;
  flex-shrink:0;
  box-sizing:border-box;
}
.tsukie-color-swatch.is-active{
  border:2px solid #1e2a38;
}
.tsukie-product-price{
  font-size:15px;
  color:#1a1a1a;
  font-family:'Montserrat',sans-serif;
  margin:0;
}
.tsukie-product-price--compare{
  color:#999;
  text-decoration:line-through;
  margin-left:8px;
}
.tsukie-viewall-wrapper{
  text-align:center;
}
.tsukie-viewall-btn{
  display:inline-block;
  background:#1e2a38;
  color:#d4c5a9;
  padding:16px 48px;
  font-size:12px;
  letter-spacing:2.5px;
  text-transform:uppercase;
  text-decoration:none;
  font-weight:500;
  transition:all 0.3s ease;
  border:none;
}
.tsukie-viewall-btn:hover{
  background:#2a3a4a;
  transform:translateY(-2px);
}

@media(max-width:989px){
  .tsukie-newarrivals-grid{
    grid-template-columns:repeat(2,1fr);
    gap:24px;
  }
}
@media(max-width:749px){
  .tsukie-newarrivals-section{padding:16px 0 50px}
  .tsukie-newarrivals-inner{padding:0 16px}
  .tsukie-newarrivals-grid{
    display:grid;
    grid-template-columns:repeat(2,1fr);
    gap:16px;
    margin:0 0 32px;
    padding:0;
  }
  .tsukie-product-card{
    width:100%;
  }
  .tsukie-quick-add-btn{transform:translateY(0);padding:11px;font-size:10px}
  .tsukie-color-swatch{width:15px;height:15px}
  .tsukie-product-title{font-size:14px}
  .tsukie-product-info{margin-top:10px}
  .tsukie-product-price{font-size:14px}
  .tsukie-viewall-btn{padding:13px 32px;font-size:11px;width:100%;max-width:280px}
}
</style>

<div class="tsukie-newarrivals-section">
  <div class="tsukie-newarrivals-inner">
    <div class="tsukie-newarrivals-grid">
      {% for product in collections.new-arrivals.products limit: 5 %}
      <div class="tsukie-product-card">
        <div class="tsukie-product-media">
          <a href="{{ product.url }}" class="tsukie-product-link">
            <span class="tsukie-product-badge">Bestsellers</span>
            
            {% if product.featured_image %}
            <img 
              src="{{ product.featured_image | image_url: width: 600 }}" 
              alt="{{ product.title | escape }}"
              class="tsukie-product-img"
              loading="lazy"
            >
            {% else %}
            {{ 'product-1' | placeholder_svg_tag: 'tsukie-product-img' }}
            {% endif %}
          </a>
          
          {% form 'product', product %}
            <input type="hidden" name="id" value="{{ product.selected_or_first_available_variant.id }}">
            <button type="submit" class="tsukie-quick-add-btn" {% unless product.selected_or_first_available_variant.available %}disabled{% endunless %}>
              {% if product.selected_or_first_available_variant.available %}QUICK ADD{% else %}SOLD OUT{% endif %}
            </button>
          {% endform %}
        </div>
        
        <div class="tsukie-product-info">
          <a href="{{ product.url }}" class="tsukie-product-link">
            <h3 class="tsukie-product-title">{{ product.title }}</h3>
          </a>
          
          <div class="tsukie-product-price">
            {{ product.price | money }}
            {% if product.compare_at_price > product.price %}
            <span class="tsukie-product-price--compare">{{ product.compare_at_price | money }}</span>
            {% endif %}
          </div>
          
          {% assign color_option = product.options_with_values | where: 'name', 'Color' | first %}
          {% unless color_option %}
            {% assign color_option = product.options_with_values | where: 'name', 'Colour' | first %}
          {% endunless %}
          
          {% if color_option and color_option.values.size > 1 %}
          <div class="tsukie-color-swatches">
            {% for value in color_option.values limit: 4 %}
              <span 
                class="tsukie-color-swatch {% if forloop.first %}is-active{% endif %}" 
                style="background-color: {{ value | downcase }};"
                title="{{ value }}"
              ></span>
            {% endfor %}
          </div>
          {% endif %}
        </div>
      </div>
      {% endfor %}
    </div>
    
    <div class="tsukie-viewall-wrapper">
      <a href="{{ collections.new-arrivals.url }}" class="tsukie-viewall-btn">VIEW ALL</a>
    </div>
  </div>
</div>"""

# ----------------- SECTION 4: custom_liquid_nc9Wf6 (Shop by Category collections grid) -----------------
nc9Wf6_code = """<style>
.tsukie-collections-section {
  background: #f5f1ea;
  padding: 24px 0 80px;
}
.tsukie-collections-inner {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 40px;
}
.tsukie-collections-grid{
  display:flex;
  gap:24px;
  overflow-x:auto;
  scroll-snap-type:x mandatory;
  scrollbar-width:none;
  -webkit-overflow-scrolling:touch;
}
.tsukie-collections-grid::-webkit-scrollbar {
  display:none;
}
.tsukie-collection-card{
  position:relative;
  display:block;
  text-decoration:none;
  overflow:hidden;
  flex:0 0 calc(33.333% - 16px);
  scroll-snap-align:start;
}
.tsukie-collection-img{
  width:100%;
  aspect-ratio:3/4;
  object-fit:cover;
  display:block;
  transition:transform 0.5s ease;
}
.tsukie-collection-card:hover .tsukie-collection-img{
  transform:scale(1.04);
}
.tsukie-collection-overlay{
  position:absolute;
  bottom:0;
  left:0;
  right:0;
  background:linear-gradient(transparent, rgba(0,0,0,0.5));
  padding:60px 24px 24px;
}
.tsukie-collection-title{
  font-family:'Playfair Display',serif;
  font-size:24px;
  font-style:italic;
  margin:0;
  font-weight:400;
  color:#d4c5a9;
  text-shadow:0 2px 12px rgba(0,0,0,0.4);
}

@media(max-width:749px){
  .tsukie-collections-section{padding:16px 0 50px}
  .tsukie-collections-inner{padding:0}
  .tsukie-collections-grid{
    gap:16px;
    margin:0 -20px;
    padding:0 20px;
  }
  .tsukie-collection-card{
    flex:0 0 75%;
  }
  .tsukie-collection-title{
    font-size:22px;
  }
  .tsukie-collection-overlay{
    padding:50px 20px 20px;
  }
}
</style>

<div class="tsukie-collections-section">
  <div class="tsukie-collections-inner">
    <div class="tsukie-collections-grid">
      <!-- Collection 1 -->
      <a href="/collections/dresses" class="tsukie-collection-card">
        <img 
          src="{{ collections['dresses'].image | image_url: width: 800 }}" 
          alt="Dresses"
          class="tsukie-collection-img"
          loading="lazy"
        >
        <div class="tsukie-collection-overlay">
          <h3 class="tsukie-collection-title">Dresses</h3>
        </div>
      </a>
      
      <!-- Collection 2 -->
      <a href="/collections/coord-sets" class="tsukie-collection-card">
        <img 
          src="{{ collections['Skirts'].image | image_url: width: 800 }}" 
          alt="Skirts"
          class="tsukie-collection-img"
          loading="lazy"
        >
        <div class="tsukie-collection-overlay">
          <h3 class="tsukie-collection-title">Skirts</h3>
        </div>
      </a>
      
      <!-- Collection 3 -->
      <a href="/collections/tops" class="tsukie-collection-card">
        <img 
          src="{{ collections['tops'].image | image_url: width: 800 }}" 
          alt="Tops"
          class="tsukie-collection-img"
          loading="lazy"
        >
        <div class="tsukie-collection-overlay">
          <h3 class="tsukie-collection-title">Tops & Blouses</h3>
        </div>
      </a>
    </div>
  </div>
</div>"""

# ----------------- SECTION 5: custom_liquid_izaKX4 (Best Sellers Head) -----------------
izaKX4_code = """<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,400;1,600&family=Montserrat:wght@400;500&display=swap');

.tsukie-bestsellers-head{
  background:#f5f1ea;
  padding:80px 0 0;
  text-align:center;
}
.tsukie-bestsellers-inner{
  max-width:1400px;
  margin:0 auto;
  padding:0 40px;
}
.tsukie-bestsellers-header{
  text-align:center;
  margin-bottom:45px;
}
.tsukie-bestsellers-eyebrow{
  color:#a08766;
  font-size:11px;
  letter-spacing:3px;
  text-transform:uppercase;
  margin:0 0 16px;
  font-weight:500;
  font-family:'Montserrat',sans-serif;
}
.tsukie-bestsellers-heading{
  font-family:'Playfair Display',serif;
  font-size:52px;
  font-style:italic;
  font-weight:600;
  line-height:1.15;
  margin:0 0 20px;
  color:#1e2a38;
}
.tsukie-bestsellers-subtext{
  font-size:15px;
  line-height:1.6;
  color:#6b6b6b;
  margin:0 auto;
  max-width:580px;
  font-family:'Montserrat',sans-serif;
}

@media(max-width:749px){
  .tsukie-bestsellers-head{padding:50px 0 0}
  .tsukie-bestsellers-inner{padding:0 20px}
  .tsukie-bestsellers-heading{font-size:36px;margin:0 0 16px;line-height:1.2}
  .tsukie-bestsellers-header{margin-bottom:35px}
  .tsukie-bestsellers-eyebrow{margin:0 0 12px}
}
</style>

<div class="tsukie-bestsellers-head">
  <div class="tsukie-bestsellers-inner">
    <div class="tsukie-bestsellers-header">
      <p class="tsukie-bestsellers-eyebrow">CUSTOMER FAVOURITES</p>
      <h2 class="tsukie-bestsellers-heading">Best Sellers</h2>
      <p class="tsukie-bestsellers-subtext">
        The pieces our community keeps coming back for — tried, loved, and almost always sold out.
      </p>
    </div>
  </div>
</div>"""

# ----------------- SECTION 6: custom_liquid_ywjAVh (Best Sellers Grid) -----------------
ywjAVh_code = """<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,400&family=Montserrat:wght@400;500;600&display=swap');

.tsukie-bestsellers-grid-section{
  background:#f5f1ea;
  padding:24px 0 80px;
}
.tsukie-bestsellers-inner{
  max-width:1400px;
  margin:0 auto;
  padding:0 40px;
}
.tsukie-bestsellers-grid{
  display:grid;
  grid-template-columns:repeat(4,1fr);
  gap:32px;
  margin-bottom:48px;
}
.tsukie-product-card{
  position:relative;
}
.tsukie-product-link{
  text-decoration:none;
  display:block;
}
.tsukie-product-media{
  position:relative;
  overflow:hidden;
  background:#fff;
  aspect-ratio:3/4;
}
.tsukie-product-img{
  width:100%;
  height:100%;
  object-fit:cover;
  transition:transform 0.5s ease;
  display:block;
}
.tsukie-product-card:hover .tsukie-product-img{
  transform:scale(1.05);
}
.tsukie-product-badge{
  position:absolute;
  top:12px;
  left:12px;
  background:#1e2a38;
  color:#d4c5a9;
  font-size:10px;
  letter-spacing:1.5px;
  text-transform:uppercase;
  padding:6px 12px;
  font-weight:600;
  z-index:2;
  border-radius:2px;
}
.tsukie-quick-add-btn{
  position:absolute;
  bottom:0;
  left:0;
  right:0;
  background:#1e2a38;
  color:#d4c5a9;
  text-align:center;
  padding:14px;
  font-size:11px;
  letter-spacing:2px;
  text-transform:uppercase;
  border:none;
  cursor:pointer;
  transform:translateY(100%);
  transition:transform 0.3s ease;
  width:100%;
}
.tsukie-product-card:hover .tsukie-quick-add-btn{
  transform:translateY(0);
}
.tsukie-product-info{
  margin-top:16px;
  display:flex;
  flex-direction:column;
  gap:10px;
}
.tsukie-product-title{
  font-family:'Playfair Display',serif;
  font-size:16px;
  color:#1a1a1a;
  margin:0;
  font-weight:400;
  line-height:1.3;
}
.tsukie-color-swatches{
  display:flex;
  gap:6px;
  margin:0;
  align-items:center;
}
.tsukie-color-swatch{
  width:18px;
  height:18px;
  border-radius:50%;
  border:1px solid #c9c9c9;
  cursor:default;
  flex-shrink:0;
  box-sizing:border-box;
}
.tsukie-color-swatch.is-active{
  border:2px solid #1e2a38;
}
.tsukie-product-price{
  font-size:15px;
  color:#1a1a1a;
  font-family:'Montserrat',sans-serif;
  margin:0;
}
.tsukie-product-price--compare{
  color:#999;
  text-decoration:line-through;
  margin-left:8px;
}
.tsukie-viewall-wrapper{
  text-align:center;
}
.tsukie-viewall-btn{
  display:inline-block;
  background:#1e2a38;
  color:#d4c5a9;
  padding:16px 48px;
  font-size:12px;
  letter-spacing:2.5px;
  text-transform:uppercase;
  text-decoration:none;
  font-weight:500;
  transition:all 0.3s ease;
  border:none;
}
.tsukie-viewall-btn:hover{
  background:#2a3a4a;
  transform:translateY(-2px);
}

@media(max-width:989px){
  .tsukie-bestsellers-grid{grid-template-columns:repeat(2,1fr);gap:24px}
}
@media(max-width:749px){
  .tsukie-bestsellers-grid-section{padding:16px 0 50px}
  .tsukie-bestsellers-inner{padding:0 16px}
  .tsukie-bestsellers-grid{
    display:grid;
    grid-template-columns:repeat(2,1fr);
    gap:16px;
    margin:0 0 32px;
    padding:0;
  }
  .tsukie-product-card{
    width:100%;
  }
  .tsukie-quick-add-btn{transform:translateY(0);padding:11px;font-size:10px}
  .tsukie-color-swatch{width:15px;height:15px}
  .tsukie-product-title{font-size:14px}
  .tsukie-product-info{margin-top:10px}
  .tsukie-product-price{font-size:14px}
  .tsukie-viewall-btn{padding:13px 32px;font-size:11px;width:100%;max-width:280px}
}
</style>

<div class="tsukie-bestsellers-grid-section">
  <div class="tsukie-bestsellers-inner">
    <div class="tsukie-bestsellers-grid">
      {% for product in collections.all.products limit: 4 %}
      <div class="tsukie-product-card">
        <div class="tsukie-product-media">
          <a href="{{ product.url }}" class="tsukie-product-link">
            <span class="tsukie-product-badge">Bestsellers</span>
            
            {% if product.featured_image %}
            <img 
              src="{{ product.featured_image | image_url: width: 600 }}" 
              alt="{{ product.title | escape }}"
              class="tsukie-product-img"
              loading="lazy"
            >
            {% else %}
            {{ 'product-1' | placeholder_svg_tag: 'tsukie-product-img' }}
            {% endif %}
          </a>
          
          {% form 'product', product %}
            <input type="hidden" name="id" value="{{ product.selected_or_first_available_variant.id }}">
            <button type="submit" class="tsukie-quick-add-btn" {% unless product.selected_or_first_available_variant.available %}disabled{% endunless %}>
              {% if product.selected_or_first_available_variant.available %}QUICK ADD{% else %}SOLD OUT{% endif %}
            </button>
          {% endform %}
        </div>
        
        <div class="tsukie-product-info">
          <a href="{{ product.url }}" class="tsukie-product-link">
            <h3 class="tsukie-product-title">{{ product.title }}</h3>
          </a>
          
          <div class="tsukie-product-price">
            {{ product.price | money }}
            {% if product.compare_at_price > product.price %}
            <span class="tsukie-product-price--compare">{{ product.compare_at_price | money }}</span>
            {% endif %}
          </div>
          
          {% assign color_option = product.options_with_values | where: 'name', 'Color' | first %}
          {% unless color_option %}
            {% assign color_option = product.options_with_values | where: 'name', 'Colour' | first %}
          {% endunless %}
          
          {% if color_option and color_option.values.size > 1 %}
          <div class="tsukie-color-swatches">
            {% for value in color_option.values limit: 4 %}
              <span 
                class="tsukie-color-swatch {% if forloop.first %}is-active{% endif %}" 
                style="background-color: {{ value | downcase }};"
                title="{{ value }}"
              ></span>
            {% endfor %}
          </div>
          {% endif %}
        </div>
      </div>
      {% endfor %}
    </div>
    
    <div class="tsukie-viewall-wrapper">
      <a href="{{ collections.all.url }}" class="tsukie-viewall-btn">VIEW ALL</a>
    </div>
  </div>
</div>"""

# ----------------- SECTION 7: custom_liquid_8xRgKx (Best Sellers secondary) -----------------
sec_8xRgKx_code = """<style>
.tsukie-bestsellers{background:#f5f1ea;padding:80px 0}
.tsukie-bestsellers-inner{max-width:1400px;margin:0 auto;padding:0 40px}
.tsukie-bestsellers-header{text-align:center;margin-bottom:60px}
.tsukie-bestsellers-eyebrow{color:#a08766;font-size:11px;letter-spacing:3px;text-transform:uppercase;margin:0 0 24px;font-weight:500}
.tsukie-bestsellers-heading{
  font-family:'Playfair Display',serif;
  font-size:52px;
  font-style:italic;
  font-weight:600;
  line-height:1.15;
  margin:0 0 28px;
  color:#1e2a38;
}
.tsukie-bestsellers-subtext{font-size:15px;line-height:1.7;color:#6b6b6b;margin:0 auto;max-width:580px}
.tsukie-bestsellers-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:32px}
.tsukie-product-card{position:relative}
.tsukie-product-link{text-decoration:none;display:block}
.tsukie-product-media{position:relative;overflow:hidden;background:#fff;aspect-ratio:3/4}
.tsukie-product-img{width:100%;height:100%;object-fit:cover;transition:transform 0.5s ease;display:block}
.tsukie-product-card:hover .tsukie-product-img{transform:scale(1.05)}
.tsukie-product-badge{
  position:absolute;
  top:12px;
  left:12px;
  background:#1e2a38;
  color:#d4c5a9;
  font-size:10px;
  letter-spacing:1.5px;
  text-transform:uppercase;
  padding:6px 12px;
  font-weight:600;
  z-index:2;
  border-radius:2px;
}
.tsukie-quick-add-btn{position:absolute;bottom:0;left:0;right:0;background:#1e2a38;color:#d4c5a9;text-align:center;padding:14px;font-size:11px;letter-spacing:2px;text-transform:uppercase;border:none;cursor:pointer;transform:translateY(100%);transition:transform 0.3s ease;width:100%}
.tsukie-product-card:hover .tsukie-quick-add-btn{transform:translateY(0)}
.tsukie-product-info{
  margin-top:16px;
  display:flex;
  flex-direction:column;
  gap:10px;
}
.tsukie-product-title{
  font-family:'Playfair Display',serif;
  font-size:16px;
  color:#1a1a1a;
  margin:0;
  font-weight:400;
}
.tsukie-product-price{
  font-size:15px;
  color:#1a1a1a;
  margin:0;
}
.tsukie-product-price--compare{color:#999;text-decoration:line-through;margin-left:8px}
@media(max-width:989px){.tsukie-bestsellers-grid{grid-template-columns:repeat(2,1fr);gap:20px}}
@media(max-width:749px){
  .tsukie-bestsellers{padding:50px 0}
  .tsukie-bestsellers-inner{padding:0 16px}
  .tsukie-bestsellers-heading{font-size:36px}
  .tsukie-bestsellers-grid{
    grid-template-columns:repeat(2,1fr);
    gap:16px;
  }
  .tsukie-quick-add-btn{transform:translateY(0)}
}
</style>

<div class="tsukie-bestsellers">
  <div class="tsukie-bestsellers-inner">
    <div class="tsukie-bestsellers-header">
      <p class="tsukie-bestsellers-eyebrow">CUSTOMER FAVOURITES</p>
      <h2 class="tsukie-bestsellers-heading">Best Sellers</h2>
      <p class="tsukie-bestsellers-subtext">
        The pieces our community keeps coming back for — tried, loved, and almost always sold out.
      </p>
    </div>
    
    <div class="tsukie-bestsellers-grid">
      {% for product in collections.all.products limit: 4 %}
      <div class="tsukie-product-card">
        <div class="tsukie-product-media">
          <a href="{{ product.url }}" class="tsukie-product-link">
            <span class="tsukie-product-badge">Bestsellers</span>
            
            {% if product.featured_image %}
            <img 
              src="{{ product.featured_image | image_url: width: 600 }}" 
              alt="{{ product.title | escape }}"
              class="tsukie-product-img"
              loading="lazy"
            >
            {% else %}
            {{ 'product-1' | placeholder_svg_tag: 'tsukie-product-img' }}
            {% endif %}
          </a>
          
          {% form 'product', product %}
            <input type="hidden" name="id" value="{{ product.selected_or_first_available_variant.id }}">
            <button type="submit" class="tsukie-quick-add-btn" {% unless product.selected_or_first_available_variant.available %}disabled{% endunless %}>
              {% if product.selected_or_first_available_variant.available %}QUICK ADD{% else %}SOLD OUT{% endif %}
            </button>
          {% endform %}
        </div>
        
        <div class="tsukie-product-info">
          <a href="{{ product.url }}" class="tsukie-product-link">
            <h3 class="tsukie-product-title">{{ product.title }}</h3>
            <div class="tsukie-product-price">
              {{ product.price | money }}
              {% if product.compare_at_price > product.price %}
              <span class="tsukie-product-price--compare">{{ product.compare_at_price | money }}</span>
              {% endif %}
            </div>
          </a>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</div>"""

# ----------------- SECTION 8: custom_liquid_dQUmQ6 (Why Women Loves Us) -----------------
dQUmQ6_code = """<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,400&family=Montserrat:wght@400;500;600&display=swap');

.tsukie-promise{
  background:#1e2a38;
  padding:80px 0;
  text-align:center;
  color:#fff;
  width:100vw;
  position:relative;
  left:50%;
  right:50%;
  margin-left:-50vw;
  margin-right:-50vw;
}
.tsukie-promise-inner{
  max-width:1200px;
  margin:0 auto;
  padding:0 40px;
}
.tsukie-promise-eyebrow{
  color:#d4c5a9;
  font-size:10px;
  letter-spacing:2.5px;
  text-transform:uppercase;
  margin:0 0 12px;
  font-weight:500;
  font-family:'Montserrat',sans-serif;
}
.tsukie-promise-heading{
  font-family:'Playfair Display',serif;
  font-size:48px;
  line-height:1.05;
  font-weight:400;
  margin:0 0 14px;
  color:#fff;
}
.tsukie-promise-heading em{
  font-style:italic;
  color:#d4c5a9;
  font-weight:400;
}
.tsukie-promise-desc{
  color:#b8c2cc;
  font-size:14px;
  line-height:1.6;
  margin:0 auto 40px;
  max-width:550px;
  font-family:'Montserrat',sans-serif;
}
.tsukie-promise-grid{
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:24px;
}
.tsukie-promise-card{
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(212,197,169,0.15);
  border-radius:10px;
  padding:32px 24px;
  position:relative;
  text-align:center;
}
.tsukie-promise-number{
  position:absolute;
  top:16px;
  right:16px;
  font-size:36px;
  color:rgba(212,197,169,0.08);
  font-family:'Playfair Display',serif;
  font-weight:400;
  line-height:1;
}
.tsukie-promise-icon{
  width:40px;
  height:40px;
  margin:0 auto 20px;
  stroke:#d4c5a9;
  stroke-width:1.5;
  fill:none;
}
.tsukie-promise-title{
  font-family:'Playfair Display',serif;
  font-size:18px;
  color:#fff;
  margin:0 0 12px;
  font-weight:400;
  line-height:1.3;
}
.tsukie-promise-text{
  color:#b8c2cc;
  font-size:13px;
  line-height:1.6;
  margin:0;
  font-family:'Montserrat',sans-serif;
}

@media(max-width:989px){
  .tsukie-promise-grid{gap:20px}
  .tsukie-promise-card{padding:28px 20px}
}

@media(max-width:749px){
  .tsukie-promise{padding:50px 0}
  .tsukie-promise-inner{padding:0 12px}
  .tsukie-promise-eyebrow{font-size:9px;margin:0 0 10px;letter-spacing:2px}
  .tsukie-promise-heading{font-size:28px;margin:0 0 10px}
  .tsukie-promise-desc{font-size:12px;margin-bottom:28px;line-height:1.5}
  .tsukie-promise-grid{
    grid-template-columns:repeat(3,1fr);
    gap:10px;
  }
  .tsukie-promise-card{
    padding:18px 10px;
    border-radius:8px;
  }
  .tsukie-promise-number{
    top:10px;
    right:10px;
    font-size:24px;
  }
  .tsukie-promise-icon{
    width:28px;
    height:28px;
    margin:0 auto 12px;
  }
  .tsukie-promise-title{
    font-size:13px;
    margin:0 0 8px;
    line-height:1.2;
  }
  .tsukie-promise-text{
    font-size:10px;
    line-height:1.4;
  }
}

@media(max-width:374px){
  .tsukie-promise-title{font-size:12px}
  .tsukie-promise-text{font-size:9px}
  .tsukie-promise-card{padding:16px 8px}
}
</style>

<div class="tsukie-promise">
  <div class="tsukie-promise-inner">
    <p class="tsukie-promise-eyebrow">THE TSUKIE PROMISE</p>
    
    <h2 class="tsukie-promise-heading">
      Why Women <em>Love</em> Us
    </h2>
    
    <p class="tsukie-promise-desc">
      Every piece is designed with a simple belief — that luxury should feel attainable, and comfort should never be compromised.
    </p>
    
    <div class="tsukie-promise-grid">
      <div class="tsukie-promise-card">
        <span class="tsukie-promise-number">01</span>
        <svg class="tsukie-promise-icon" viewBox="0 0 24 24">
          <path d="M9 12l2 2 4-4m5.618-4.016A11.955 0 0112 2.944a11.955 0 01-8.618 3.04A12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
        </svg>
        <h3 class="tsukie-promise-title">Premium Fabric</h3>
        <p class="tsukie-promise-text">
          Hand-selected fabrics for drape, breathability, and longevity.
        </p>
      </div>
      
      <div class="tsukie-promise-card">
        <span class="tsukie-promise-number">02</span>
        <svg class="tsukie-promise-icon" viewBox="0 0 24 24">
          <circle cx="12" cy="12" r="10"/>
          <path d="M12 6v6l4 2"/>
        </svg>
        <h3 class="tsukie-promise-title">Real Body Fit</h3>
        <p class="tsukie-promise-text">
          Flattering silhouettes across XS to 4XL for every woman.
        </p>
      </div>
      
      <div class="tsukie-promise-card">
        <span class="tsukie-promise-number">03</span>
        <svg class="tsukie-promise-icon" viewBox="0 0 24 24">
          <path d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/>
        </svg>
        <h3 class="tsukie-promise-title">Fair Prices</h3>
        <p class="tsukie-promise-text">
          Premium quality without the markup. Starts at ₹1,499.
        </p>
      </div>
    </div>
  </div>
</div>"""

# ----------------- SECTION 9: custom_liquid_GaLWNF (Testimonials) -----------------
GaLWNF_code = """<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,400&family=Cormorant+Garamond:ital@1&family=Montserrat:wght@400;500;600&display=swap');

.tsukie-testimonials{
  background:#f5f1ea;
  padding:80px 0;
}
.tsukie-testimonials-inner{
  max-width:1400px;
  margin:0 auto;
  padding:0 40px;
}
.tsukie-testimonials-header{
  display:flex;
  justify-content:space-between;
  align-items:flex-end;
  margin-bottom:50px;
}
.tsukie-testimonials-left{}
.tsukie-testimonials-eyebrow{
  color:#a08766;
  font-size:10px;
  letter-spacing:2.5px;
  text-transform:uppercase;
  margin:0 0 14px;
  font-weight:500;
  font-family:'Montserrat',sans-serif;
}
.tsukie-testimonials-heading{
  font-family:'Playfair Display',serif;
  font-size:52px;
  line-height:1.15;
  font-weight:600;
  font-style:italic;
  margin:0;
  color:#1e2a38;
  padding-bottom:3px;
}
.tsukie-testimonials-right{
  text-align:right;
}
.tsukie-rating-number{
  font-family:'Playfair Display',serif;
  font-size:52px;
  line-height:1;
  font-weight:400;
  color:#1e2a38;
  margin:0 0 6px;
}
.tsukie-stars{
  color:#a08766;
  font-size:13px;
  letter-spacing:3px;
  margin-bottom:6px;
}
.tsukie-rating-text{
  color:#6b6b6b;
  font-size:10px;
  letter-spacing:1.5px;
  text-transform:uppercase;
  margin:0;
  font-family:'Montserrat',sans-serif;
}
.tsukie-testimonials-grid{
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:20px;
}
.tsukie-testimonial-card{
  background:#ffffff;
  padding:36px 28px;
  border-radius:8px;
  position:relative;
  box-shadow:0 2px 12px rgba(160,135,102,0.08);
}
.tsukie-quote-stars{
  color:#c9a77c;
  font-size:11px;
  letter-spacing:2px;
  margin-bottom:20px;
}
.tsukie-quote-text{
  font-family:'Cormorant Garamond',serif;
  font-size:15px;
  line-height:1.65;
  color:#3a3a3a;
  margin:0 0 28px;
  font-style:italic;
  min-height:130px;
}
.tsukie-testimonial-footer{
  display:flex;
  align-items:center;
  justify-content:space-between;
  padding-top:20px;
  border-top:1px solid #f0ebe3;
  gap:8px;
}
.tsukie-customer-info{
  display:flex;
  align-items:center;
  gap:10px;
  flex:1;
  min-width:0;
}
.tsukie-avatar{
  width:40px;
  height:40px;
  border-radius:50%;
  background:linear-gradient(135deg, #a08766 0%, #c9a77c 100%);
  color:#fff;
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:13px;
  font-weight:600;
  letter-spacing:1px;
  flex-shrink:0;
  font-family:'Montserrat',sans-serif;
}
.tsukie-customer-details{
  min-width:0;
  flex:1;
}
.tsukie-customer-name{
  font-size:13px;
  font-weight:600;
  color:#1e2a38;
  margin:0 0 2px;
  font-family:'Montserrat',sans-serif;
  white-space:nowrap;
  overflow:hidden;
  text-overflow:ellipsis;
}
.tsukie-customer-meta{
  font-size:11px;
  color:#8a8a8a;
  margin:0;
  font-family:'Montserrat',sans-serif;
  white-space:nowrap;
  overflow:hidden;
  text-overflow:ellipsis;
}
.tsukie-verified{
  color:#a08766;
  font-size:9px;
  letter-spacing:1.5px;
  text-transform:uppercase;
  font-weight:600;
  display:flex;
  align-items:center;
  gap:3px;
  font-family:'Montserrat',sans-serif;
  flex-shrink:0;
}

@media(max-width:989px){
  .tsukie-testimonials-header{flex-direction:column;align-items:flex-start;gap:28px}
  .tsukie-testimonials-right{text-align:left}
  .tsukie-testimonials-grid{grid-template-columns:repeat(2,1fr)}
  .tsukie-quote-text{min-height:auto}
}

@media(max-width:749px){
  .tsukie-testimonials{padding:50px 0}
  .tsukie-testimonials-inner{padding:0 14px}
  .tsukie-testimonials-header{margin-bottom:18px;gap:14px}
  .tsukie-testimonials-heading{font-size:36px}
  .tsukie-rating-number{font-size:36px}
  .tsukie-testimonials-eyebrow{font-size:9px;margin:0 0 6px}
  .tsukie-rating-text{font-size:9px}
  .tsukie-stars{font-size:10px;margin-bottom:3px}
  
  .tsukie-testimonials-grid{
    display:flex;
    gap:10px;
    overflow-x:auto;
    scroll-snap-type:x mandatory;
    -webkit-overflow-scrolling:touch;
    scrollbar-width:none;
    margin:0 -14px;
    padding:0 14px 4px;
  }
  .tsukie-testimonials-grid::-webkit-scrollbar{display:none}
  
  .tsukie-testimonial-card{
    flex:0 0 47%;
    scroll-snap-align:start;
    padding:16px 12px;
  }
  .tsukie-quote-stars{font-size:8px;margin-bottom:8px}
  .tsukie-quote-text{
    font-size:11px;
    line-height:1.4;
    margin:0 0 12px;
    min-height:70px;
  }
  .tsukie-testimonial-footer{
    padding-top:10px;
    gap:6px;
  }
  .tsukie-customer-info{gap:8px}
  .tsukie-avatar{width:26px;height:26px;font-size:9px}
  .tsukie-customer-name{font-size:10px;margin:0 0 1px}
  .tsukie-customer-meta{font-size:8px}
  .tsukie-verified{font-size:6px;gap:2px}
  .tsukie-verified svg{width:8px;height:8px}
}

@media(max-width:374px){
  .tsukie-testimonial-card{flex:0 0 47%;padding:14px 10px}
  .tsukie-quote-text{font-size:10px;min-height:65px;line-height:1.35}
  .tsukie-customer-name{font-size:9px}
  .tsukie-customer-meta{font-size:7px}
}
</style>

<div class="tsukie-testimonials">
  <div class="tsukie-testimonials-inner">
    <div class="tsukie-testimonials-header">
      <div class="tsukie-testimonials-left">
        <p class="tsukie-testimonials-eyebrow">12,000+ HAPPY CUSTOMERS</p>
        <h2 class="tsukie-testimonials-heading">What They're Saying</h2>
      </div>
      
      <div class="tsukie-testimonials-right">
        <div class="tsukie-rating-number">4.8</div>
        <div class="tsukie-stars">★★★★★</div>
        <p class="tsukie-rating-text">BASED ON 2,400+ VERIFIED REVIEWS</p>
      </div>
    </div>
    
    <div class="tsukie-testimonials-grid">
      <div class="tsukie-testimonial-card">
        <div class="tsukie-quote-stars">★★★★★</div>
        <p class="tsukie-quote-text">
          "The Valentina dress is everything I wanted — it fits so perfectly and the fabric is softer than anything I've ever owned. I've already ordered two more colours."
        </p>
        <div class="tsukie-testimonial-footer">
          <div class="tsukie-customer-info">
            <div class="tsukie-avatar">PA</div>
            <div class="tsukie-customer-details">
              <p class="tsukie-customer-name">Priya Anand</p>
              <p class="tsukie-customer-meta">Mumbai · Verified Buyer</p>
            </div>
          </div>
          <span class="tsukie-verified">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 0 01-8.618 3.04A12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
            </svg>
            VERIFIED
          </span>
        </div>
      </div>
      
      <div class="tsukie-testimonial-card">
        <div class="tsukie-quote-stars">★★★★★</div>
        <p class="tsukie-quote-text">
          "Finally a brand that understands what women actually want — beautiful clothes that are comfortable AND stylish. The coord set I bought got so many compliments at work."
        </p>
        <div class="tsukie-testimonial-footer">
          <div class="tsukie-customer-info">
            <div class="tsukie-avatar">RK</div>
            <div class="tsukie-customer-details">
              <p class="tsukie-customer-name">Riya Kapoor</p>
              <p class="tsukie-customer-meta">Delhi · Verified Buyer</p>
            </div>
          </div>
          <span class="tsukie-verified">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 0 01-8.618 3.04A12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
            </svg>
            VERIFIED
          </span>
        </div>
      </div>
      
      <div class="tsukie-testimonial-card">
        <div class="tsukie-quote-stars">★★★★★</div>
        <p class="tsukie-quote-text">
          "I'm a size 2XL and honestly cried when I saw how well the dress fit. No compromise, no stretching — just a perfectly proportioned design. This is what inclusivity actually looks like."
        </p>
        <div class="tsukie-testimonial-footer">
          <div class="tsukie-customer-info">
            <div class="tsukie-avatar">NS</div>
            <div class="tsukie-customer-details">
              <p class="tsukie-customer-name">Neha Sharma</p>
              <p class="tsukie-customer-meta">Bangalore · Verified Buyer</p>
            </div>
          </div>
          <span class="tsukie-verified">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9 12l2 2 4-4m5.618-4.016A11.955 0 0112 2.944a11.955 0 01-8.618 3.04A12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
            </svg>
            VERIFIED
          </span>
        </div>
      </div>
    </div>
  </div>
</div>"""

# ----------------- SECTION 10: custom_liquid_MMecBe (Style in Motion) -----------------
MMecBe_code = """<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,400;1,600&family=Cormorant+Garamond:ital@1&family=Montserrat:wght@300;400;500;600&display=swap');

.tsukie-insta-section{
  background:#fdfbf7;
  padding:80px 0;
  text-align:center;
  width:100%;
}
.tsukie-insta-inner{
  width:100%;
  padding:0 20px;
}
.tsukie-insta-heading{
  font-family:'Playfair Display',serif;
  font-size:52px;
  font-style:italic;
  font-weight:600;
  margin:0 0 8px;
  color:#1e2a38;
  line-height:1.15;
  padding-bottom:3px;
}
.tsukie-insta-subheading{
  font-family:'Montserrat',sans-serif;
  font-size:13px;
  letter-spacing:2px;
  text-transform:uppercase;
  color:#1e2a38;
  margin:0 0 6px;
  font-weight:600;
}
.tsukie-insta-divider{
  display:flex;
  align-items:center;
  justify-content:center;
  gap:14px;
  max-width:280px;
  margin:0 auto 18px;
}
.tsukie-insta-line{
  flex:1;
  height:1px;
  background:linear-gradient(90deg, transparent, #a08766, transparent);
}
.tsukie-insta-desc{
  font-family:'Cormorant Garamond',serif;
  font-size:18px;
  font-style:italic;
  color:#5a5a5a;
  margin:0 0 20px;
  line-height:1.5;
}
#insta-feed-widget{
  width:100%;
}
.tsukie-insta-handle{
  display:inline-block;
  background:linear-gradient(135deg, #a08766 0%, #c9a77c 100%);
  color:#1e2a38;
  padding:12px 32px;
  border-radius:50px;
  text-decoration:none;
  font-family:'Montserrat',sans-serif;
  font-size:13px;
  letter-spacing:1.5px;
  font-weight:600;
  text-transform:uppercase;
  margin-top:24px;
  transition:transform 0.3s ease;
}
.tsukie-insta-handle:hover{
  transform:translateY(-2px);
}

@media(max-width:749px){
  .tsukie-insta-section{padding:50px 0}
  .tsukie-insta-inner{padding:0 15px}
  .tsukie-insta-heading{font-size:36px;margin:0 0 6px;line-height:1.2}
  .tsukie-insta-subheading{margin:0 0 5px}
  .tsukie-insta-divider{margin:0 auto 16px}
  .tsukie-insta-desc{font-size:16px;margin:0 0 18px}
  .tsukie-insta-handle{margin-top:20px}
}
</style>

<div class="tsukie-insta-section">
  <div class="tsukie-insta-inner">
    <p class="tsukie-insta-subheading">Follow Our Journey</p>
    <h2 class="tsukie-insta-heading">Style in Motion</h2>
    <div class="tsukie-insta-divider">
      <span class="tsukie-insta-line"></span>
      <span style="color:#a08766;font-size:18px">✦</span>
      <span class="tsukie-insta-line"></span>
    </div>
    <p class="tsukie-insta-desc">See how real women style Tsukie. Tag us to be featured.</p>
    
    <div id="insta-feed-widget">
      {{ shop.metafields.social.instagram_feed }}
    </div>
    
    <a href="https://instagram.com/yourhandle" target="_blank" class="tsukie-insta-handle">
      @tsukieofficial
    </a>
  </div>
</div>"""

# Assign to index.json data
data['sections']['custom_liquid_pLiMzL']['settings']['custom_liquid'] = pLiMzL_code
data['sections']['custom_liquid_nJYiF7']['settings']['custom_liquid'] = nJYiF7_code
data['sections']['custom_liquid_YqjbNx']['settings']['custom_liquid'] = YqjbNx_code
data['sections']['custom_liquid_nc9Wf6']['settings']['custom_liquid'] = nc9Wf6_code
data['sections']['custom_liquid_izaKX4']['settings']['custom_liquid'] = izaKX4_code
data['sections']['custom_liquid_ywjAVh']['settings']['custom_liquid'] = ywjAVh_code
data['sections']['custom_liquid_8xRgKx']['settings']['custom_liquid'] = sec_8xRgKx_code
data['sections']['custom_liquid_dQUmQ6']['settings']['custom_liquid'] = dQUmQ6_code
data['sections']['custom_liquid_GaLWNF']['settings']['custom_liquid'] = GaLWNF_code
data['sections']['custom_liquid_MMecBe']['settings']['custom_liquid'] = MMecBe_code

with open(path, 'w', encoding='utf-8') as f:
    f.write(comment + json.dumps(data, indent=2, ensure_ascii=False))
    
print("Successfully modified homepage layouts, style updates, card layouts and spacing!")
