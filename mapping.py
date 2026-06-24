def translate_code(myanmar_code):
    # အရေးကြီးဆုံးအချက်: မြန်မာဂဏန်းတွေကို အင်္ဂလိပ်ဂဏန်းအဖြစ် အရင်ပြောင်းပါ
    num_map = {'၀': '0', '၁': '1', '၂': '2', '၃': '3', '၄': '4', 
               '၅': '5', '၆': '6', '၇': '7', '၈': '8', '၉': '9'}
    
    translated = myanmar_code
    for burmese, english in num_map.items():
        translated = translated.replace(burmese, english)
        
    # ကျန်တဲ့ Keyword တွေ Mapping လုပ်ပါ
    mapping = {
        "ထုတ် :": "print(",
        "ဖြစ်သည်": "=",
        "အကယ်၍": "if",
        "မဟုတ်လျှင်": "else:"
    }
    
    for burmese, python in mapping.items():
        translated = translated.replace(burmese, python)
        
    return translated
