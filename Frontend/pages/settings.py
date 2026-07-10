import streamlit as st
from pages.helper import button
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

def settings():
    with st.popover("⚙️ Settings"):
        button()
        if st.button("Add Expense"):
            st.switch_page("pages/add_expense.py")

        if st.button("Update Income"):
            st.switch_page("pages/update_income.py")

        if st.button("History"):
            st.switch_page("pages/history.py")

        if st.button("Logout"):
            st.switch_page("app.py")