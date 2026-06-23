def translate_code(myanmar_code):
    # ... (အပေါ်က ဂဏန်းပြောင်းတဲ့ Logic တွေ ထားခဲ့ပါ) ...
    
    mapping = {
        "ထုတ် :": "print(",
        "ဖြစ်သည်": "=",
        "အကယ်၍": "if",
        "မဟုတ်လျှင်": "else:" # else နောက်မှာ : ပါမှ Python က သိပါတယ်
    }
    
    translated = myanmar_code
    for burmese, python in mapping.items():
        translated = translated.replace(burmese, python)
        
    # (အပေါ်က Bracket ပိတ်တဲ့ Logic တွေကိုလည်း ထားခဲ့ပါ)
    return translated
