from config import MY_DICT
import io
from contextlib import redirect_stdout

def run_myanmar_code(code_text):
    processed_code = code_text
    # မြန်မာစကားလုံးတွေကို Python စကားလုံးအဖြစ် အစားထိုးခြင်း
    for burmese, python_key in MY_DICT.items():
        processed_code = processed_code.replace(burmese, python_key)
    
    f = io.StringIO()
    with redirect_stdout(f):
        try:
            # အလုပ်လုပ်တဲ့အပိုင်း (Exec)
            exec(processed_code)
        except Exception as e:
            print(f"အမှားရှိနေပါတယ် : {e}")
            
    return f.getvalue()