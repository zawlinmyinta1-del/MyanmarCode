import streamlit as st
import sys
import io
from mapping import translate_code, burmese_to_python

st.title("MyanmarCode (Python Converter)")

# စာရိုက်ရန်နေရာ
user_input = st.text_area("ဒီမှာ မြန်မာလို Code ရိုက်ပါ", height=150)

if st.button("Run"):
    try:
        # ဘာသာပြန်ခြင်း
        python_code = translate_code(user_input)
        
        # ပြောင်းသွားတဲ့ Code ကို ပြခြင်း
        st.write("ပြောင်းလဲလိုက်သော Python Code:")
        st.code(python_code, language='python')
        
        # ရလဒ်ကို အမှန်တကယ် Run ခြင်း
        st.write("ရလဒ်:")
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()
        exec(python_code)
        sys.stdout = old_stdout
        st.success(mystdout.getvalue())
        
    except Exception as e:
        st.error(f"Error: {e}")
