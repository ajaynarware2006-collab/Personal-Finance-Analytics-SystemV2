import streamlit as st
from backend.varification import login
from pages.helper import hide_sidebar,text_gredient
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="login",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

hide_sidebar()
text_gredient("PERSONAL FINANCE ANALYTICS SYSTEM")

with st.form("login"):
    st.markdown("<h1 style='background: linear-gradient(to right, #C11E38, #220B34); -webkit-background-clip: text; background-clip: text; color: transparent;text-align:center;'>WELCOME BACK</h1>",unsafe_allow_html=True)

    name = st.text_input("Name")

    password = st.text_input("Password", type="password")

    submit = st.form_submit_button("Login")

if submit:
    if not name:
        st.error("Plese Enter Your Name")
    
    elif not password:
        st.error("Password cannot be empty")

    else:
        user=login(name=name,password=password)

        if not user:
            st.error("User not found")

        else:
            st.success("Login Successfully")

            st.session_state["user_id"]=user[0]
            
            st.switch_page("pages/dashboard.py")

