import io
from contextlib import redirect_stdout

def execute_mc(code_input):
    # ဤနေရာတွင် မြန်မာစကားလုံးများကို Python ကုဒ်အဖြစ် ဘာသာပြန်ခြင်း (Mapping)
    translated_code = code_input.replace("အကယ်၍", "if")
    translated_code = translated_code.replace("ပြီးတော့", ":") # ဥပမာ - အကယ်၍ 5 > 3 ပြီးတော့
    translated_code = translated_code.replace("ပြ", "print")
    
    # ရလဒ်ကို ဖမ်းယူရန်အတွက်
    f = io.StringIO()
    with redirect_stdout(f):
        try:
            # ဘာသာပြန်ထားသော ကုဒ်ကို Run ခြင်း
            exec(translated_code)
        except Exception as e:
            print(f"Error တက်နေပါတယ်: {e}")
            
    return f.getvalue()