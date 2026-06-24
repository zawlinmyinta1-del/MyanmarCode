import streamlit as st
from mapping import translate_code

st.set_page_config(page_title="MyanmarCode Compiler", page_icon="💻")
st.title("💻 MyanmarCode Compiler")

# Variable တွေကို သိမ်းထားမယ့်နေရာ
if 'variables' not in st.session_state:
    st.session_state.variables = {}

code_input = st.text_area("ဒီမှာ Code ရိုက်ပါ", height=150)

if st.button("Run"):
    try:
        translated = translate_code(code_input)
        exec(translated, {}, st.session_state.variables)
        
        # ရလဒ်ကို အလှဆင်ပြီးပြသခြင်း
        st.success("✅ အောင်မြင်စွာ ဘာသာပြန်ပြီးပါပြီ")
        
        # Dictionary ထဲက တန်ဖိုးတွေကို အလှဆင်ပြသခြင်း
        if st.session_state.variables:
            st.info("မှတ်သားထားသော Variable များ:")
            for key, value in st.session_state.variables.items():
                st.write(f"🔹 **{key}** : `{value}`")
        
    except Exception as e:
        st.error(f"⚠️ အမှား - {e}")
