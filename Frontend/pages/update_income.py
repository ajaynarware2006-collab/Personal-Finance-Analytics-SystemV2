import streamlit as st
from backend.income_operation import update_income
import time 

user_id=st.session_state.get("user_id")
st.set_page_config(
    page_title="login",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}

[data-testid="stSidebarCollapsedControl"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

income=st.number_input(label="new income",placeholder="Enter new income",value=None,)


if st.button("Update"):
    if income:
        income=int(income)
        success=update_income(income=income,user_id=user_id)
        st.success(success)
        time.sleep(1)
        st.switch_page("pages/dashboard.py")
    else:
        st.error("Enter income first")