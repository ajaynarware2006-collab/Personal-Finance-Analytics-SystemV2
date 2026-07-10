import streamlit as st
from backend.varification import signup
from pages.helper import hide_sidebar

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Singup",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)
hide_sidebar()

password=st.session_state.get("password")
name=st.session_state.get("name")
income=st.number_input(label="Income",placeholder="Enter Your Monthly Income",value=None)
budget=st.number_input(label="Budget",placeholder="Enter Your Monthly Budget",value=None)


if st.button("Confirm"):

    if not income:
        st.error("Income cannot be Empty")
    elif not budget:
        st.error("Budget cannot be Empty")
    else:

        user_id=signup(name,income,password,budget)

        if not user_id:
            st.error("Something went wrong")
        
        else:
            st.session_state["user_id"]=user_id
            st.success(f"Successfully Registered")
            st.session_state["user_id"]=user_id[0]
            st.switch_page("pages/dashboard.py")
    
        


