def translate_code(myanmar_code):
    # ၁။ မြန်မာဂဏန်းများကို အင်္ဂလိပ်ဂဏန်းအဖြစ် ပြောင်းလဲခြင်း
    num_map = {'၀': '0', '၁': '1', '၂': '2', '၃': '3', '၄': '4', 
               '၅': '5', '၆': '6', '၇': '7', '၈': '8', '၉': '9'}
    
    translated = myanmar_code
    for b, e in num_map.items():
        translated = translated.replace(b, e)
        
    # ၂။ စာသားများအတွက် Quote တွေကို ရှာဖွေပြီး ထိန်းသိမ်းခြင်း
    # (ဒီနေရာမှာ ရိုးရှင်းအောင် အရင်ဆုံး " ကို လက်ခံအောင်လုပ်ပါမယ်)
    
    # ၃။ Keyword Mapping
    mapping = {
        "ထုတ် :": "print(",
        "ဖြစ်သည်": "=",
        "အကယ်၍": "if",
        "မဟုတ်လျှင်": "else:",
        "loop": "for i in range("
    }
    
    for burmese, python in mapping.items():
        translated = translated.replace(burmese, python)
        
    # ၄။ Loop အတွက် အထူးပြင်ဆင်ချက်
    import re
    translated = re.sub(r'for i in range\((\d+)\)', r'for i in range(\1)', translated)
    
    # ၅။ print() အတွက် နောက်ဆုံး ) ကို ဖြည့်ပေးခြင်း
    if "print(" in translated and not translated.strip().endswith(")"):
        translated = translated + ")"
            
    return translated
