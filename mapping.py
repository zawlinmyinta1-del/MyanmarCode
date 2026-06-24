def translate_code(myanmar_code):
    # မြန်မာဂဏန်းပြောင်းခြင်း
    num_map = {'၀': '0', '၁': '1', '၂': '2', '၃': '3', '၄': '4', 
               '၅': '5', '၆': '6', '၇': '7', '၈': '8', '၉': '9'}
    
    translated = myanmar_code
    for b, e in num_map.items():
        translated = translated.replace(b, e)
        
    # Keyword Mapping
    mapping = {
        "ထုတ် :": "print(",
        "ဖြစ်သည်": "=",
        "အကယ်၍": "if",
        "မဟုတ်လျှင်": "else:" 
    }
    
    for burmese, python in mapping.items():
        translated = translated.replace(burmese, python)
        
    # print အတွက် ) ပိတ်ပေးခြင်း
    if "print(" in translated and not translated.strip().endswith(")"):
        translated = translated + ")"
            
    return translated
