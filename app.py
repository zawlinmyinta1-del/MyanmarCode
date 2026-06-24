import streamlit as st
from mapping import translate_code

if 'my_vars' not in st.session_state:
    st.session_state.my_vars = {}

code_input = st.text_area("Code ရိုက်ပါ")
if st.button("Run"):
    try:
        translated = translate_code(code_input)
        # exec လုပ်တဲ့အခါ my_vars ကို သုံးပါမယ်
        exec(translated, {}, st.session_state.my_vars)
        st.write(st.session_state.my_vars)
    except Exception as e:
        st.error(f"အမှား - {e}")
