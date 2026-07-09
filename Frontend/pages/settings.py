import streamlit as st
def settings():
    with st.popover("⚙️ Settings"):
        if st.button("Add Expense"):
            st.switch_page("pages/add_expense.py")

        if st.button("Delete Expense"):
            st.switch_page("pages/delete_expense.py")

        if st.button("Update Expense"):
            st.switch_page("pages/update_expense.py")

        if st.button("Update Income"):
            st.switch_page("pages/update_income.py")

        if st.button("History"):
            st.switch_page("pages/history.py")

        if st.button("Logout"):
            st.switch_page("app.py")