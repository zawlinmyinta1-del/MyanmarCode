import streamlit as st
from my_parser import execute_mc

# Page setup လုပ်ခြင်း
st.set_page_config(page_title="Python Myanmar App", layout="wide")

# Sidebar မှာ GitBook Link ထည့်ခြင်း
st.sidebar.title("📚 သင်ခန်းစာများ")
st.sidebar.markdown("[📖 Python Myanmar Guideline ကို ဖတ်ရန်](https://python-myanmar.gitbook.io/python-myanmar-docs/)")
# (မှတ်ချက် - ဒီလင့်ခ်နေရာမှာ ဆရာ့ GitBook ရဲ့ Publish Link အမှန်ကို ထည့်ပါ)

st.title("Python Myanmar Code Executor")

# ကုဒ်ရိုက်ရန် နေရာ
user_code = st.text_area("သင်၏ မြန်မာကုဒ်ကို ရိုက်ပါ:")

if st.button("Run"):
    if user_code:
        # ဘာသာပြန်ပြီး Run ပေးပါ
        output = execute_mc(user_code)
        st.write("ရလဒ် (Output):")
        st.code(output)
    else:
        st.warning("ကုဒ် အရင်ရိုက်ပေးပါဦး!")