import os

filepath = "C:/Users/hp/.gemini/antigravity-ide/brain/8f068730-3b21-43a7-96ee-55f10e6b4b4b/scratch/custom_liquid_rW9bhR.liquid"

if not os.path.exists(filepath):
    print("File not found")
else:
    content = open(filepath, 'r', encoding='utf-8').read()
    print("Length:", len(content))
    print("Has {% form 'product' %}:", "{% form 'product'" in content)
    print("Has tsukie-btn-buy:", "tsukie-btn-buy" in content)
    print("Has tsukieBuyNowClean:", "tsukieBuyNowClean" in content)
    print("Has tsukie-special-offers-strip:", "tsukie-special-offers-strip" in content)
    print("Has tsukie-size-guide-modal:", "tsukie-size-guide-modal" in content)
    print("Has tsukie-premium-badges (SVG):", "tsukie-premium-badges" in content)
    print("Has tsukie-order-status-v2:", "tsukie-order-status-v2" in content)
    print("Has tsukieFilterImagesByColor:", "tsukieFilterImagesByColor" in content)
    print("Has Cormorant Garamond:", "Cormorant" in content)
