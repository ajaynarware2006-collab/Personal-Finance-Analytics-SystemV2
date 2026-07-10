from backend.income_operation import get_income
from backend.analytics import current_month_expense,top_category,highest_expense,lowest_expense,total_savings,budget_remaining,monthly_savings,monthly_expense,yearly_expense,average_daily_expense,category_summary
import streamlit as st
import pandas as pd
import plotly.express as px
from Frontend.pages.settings import settings
from Frontend.pages.helper import page_config,hide_sidebar
import time

# ---------------- PAGE CONFIG ---------------- #
page_config("Dashboard","💰")

hide_sidebar()

# -------------------- USER --------------------
user_id=st.session_state.get("user_id")
if user_id is None:
    st.error("Please Login First")
    time.sleep(2)
    st.switch_page("app.py")

# -------------------- SETTING OPTION --------------------
settings()

st.markdown("<h1 style='background: linear-gradient(to right, #08203E, #557C93); -webkit-background-clip: text; background-clip: text; color: transparent;text-align:center;padding-top:-20px;padding-bottom:40px;'>PERSONAL FINANCE DASHBOARD</h1>",unsafe_allow_html=True)


# -------------------- FIRST COLUMN --------------------
col1,col2,col3,col4=st.columns([1,1,1,1],gap="large")

with col1:
    st.metric(label="💰 Income",value=f"₹{get_income(user_id)}")

with col2:

    st.metric(label="🏆 Top Category",value=f"₹{top_category(user_id)}")

with col3:
    st.metric(label="📈 Highest Expense",value=f"₹{highest_expense(user_id)}")


with col4:
    st.metric(label="📉 Lowest Expense",value=f"₹{lowest_expense(user_id)}")



st.divider()

# -------------------- SECOND COLUMN --------------------
st.markdown("<BR><BR><BR><BR><BR>",unsafe_allow_html=True)
col5,col6=st.columns([1,3])

with col5:
    st.metric("💵TOTAL SAVING YOU HAVE",value=f"₹{total_savings(user_id)}")
    st.markdown("<BR><BR><BR>",unsafe_allow_html=True)
    budget=budget_remaining(user_id)

    if budget==None:
        st.metric("🎯BUDGET REMAINING",value=None)

    elif budget < 0:
        error="You run out of budget"
        st.metric("🎯BUDGET REMAINING",value=f"₹{error}")
        st.error(f"₹{budget}")


    else:
        st.metric("🎯BUDGET REMAINING",value=f"₹{budget}")

with col6:
    data=category_summary(user_id)
    df=pd.DataFrame(data)
    if not data:
        st.warning("No data to display yet")
        
    else:
        fig=px.pie(df,names=0,values=1)
        st.subheader("Category wise expense")
        st.plotly_chart(fig)


# -------------------- THIRD COLUMN --------------------
col7,col8=st.columns(2)

with col7:
    monthly_exp=monthly_expense(user_id)
    if not monthly_exp:
        st.warning("No data to display yet.")
    else:
        df=pd.DataFrame(monthly_exp)
        df.columns=["Month","Expense (₹)"]
        df["Expense (₹)"] = df["Expense (₹)"].astype(float)
        st.subheader("Monthly Expense")
        st.line_chart(df,x="Month",y="Expense (₹)")


with col8:
    yearly_exp=yearly_expense(user_id)
    if not yearly_exp:
        st.warning("No data to display yet.")
    else:
        df=pd.DataFrame(yearly_exp)
        df.columns=["Year","Expense (₹)"]
        df["Expense (₹)"] = df["Expense (₹)"].astype(float)
        st.subheader("Yearly Expense")
        st.bar_chart(df,x="Year",y="Expense (₹)")

# -------------------- SECOND LAST GRAPH --------------------

avg=average_daily_expense(user_id)
if not avg:
    st.warning("No data to display yet.")
else:
    df=pd.DataFrame(avg)
    df.columns=["Month","Expense (₹)"]
    df["Expense (₹)"] = df["Expense (₹)"].astype(float)
    st.subheader("Average daily expesne")
    st.bar_chart(df,x="Month",y="Expense (₹)")

# -------------------- LAST GRAPH --------------------
data=monthly_savings(user_id)
if not data:
    st.warning("No data to display yet.")

else:
    df=pd.DataFrame(data)
    df.columns=["Expense (₹)","Months"]
    df["Expense (₹)"] = df["Expense (₹)"].astype(float)
    st.subheader("Monthly Savings")
    st.line_chart(df,x="Months",y="Expense (₹)")