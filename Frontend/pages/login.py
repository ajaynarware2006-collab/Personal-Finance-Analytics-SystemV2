import streamlit as st
from backend.connection import connecting

connection,cursor=connecting()


st.set_page_config(
    page_title="login",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)
st.markdown("<h1 style='background: linear-gradient(to right, #08203E, #557C93); -webkit-background-clip: text; background-clip: text; color: transparent;text-align:center;'>PERSONAL FINANCE ANALYTICS SYSTEM</h1>",unsafe_allow_html=True)

with st.form("login"):
    st.markdown("<h1 style='background: linear-gradient(to right, #C11E38, #220B34); -webkit-background-clip: text; background-clip: text; color: transparent;text-align:center;'>WELCOME TO THE APP</h1>",unsafe_allow_html=True)


    name = st.text_input("Name")

    password = st.text_input("Password", type="password")

    submit = st.form_submit_button("Login")

if submit:
    if not name:
        st.error("Plese Enter Your Name")
    
    elif not password:
        st.error("Password cannot be empty")

    else:
        cursor.execute("SELECT user_id,name,password FROM users WHERE name=%s AND password=%s",(name,password))

        user=cursor.fetchone()

        if not user:
            st.error("User not found")

        else:
            st.success("Login Successfully")
            st.session_state["user_id"]=user[0]
            st.switch_page("pages/dashboard.py")

