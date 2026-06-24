def translate_code(myanmar_code):
    # မြန်မာဂဏန်းပြောင်းခြင်း
    num_map = {'၀': '0', '၁': '1', '၂': '2', '၃': '3', '၄': '4', 
               '၅': '5', '၆': '6', '၇': '7', '၈': '8', '၉': '9'}
    
    translated = myanmar_code
    for b, e in num_map.items():
        translated = translated.replace(b, e)
        
    # Keyword များ ပြောင်းလဲခြင်း
    translated = translated.replace("ထုတ် :", "print(")
    translated = translated.replace("ဖြစ်သည်", "=")
    
    # Loop အတွက် အထူးပြင်ဆင်ချက်
    if "loop" in translated:
        # loop 5: ကို for i in range(5): ဖြစ်အောင် ပြောင်းခြင်း
        import re
        translated = re.sub(r'loop (\d+):', r'for i in range(\1):', translated)
            
    # ပိတ်စရာကျန်တဲ့ ) များကို ပိတ်ပေးခြင်း
    if "print(" in translated and not translated.strip().endswith(")"):
        translated = translated + ")"
            
    return translated
