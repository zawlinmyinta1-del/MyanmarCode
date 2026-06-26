# mapping.py 

myanmar_to_python = {
    # --- Control Flow ---
    "အကယ်၍": "if",
    "မ": "else",
    "မှန်ပါက": "elif",
    "တွင်": "for",
    "စဉ်": "while",
    "ပြီးတော့": ":",
    "အဆုံးသတ်": "break",
    "ဆက်လုပ်": "continue",
    
    # --- Input & Output ---
    "ထုတ် :": "print(",
    "ပြန်ပေး": "return",
    "ရယူ": "input",
    
    # --- Data & Operations ---
    "ဖြစ်သည်": "=",
    "စာရင်း": "list",
    "အစုံ": "set",
    "အမှန်": "True",
    "အမှား": "False",
    "ဘာမျှမဟုတ်": "None",
    
    # --- Structure & Logic ---
    "ထည့်": "import",
    "အမှားကိုဖမ်း": "try",
    "အမှားကိုဖြေ": "except",
    "ဖိုင်ဖွင့်": "open",
    "ဖိုင်ပိတ်": "close"
    # --- List Operations (စာရင်းများ) ---
    "စာရင်းအသစ်": "[]",
    "စာရင်းထဲထည့်": ".append(",
    "စာရင်းအလျား": "len(",
    "စာရင်းဖယ်ရှား": ".pop(",
}

def translate_code(code_text):
    # ၁။ စကားလုံးများကို အစားထိုးခြင်း
    translated = code_text
    for burmese, python in myanmar_to_python.items():
        translated = translated.replace(burmese, python)
    
    # ၂။ Print အတွက် ) ထည့်ပေးခြင်း
    final_lines = []
    for line in translated.split('\n'):
        # strip() သုံးပြီး space တွေကို ဖယ်ထုတ်ပြီးမှ စစ်ဆေးခြင်း
        clean_line = line.strip()
        if clean_line.startswith("print(") and not clean_line.endswith(")"):
            line = line.strip() + ")"
        final_lines.append(line)
        
    return '\n'.join(final_lines)