# မြန်မာမှ Python သို့ ပြောင်းလဲပေးမည့် အဘိဓာန်
burmese_to_python = {
    "ထုတ် :": "print(",
    "ရိုက်သည်": "input",
    "ဖြစ်သည်": "=",
    "မှန်": "True",
    "မှား": "False",
    "အကယ်၍": "if",
    "မဟုတ်ရင်": "else",
    "အအတွက်": "for"
}

def translate_code(myanmar_code):
    translated = myanmar_code
    # စကားလုံးတွေကို အစားထိုးမယ်
    for burmese, python in burmese_to_python.items():
        translated = translated.replace(burmese, python)
    
    # print အတွက် bracket ပိတ်ပေးခြင်း
    if "print(" in translated and not translated.strip().endswith(")"):
        translated = translated + ")"
        
    return translated
