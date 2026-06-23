import streamlit as st
import sys
import io
from mapping import translate_code

st.title("MyanmarCode (Python Converter)")

user_input = st.text_area("ဒီမှာ မြန်မာလို Code ရိုက်ပါ", height=150)

if st.button("Run"):
    # ဘာသာပြန်ခြင်း
    python_code = translate_code(user_input)
    st.write("ပြောင်းလဲလိုက်သော Python Code:")
    st.code(python_code, language='python')
    
    # ရလဒ်ကို အမှန်တကယ် Run ခြင်း
    st.write("ရလဒ်:")
    
    try:
        # Output ကို ဖမ်းယူရန်
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()
        
        exec(python_code)
        
        sys.stdout = old_stdout
        st.success(mystdout.getvalue())
    except Exception as e:
        # ဒီနေရာမှာ Error အမှန်ကို ပြပေးမယ်
        st.error(f"Error အမှားအယွင်း: {str(e)}")
