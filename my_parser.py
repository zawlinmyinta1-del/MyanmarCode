from config import MY_DICT
import io
from contextlib import redirect_stdout

def run_myanmar_code(code_text):
    # စကားလုံးတွေကို အစားထိုးတဲ့အပိုင်း
    processed_code = code_text
    for burmese, python_key in MY_DICT.items():
        processed_code = processed_code.replace(burmese, python_key)
    
    # ရလဒ်ကို ဖမ်းယူတဲ့အပိုင်း
    f = io.StringIO()
    with redirect_stdout(f):
        try:
            # global တွေကို ထည့်ပေးခြင်းဖြင့် Python functions (input, print) တွေကို သိသွားပါမယ်
            exec(processed_code, globals())
        except Exception as e:
            print(f"Error တက်နေပါတယ်: {e}")