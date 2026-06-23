# MyanmarCode မှ Python သို့ ပြောင်းလဲပေးမည့် အဘိဓာန်
burmese_to_python = {
    "ထုတ်": "print",
    "ရိုက်သည်": "input",
    "ဖြစ်သည်": "=",
    "မှန်": "True",
    "မှား": "False",
    "အကယ်၍": "if",
    "မဟုတ်ရင်": "else",
    "အအတွက်": "for",
    "ပြီးဆုံး": "break",
    "ဆက်လုပ်": "continue"
}

def translate_code(myanmar_code):
    translated = myanmar_code
    for burmese, python in burmese_to_python.items():
        translated = translated.replace(burmese, python)
    return translated
