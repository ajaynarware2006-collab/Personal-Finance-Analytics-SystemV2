import streamlit as st
import pandas as pd
from backend.settings import get_user_expenses
import time

# -------------------- PAGE CONFIG --------------------

st.set_page_config(
    page_title="Expense History",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------- HIDE SIDEBAR --------------------

st.markdown("""
<style>

[data-testid="stSidebar"]{
    display:none;
}

[data-testid="stSidebarCollapsedControl"]{
    display:none;
}

div[data-testid="stMetric"]{
    background:#1c1c1c;
    padding:15px;
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# -------------------- USER --------------------

user_id = st.session_state.get("user_id")
if user_id is None:
    st.error("Please Login First")
    time.sleep(1)
    st.switch_page("app.py")

# -------------------- FETCH DATA --------------------

expenses = get_user_expenses(user_id)

expenses = pd.DataFrame(
    expenses,
    columns=[
        "Expense ID",
        "Category",
        "Amount",
        "Date"
    ]
)

# -------------------- FORMAT DATA --------------------

expenses["Amount"] = expenses["Amount"].apply(lambda x: f"₹{x:,.0f}")

expenses["Date"] = pd.to_datetime(expenses["Date"]).dt.strftime("%d %b %Y")

# -------------------- HEADER --------------------
if st.button("Exit"):
    st.switch_page("pages/dashboard.py")
st.title("📜 Expense History")
st.caption("Track every expense you've made.")

st.divider()

# -------------------- METRICS --------------------

total_expense = (
    expenses["Amount"]
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
    .sum()
)

transaction_count = len(expenses)

average = total_expense / transaction_count if transaction_count else 0

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "💰 Total Expense",
        f"₹{total_expense:,.0f}"
    )

with c2:
    st.metric(
        "🧾 Transactions",
        transaction_count
    )

with c3:
    st.metric(
        "📈 Average Expense",
        f"₹{average:,.0f}"
    )

st.divider()

# -------------------- FILTERS --------------------

col1, col2 = st.columns(2)

with col1:
    search = st.text_input(
        "🔍 Search Category"
    )

with col2:
    categories = ["All"] + sorted(expenses["Category"].unique().tolist())

    category = st.selectbox(
        "📂 Filter Category",
        categories
    )

filtered = expenses.copy()

if search:
    filtered = filtered[
        filtered["Category"].str.contains(
            search,
            case=False
        )
    ]

if category != "All":
    filtered = filtered[
        filtered["Category"] == category
    ]

st.divider()

# -------------------- TABLE --------------------

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)