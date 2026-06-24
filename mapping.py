def translate_code(myanmar_code):
    # ဂဏန်းပြောင်းခြင်း
    num_map = {'၀': '0', '၁': '1', '၂': '2', '၃': '3', '၄': '4', '၅': '5'}
    translated = myanmar_code
    for b, e in num_map.items():
        translated = translated.replace(b, e)
    
    # Keyword များ
    mapping = {
        "ထုတ် :": "print(",
        "ဖြစ်သည်": "=",
    }
    
    for burmese, python in mapping.items():
        translated = translated.replace(burmese, python)
        
    # Strings များအတွက် ) ပိတ်ခြင်း
    lines = translated.split('\n')
    new_lines = []
    for line in lines:
        if "print(" in line and not line.strip().endswith(")"):
            line += ")"
        new_lines.append(line)
        
    return '\n'.join(new_lines)
