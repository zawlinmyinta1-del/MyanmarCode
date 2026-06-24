def translate_code(myanmar_code):
    # မြန်မာဂဏန်းပြောင်းခြင်း
    num_map = {'၀': '0', '၁': '1', '၂': '2', '၃': '3', '၄': '4', 
               '၅': '5', '၆': '6', '၇': '7', '၈': '8', '၉': '9'}
    
    translated = myanmar_code
    for b, e in num_map.items():
        translated = translated.replace(b, e)
        
    # Mapping အသစ် (အမှားမရှိအောင် သေချာပြင်ထားသည်)
    mapping = {
        "ထုတ် :": "print(",
        "ဖြစ်သည်": "=",
        "အကယ်၍": "if",
        "မဟုတ်လျှင်": "else:",
        "loop ": "for i in range(" 
    }
    
    for burmese, python in mapping.items():
        translated = translated.replace(burmese, python)
        
    # Loop အတွက် နောက်ဆုံးပိတ် ) နဲ့ : ကို ထည့်ပေးခြင်း
    if "for i in range(" in translated:
        # ဥပမာ - loop 5: ကို for i in range(5): ဖြစ်အောင် လုပ်ခြင်း
        if ":" not in translated:
            translated = translated.replace("range(", "range(").replace("):", "") + "):"
            
    return translated
