import streamlit as st
import sys
import io
from mapping import translate_code

# Global variables ကို သိမ်းထားမယ့်နေရာ
if 'my_globals' not in st.session_state:
    st.session_state.my_globals = {}

st.title("MyanmarCode (Variable Support)")

user_input = st.text_area("ဒီမှာ Code ရိုက်ပါ (ဥပမာ - က ဖြစ်သည် ၁၀)", height=150)

if st.button("Run"):
    try:
        python_code = translate_code(user_input)
        
        # Output ဖမ်းယူရန်
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()
        
        # အရေးကြီးဆုံး: st.session_state.my_globals ကို ထည့်သွင်းပေးခြင်း
        exec(python_code, st.session_state.my_globals)
        
        sys.stdout = old_stdout
        st.success(f"ရလဒ်: {mystdout.getvalue()}")
        st.write("လက်ရှိသိမ်းထားသော Variables:", st.session_state.my_globals)
        
    except Exception as e:
        st.error(f"Error: {e}")
