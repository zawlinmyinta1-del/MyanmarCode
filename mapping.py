def translate_code(myanmar_code):
    # ၁။ ဂဏန်းပြောင်းခြင်း
    num_map = {'၀': '0', '၁': '1', '၂': '2', '၃': '3', '၄': '4', 
               '၅': '5', '၆': '6', '၇': '7', '၈': '8', '၉': '9'}
    translated = myanmar_code
    for b, e in num_map.items():
        translated = translated.replace(b, e)
        
    # ၂။ Keyword Mapping
    mapping = {
        "ထုတ် :": "print(",
        "ဖြစ်သည်": "=",
        "အကယ်၍": "if",
        "မဟုတ်လျှင်": "else:"
    }
    for b, p in mapping.items():
        translated = translated.replace(b, p)
        
    # ၃။ အကယ်၍ (if) စာကြောင်းအတွက် : ဖြည့်ပေးခြင်း
    if "if" in translated and not translated.strip().endswith(":"):
        translated = translated + ":"
        
    # ၄။ print အတွက် ) ဖြည့်ပေးခြင်း
    if "print(" in translated and not translated.strip().endswith(")"):
        translated = translated + ")"
            
    return translated
