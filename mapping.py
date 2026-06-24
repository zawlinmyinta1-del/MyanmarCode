def translate_code(myanmar_code):
    # ၁။ ဂဏန်းပြောင်းခြင်း
    num_map = {'၀': '0', '၁': '1', '၂': '2', '၃': '3', '၄': '4', '၅': '5'}
    translated = myanmar_code
    for b, e in num_map.items():
        translated = translated.replace(b, e)
    
    # ၂။ Keyword များ
    mapping = {
        "ထုတ် :": "print(",
        "ဖြစ်သည်": "=",
    }
    for burmese, python in mapping.items():
        translated = translated.replace(burmese, python)
        
    return translated
