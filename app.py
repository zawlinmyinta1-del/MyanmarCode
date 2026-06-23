import streamlit as st
import sys
import io
from mapping import translate_code, burmese_to_python

st.title("MyanmarCode (Python Converter)")

# အသုံးပြုသူအတွက် စာရိုက်ရန်နေရာ
user_input = st.text_area("ဒီမှာ မြန်မာလို Code ရိုက်ပါ (ဥပမာ - ထုတ် : 'မင်္ဂလာပါ')", height=200)

if st.button("Run"):
    try:
        # ၁။ မြန်မာကို Python လို ပြောင်းမယ်
        python_code = translate_code(user_input)
        
        # ၂။ ပြောင်းသွားတဲ့ Code ကို ပြမယ်
        st.subheader("ပြောင်းလဲလိုက်သော Python Code:")
        st.code(python_code, language='python')
        
        # ၃။ Code ကို တကယ် Run မယ်
        st.subheader("ရလဒ်:")
        # ရလဒ်ကို ဖမ်းယူရန်
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()
        
        exec(python_code)
        
        sys.stdout = old_stdout
        st.write(mystdout.getvalue()) # ရလဒ်ကို Screen ပေါ် ပြမယ်
        
    except Exception as e:
        st.error(f"အမှားအယွင်းရှိသည်: {e}")

# ဘေးမှာ Cheat Sheet ပြပေးမယ်
st.sidebar.title("ကူညီမည့် စာရင်း (Cheat Sheet)")
for burmese, python in burmese_to_python.items():
    st.sidebar.write(f"**{burmese}** = `{python}`")
