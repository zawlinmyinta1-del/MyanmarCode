# app.py ၏ အဓိကအပိုင်းကို ဤသို့ပြင်ပါ
try:
    python_code = translate_code(user_input)
    # print ရလဒ်ကို ဖမ်းယူရန်
    import io
    from contextlib import redirect_stdout
    
    f = io.StringIO()
    with redirect_stdout(f):
        exec(python_code)
    out = f.getvalue()
    st.success(out)
except Exception as e:
    st.error(f"Error: {e}")
