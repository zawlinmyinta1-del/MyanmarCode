def translate_code(myanmar_code):
    # မြန်မာစကားလုံးတွေကို Python စကားလုံးအဖြစ် အစားထိုးခြင်း
    mapping = {
        "ထုတ် :": "print(",
        "ရိုက်သည်": "input",
        "ဖြစ်သည်": "=",
        "မှန်": "True",
        "မှား": "False"
    }
    
    translated = myanmar_code
    for burmese, python in mapping.items():
        translated = translated.replace(burmese, python)
        
    # Python မှာ print( ... ) ဆိုတဲ့ ပုံစံဖြစ်အောင် အဆုံးမှာ ')' ကို အလိုအလျောက်ဖြည့်ပေးခြင်း
    if "print(" in translated and not translated.strip().endswith(")"):
        translated = translated + ")"
        
    return translated
