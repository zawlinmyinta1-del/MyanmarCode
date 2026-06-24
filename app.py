import streamlit as st
from mapping import translate_code

st.title("MyanmarCode Compiler")

# Variable တွေကို သိမ်းထားမယ့်နေရာ
if 'variables' not in st.session_state:
    st.session_state.variables = {}

code_input = st.text_area("ဒီမှာ Code ရိုက်ပါ")

if st.button("Run"):
    try:
        translated = translate_code(code_input)
        # တွက်ချက်ခြင်း
        exec(translated, {}, st.session_state.variables)
        st.success("ရလဒ်:")
        st.write(st.session_state.variables)
    except Exception as e:
        st.error(f"အမှား - {e}")
