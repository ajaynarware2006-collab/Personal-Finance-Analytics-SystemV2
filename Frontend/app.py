import streamlit as st
from pages.helper import hide_sidebar
from backend.varification import login
import time
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


hide_sidebar()

st.set_page_config(
    page_title="home",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)
st.markdown("<h1 style='background: linear-gradient(to right, #08203E, #557C93); -webkit-background-clip: text; background-clip: text; color: transparent;text-align:center;'>PERSONAL FINANCE ANALYTICS SYSTEM</h1>",unsafe_allow_html=True)
with st.form("sign_up"):
    st.markdown("<h1 style='background: linear-gradient(to right, #C11E38, #220B34); -webkit-background-clip: text; background-clip: text; color: transparent;text-align:center;'>WELCOME TO THE APP</h1>",unsafe_allow_html=True)


    name = st.text_input("Name")

    password = st.text_input("Password", type="password")

    confirm_pass= st.text_input("Confirm Password", type="password")

    submit = st.form_submit_button("Sign up")

if submit:
    if not name:
        st.error("Plese Enter Your Name")
    
    elif not password and not confirm_pass:
        st.error("Password cannot be empty")

    elif password != confirm_pass:
        st.error("Password does not match")

    else:
        
        st.session_state["name"]=name
        st.session_state["password"]=password

        user=login(name=name,password=password)

        if not user:
            st.switch_page("pages/signup.py")

        else:
            st.warning("Already have an account")
            time.sleep(1)
            st.switch_page("pages/login.py")
    
col1,col2=st.columns([4,1])
with col1:
    st.markdown(" ### Already have an account ?")
with col2:
    if st.button("Login"):
        st.switch_page("pages/login.py")
