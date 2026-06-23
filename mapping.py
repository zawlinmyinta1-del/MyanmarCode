def translate_code(myanmar_code):
    # ၁။ မြန်မာဂဏန်းတွေကို English ဂဏန်းအဖြစ် ပြောင်းရန်
    num_map = {'၀': '0', '၁': '1', '၂': '2', '၃': '3', '၄': '4', 
               '၅': '5', '၆': '6', '၇': '7', '၈': '8', '၉': '9'}
    
    translated = myanmar_code
    for burmese, english in num_map.items():
        translated = translated.replace(burmese, english)
        
    # ၂။ စကားလုံး Mapping
    mapping = {
        "ထုတ် :": "print(",
        "ဖြစ်သည်": "="
    }
    
    for burmese, python in mapping.items():
        translated = translated.replace(burmese, python)
        
    # ၃။ အရေးကြီးဆုံး: print() ဖွင့်ထားရင် အဆုံးမှာ ) ဖြည့်ပေးခြင်း
    if "print(" in translated:
        # နောက်ဆုံးမှာ ) မပါရင် ထည့်ပေးမယ်
        if not translated.strip().endswith(")"):
            translated = translated + ")"
            
    return translated
