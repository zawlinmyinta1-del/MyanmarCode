def translate_code(myanmar_code):
    # မြန်မာဂဏန်းကို အင်္ဂလိပ်ဂဏန်းပြောင်းရန် Mapping
    num_map = {'၀': '0', '၁': '1', '၂': '2', '၃': '3', '၄': '4', 
               '၅': '5', '၆': '6', '၇': '7', '၈': '8', '၉': '9'}
    
    translated = myanmar_code
    for burmese, english in num_map.items():
        translated = translated.replace(burmese, english)
        
    # ကျန်တဲ့ စကားလုံး Mapping များဆက်ထည့်ပါ
    mapping = {"ထုတ် :": "print(", "ဖြစ်သည်": "="}
    for burmese, python in mapping.items():
        translated = translated.replace(burmese, python)
        
    return translated
