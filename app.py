import streamlit as st
from mapping import translate_code

st.title("MyanmarCode Compiler")

# Variable တွေကို သိမ်းထားဖို့အတွက်
if 'vars' not in st.session_state:
    st.session_state.vars = {}

code_input = st.text_area("Code ရိုက်ပါ (ဥပမာ - ထုတ် : 'Hello')")

if st.button("Run"):
    try:
        # ဘာသာပြန်ခြင်း
        py_code = translate_code(code_input)
        # အလုပ်လုပ်ခြင်း
        exec(py_code, {}, st.session_state.vars)
        st.success("အောင်မြင်သည်!")
        st.write(st.session_state.vars)
    except Exception as e:
        st.error(f"အမှား - {e}")
