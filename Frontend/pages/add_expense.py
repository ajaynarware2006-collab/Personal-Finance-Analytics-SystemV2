import streamlit as st
import time
from backend.settings import add_expense
from backend.category_operations import view_categories
from  Frontend.pages.helper import card_css


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Add expense",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------------------- USER --------------------
user_id = st.session_state.get("user_id")
if user_id is None:
    st.error("Please Login First")
    time.sleep(1)
    st.switch_page("app.py")

# ---------------- CSS ---------------- #

card_css()

# ---------------- TITLE ---------------- #

st.title("💰 Add Expense")
st.caption("Keep track your expenses.")

st.write("")

# ---------------- CARD ---------------- #

with st.container(border=True):

    st.subheader("Expense datilas")

    all_category=view_categories()
    map_category={}
    for category in all_category:
        map_category[category[0]]=category[1]
    

    category_id=st.radio("Select category",options=[i for i in map_category])
    category_id=map_category[category_id]
    Amount = st.number_input(
        "Amount Spend (₹)",
        min_value=0,
        placeholder="Enter your amount",
        step=1
    )

    description=st.text_input("Enter discribtion (OPTIONAL)")

    payment=st.radio("Select your payment method",options=["Card","UPI","Cash"])

    st.write("")

    if st.button("💾 Add Expense"):

        if not Amount:
            st.error("Amount cannot be empty")

        else:
            success = add_expense(
                category_id=category_id,
                user_id=user_id,
                amount=Amount,
                description=description,
                pay_method=payment
            )

            st.success(success)

            st.balloons()

            time.sleep(1)

            st.switch_page("pages/dashboard.py")
