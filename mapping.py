def translate_code(myanmar_code):
    # Mapping ထဲမှာ '=' ကို 'ဖြစ်သည်' နဲ့ တွဲပေးထားတယ်
    mapping = {
        "ထုတ် :": "print(",
        "ရိုက်သည်": "input",
        "ဖြစ်သည်": "=",  # ဒီမှာ 'ဖြစ်သည်' ကို '=' အဖြစ် ပြောင်းပေးမှာပါ
        "မှန်": "True",
        "မှား": "False"
    }
    
    translated = myanmar_code
    for burmese, python in mapping.items():
        translated = translated.replace(burmese, python)
    
    # print အတွက် logic
    if "print(" in translated and not translated.strip().endswith(")"):
        translated = translated + ")"
        
    return translated
