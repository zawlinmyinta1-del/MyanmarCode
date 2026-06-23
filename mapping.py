def translate_code(myanmar_code):
    # ၁။ မြန်မာဂဏန်းတွေကို English ဂဏန်းအဖြစ် ပြောင်းရန် Mapping
    burmese_numerals = {
        '၀': '0', '၁': '1', '၂': '2', '၃': '3', '၄': '4',
        '၅': '5', '၆': '6', '၇': '7', '၈': '8', '၉': '9'
    }
    
    # ၂။ စကားလုံး Mapping
    mapping = {
        "ထုတ် :": "print(",
        "ရိုက်သည်": "input",
        "ဖြစ်သည်": "=",
        "မှန်": "True",
        "မှား": "False"
    }
    
    translated = myanmar_code
    
    # ဂဏန်းတွေကို အရင်ပြောင်း
    for burmese, english in burmese_numerals.items():
        translated = translated.replace(burmese, english)
        
    # စကားလုံးတွေကို ပြောင်း
    for burmese, python in mapping.items():
        translated = translated.replace(burmese, python)
    
    # print အတွက် bracket ပိတ်ပေးခြင်း
    if "print(" in translated and not translated.strip().endswith(")"):
        translated = translated + ")"
        
    return translated
