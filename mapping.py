def translate_code(myanmar_code):
    # ၁။ မြန်မာဂဏန်းတွေကို English ဂဏန်းအဖြစ် ပြောင်းရန် Mapping
    num_map = {'၀': '0', '၁': '1', '၂': '2', '၃': '3', '၄': '4', 
               '၅': '5', '၆': '6', '၇': '7', '၈': '8', '၉': '9'}
    
    translated = myanmar_code
    for burmese, english in num_map.items():
        translated = translated.replace(burmese, english)
        
    # ၂။ စကားလုံး Mapping
    mapping = {
        "ထုတ် :": "print(",
        "ဖြစ်သည်": "=",
        "အကယ်၍": "if",
        "မဟုတ်လျှင်": "else:" 
    }
    
    for burmese, python in mapping.items():
        translated = translated.replace(burmese, python)
        
    # ၃။ အကယ်၍ (if) နောက်မှာ : မပါရင် ဖြည့်ပေးခြင်း
    if "if" in translated and not translated.strip().endswith(":"):
        translated = translated + ":"
        
    # ၄။ print အတွက် ) ဖြည့်ပေးခြင်း
    if "print(" in translated and not translated.strip().endswith(")"):
        translated = translated + ")"
            
    return translated
