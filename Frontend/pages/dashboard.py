from backend.income_operation import view_income
from backend.analytics import current_month_expense,top_category,highest_expense,lowest_expense,total_savings,budget_remaining,monthly_savings,monthly_expense,yearly_expense,average_daily_expense,category_summary
import streamlit as st
import pandas as pd
import plotly.express as px
from Frontend.pages.settings import settings

st.set_page_config(
    page_title="dashborad",
    page_icon="🤖",
    layout="wide",
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
user_id=st.session_state.get("user_id")
settings()
st.markdown("<h1 style='background: linear-gradient(to right, #08203E, #557C93); -webkit-background-clip: text; background-clip: text; color: transparent;text-align:center;padding-top:-20px;padding-bottom:40px;'>PERSONAL FINANCE DASHBOARD</h1>",unsafe_allow_html=True)


col1,col2,col3,col4=st.columns([1,1,1,1],gap="large")

with col1:
    st.metric(label="💰 Income",value=f"₹{view_income(user_id)}")

with col2:

    st.metric(label="🏆 Top Category",value=f"₹{top_category(user_id)}")

with col3:
    st.metric(label="📈 Highest Expense",value=f"₹{highest_expense(user_id)}")


with col4:
    st.metric(label="📉 Lowest Expense",value=f"₹{lowest_expense(user_id)}")


st.markdown("<BR><BR><BR><BR><BR>",unsafe_allow_html=True)
col5,col6=st.columns([1,3])

with col5:
    st.metric("💵TOTAL SAVING YOU HAVE",value=f"₹{total_savings(user_id)}")
    st.markdown("<BR><BR><BR>",unsafe_allow_html=True)
    st.metric("🎯BUDGET REMAINING",value=f"₹{budget_remaining(user_id)}")

with col6:
    df=pd.DataFrame(category_summary(user_id))
    fig=px.pie(df,names=0,values=2)
    st.plotly_chart(fig)


col7,col8=st.columns(2)

with col7:
    monthly_exp=monthly_expense(user_id)
    if not monthly_exp:
        st.warning("No data to display yet.")
    else:
        df=pd.DataFrame(monthly_exp)
        df.columns=["Month","Expense"]
        df["Expense"] = df["Expense"].astype(float)
        st.line_chart(df,x="Month",y="Expense")


with col8:
    yearly_exp=yearly_expense(user_id)
    if not yearly_exp:
        st.warning("No data to display yet.")
    else:
        df=pd.DataFrame(yearly_exp)
        df.columns=["Month","Expense"]
        df["Expense"] = df["Expense"].astype(float)
        st.bar_chart(df,x="Month",y="Expense")


avg=average_daily_expense(user_id)
if not avg:
    st.warning("No data to display yet.")
else:
    df=pd.DataFrame(avg)
    df.columns=["Month","Expense"]
    df["Expense"] = df["Expense"].astype(float)
    st.bar_chart(df,x="Month",y="Expense")

data=monthly_savings(user_id)
if not data:
    st.warning("No data to display yet.")

else:
    df=pd.DataFrame(data)
    df.columns=["Expense","Months"]
    # df["Expense"] = df["Expense"].astype(float)
    st.line_chart(df,x="Months",y="Expense")