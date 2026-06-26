import streamlit as st
from mapping import translate_code

st.title("MyanmarCode Compiler")

<<<<<<< HEAD
st.sidebar.title("ကူညီမည့် စာရင်း (Cheat Sheet)")
for burmese, python_key in MY_DICT.items():
    st.sidebar.write(f"**{burmese}** = `{python_key}`")
    # app.py
code_text = st.text_area("ဒီနေရာမှာ မြန်မာလို Code ရေးပါ:", height=300)
# app.py
if st.button("Run လုပ်မည်"):
    result = run_myanmar_code(code_text)
    st.subheader("ရလဒ်:")
    st.text(result) # Code ပုံစံနဲ့ ပြပေးတာက ပိုကြည့်ကောင်းပါတယ်
=======
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
>>>>>>> d166621a50527ff7db25f9c4058f9e30e4262faf
