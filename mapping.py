def translate_code(myanmar_code):
    # မြန်မာဂဏန်းများကို အင်္ဂလိပ်ဂဏန်းအဖြစ် ပြောင်းလဲခြင်း
    num_map = {'၀': '0', '၁': '1', '၂': '2', '၃': '3', '၄': '4', 
               '၅': '5', '၆': '6', '၇': '7', '၈': '8', '၉': '9'}
    
    translated = myanmar_code
    for burmese, english in num_map.items():
        translated = translated.replace(burmese, english)
        
    # 'ထုတ် :' ကို 'print(' အဖြစ်ပြောင်း
    # variable ဖြစ်ရင် quotation mark မပါဘဲ 'print(က)' လို့ ဖြစ်ရပါမယ်
    if "ထုတ် :" in translated:
        translated = translated.replace("ထုတ် :", "print(")
        # အကယ်၍ နောက်မှာ " ပါရင် quotation mark ဖြစ်သွားလို့ Error တက်နိုင်ပါတယ်
        # ဒါကြောင့် bracket ပိတ်ဖို့ပဲ ဂရုစိုက်ရပါမယ်
    
    # ကျန်တဲ့ mapping များ
    mapping = {"ဖြစ်သည်": "="}
    for burmese, python in mapping.items():
        translated = translated.replace(burmese, python)
        
    return translated
