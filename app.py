import streamlit as st
import sys
import io
from mapping import translate_code

# Variable များ မှတ်သားရန်
if 'my_globals' not in st.session_state:
    st.session_state.my_globals = {}

st.title("MyanmarCode Compiler")

code_input = st.text_area("ဒီမှာ Code ရိုက်ပါ", height=200)

if st.button("Run"):
    try:
        # ဘာသာပြန်ခြင်း
        translated_code = translate_code(code_input)
        
        # Output ဖမ်းယူရန်
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()
        
        # Run လုပ်ခြင်း
        exec(translated_code, st.session_state.my_globals)
        
        sys.stdout = old_stdout
        st.success("ရလဒ်:")
        st.write(mystdout.getvalue())
        
    except Exception as e:
        st.error(f"Error တက်နေသည်: {e}")
