def translate_code(myanmar_code):
    # အဓိက Keyword များ
    mapping = {
        "ထုတ် :": "print(",
        "ဖြစ်သည်": "=",
    }
    translated = myanmar_code
    for burmese, python in mapping.items():
        translated = translated.replace(burmese, python)
        
    # Print function များအတွက် ) ထည့်ပေးခြင်း
    final_lines = []
    for line in translated.split('\n'):
        if line.startswith("print(") and not line.endswith(")"):
            line += ")"
        final_lines.append(line)
    return '\n'.join(final_lines)
