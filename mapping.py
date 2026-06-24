def translate_code(myanmar_code):
    # မြန်မာဂဏန်းများကို ပြောင်းလဲခြင်း
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
        "မဟုတ်လျှင်": "else:",
        "loop": "for i in range("
    }
    
    for burmese, python in mapping.items():
        translated = translated.replace(burmese, python)
        
    # Parentheses ပြဿနာကို ဖြေရှင်းခြင်း
    # print() နဲ့ loop တွေအတွက် ) ကို စနစ်တကျ ပြန်ပိတ်ပေးပါမည်
    lines = translated.split('\n')
    processed_lines = []
    for line in lines:
        if "print(" in line and ")" not in line:
            line += ")"
        if "for i in range(" in line and ")" not in line:
            line += ")"
        processed_lines.append(line)
        
    return '\n'.join(processed_lines)
