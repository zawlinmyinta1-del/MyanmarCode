import streamlit as st
import sys
import io
from mapping import translate_code, burmese_to_python

st.title("MyanmarCode (Python Converter)")

# အသုံးပြုသူအတွက် စာရိုက်ရန်နေရာ
user_input = st.text_area("ဒီမှာ မြန်မာလို Code ရိုက်ပါ (ဥပမာ - ထုတ် : 'မင်္ဂလာပါ')", height=200)

if st.button("Run"):
    try:
        # ၁။ ဘာသာပြန်ခြင်း
        python_code = translate_code(user_input)
        
        # ၂။ ပြောင်းလဲသွားသော Code ကို ပြခြင်း
        st.subheader("ပြောင်းလဲလိုက်သော Python Code:")
        st.code(python_code, language='python')
        
        # ၃။ ရလဒ်ကို အမှန်တကယ် Run ခြင်း
        st.subheader("ရလဒ်:")
        
        # ရလဒ်ကို ဖမ်းယူရန် (Redirect stdout)
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()
        
        # Code ကို တကယ် Run မယ်
        exec(python_code)
        
        sys.stdout = old_stdout
        # ရလဒ်ကို App ပေါ်မှာ ပြမယ်
        st.success(mystdout.getvalue())
        
    except Exception as e:
        st.error(f"အမှားအယွင်းရှိသည်: {e}")

# ဘေးမှာ Cheat Sheet ပြပေးမယ်
st.sidebar.title("ကူညီမည့် စာရင်း (Cheat Sheet)")
for burmese, python in burmese_to_python.items():
    st.sidebar.write(f"**{burmese}** = `{python}`")
