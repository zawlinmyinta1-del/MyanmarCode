import streamlit as st
from mapping import translate_code

st.title("MyanmarCode Compiler")

# Variable များ သိမ်းဆည်းရန်
if 'vars' not in st.session_state:
    st.session_state.vars = {}

code = st.text_area("Code ရိုက်ပါ")
if st.button("Run"):
    try:
        py_code = translate_code(code)
        exec(py_code, {}, st.session_state.vars)
        st.success("အောင်မြင်သည်!")
        st.write(st.session_state.vars)
    except Exception as e:
        st.error(f"အမှား - {e}")
