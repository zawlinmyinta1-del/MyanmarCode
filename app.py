# app.py ဖိုင်ရဲ့ အပေါ်ဆုံးမှာ ဒီလိုရေးပါ
import streamlit as st
from config import MY_DICT
from my_parser import run_myanmar_code  # <--- ဒီစာကြောင်းလေး လိုနေတာပါ

# ကျန်တဲ့ code တွေ...

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