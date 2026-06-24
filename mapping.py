def translate_code(myanmar_code):
    # ၁။ မြန်မာဂဏန်းများကို အင်္ဂလိပ်ဂဏန်းအဖြစ် ပြောင်းလဲခြင်း
    num_map = {'၀': '0', '၁': '1', '၂': '2', '၃': '3', '၄': '4', 
               '၅': '5', '၆': '6', '၇': '7', '၈': '8', '၉': '9'}
    
    translated = myanmar_code
    for b, e in num_map.items():
        translated = translated.replace(b, e)
        
    # ၂။ စကားလုံး Mapping
    mapping = {
        "ထုတ် :": "print(",
        "ဖြစ်သည်": "=",
        "အကယ်၍": "if",
        "မဟုတ်လျှင်": "else:"
    }
    
    for burmese, python in mapping.items():
        translated = translated.replace(burmese, python)
        
    # ၃။ Loop အတွက် အထူးပြင်ဆင်ချက် (Regex သုံးခြင်း)
    import re
    # 'loop 5:' ဆိုတဲ့ ပုံစံကို 'for i in range(5):' လို့ ပြောင်းပေးပါမယ်
    translated = re.sub(r'loop (\d+):', r'for i in range(\1):', translated)
        
    # ၄။ print() အတွက် နောက်ဆုံး ) ကို ဖြည့်ပေးခြင်း
    lines = translated.split('\n')
    processed_lines = []
    for line in lines:
        if "print(" in line and ")" not in line:
            line += ")"
        processed_lines.append(line)
            
    return '\n'.join(processed_lines)
