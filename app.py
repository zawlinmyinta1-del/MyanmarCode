import streamlit as st
from mapping import translate_code

st.title("MyanmarCode Compiler")
code_input = st.text_area("ဒီမှာ Code ရိုက်ပါ", height=200)

if st.button("Run"):
    try:
        # ဘာသာပြန်ခြင်း
        translated_code = translate_code(code_input)
        
        # ရလဒ်ထုတ်ပြခြင်း
        st.write("Compiler ရလဒ်:")
        exec(translated_code)
        
    except SyntaxError:
        st.error("အမှား - ဆရာ့ Code ရိုက်ချက်မှာ စာလုံးပေါင်း (သို့) Syntax မှားနေပါတယ်။")
    except NameError:
        st.error("အမှား - ဆရာ အသုံးပြုထားတဲ့ Variable ကို မသတ်မှတ်ရသေးပါဘူး။")
    except Exception as e:
        # အခြားမမျှော်လင့်ထားတဲ့ အမှားများအတွက်
        st.error(f"အမှား - {e}")
