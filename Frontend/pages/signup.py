import streamlit as st
from backend.connection import connecting

connection,cursor=connecting()

password=st.session_state.get("password")
name=st.session_state.get("name")
income=st.number_input(label="Income",placeholder="Enter Your Monthly Income",value=None)
budget=st.number_input(label="Budget",placeholder="Enter Your Monthly Budget",value=None)

if not income:
    st.error("Income cannot be Empty")
elif not budget:
    st.error("Budget cannot be Empty")
else:

    cursor.execute("INSERT INTO users(name,monthly_income,password,budget) VALUES (%s,%s,%s,%s) RETURNING user_id;",(name,income,password,budget))
    user_id=cursor.fetchone()
    if not user_id:
        st.error("Something went wrong")
    
    else:
        connection.commit()

        st.success(f"Successfully Registered")
        st.session_state["user_id"]=user_id[0]
        st.switch_page("pages/dashboard.py")


