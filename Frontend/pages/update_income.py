import streamlit as st
from backend.income_operation import update_income
import time
from  pages.helper import card_css


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Update Income",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

user_id = st.session_state.get("user_id")

# ---------------- CSS ---------------- #

card_css()

# ---------------- TITLE ---------------- #

st.title("💰 Update Monthly Income")
st.caption("Keep your monthly income updated for accurate financial insights.")

st.write("")

# ---------------- CARD ---------------- #

with st.container(border=True):

    st.subheader("Income Details")

    income = st.number_input(
        "Monthly Income (₹)",
        min_value=0,
        placeholder="Enter your monthly income",
        step=1000
    )

    st.write("")

    if st.button("💾 Update Income"):

        if income > 0:

            success = update_income(
                income=int(income),
                user_id=user_id
            )

            st.success(success)

            st.balloons()

            time.sleep(1)

            st.switch_page("pages/dashboard.py")

        else:

            st.warning("Please enter a valid income.")