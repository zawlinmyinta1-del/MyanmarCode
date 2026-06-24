def translate_code(myanmar_code):
    mapping = {
        "ထုတ် :": "print(",
        "ဖြစ်သည်": "=",
    }
    
    translated = myanmar_code
    for burmese, python in mapping.items():
        translated = translated.replace(burmese, python)
        
    # print အတွက် ) ပိတ်ပေးခြင်း
    if "print(" in translated:
        translated = translated + ")"
            
    return translated
