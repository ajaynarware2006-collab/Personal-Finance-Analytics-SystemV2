import psycopg as pg
import streamlit as st

def connecting():
    connection=pg.connect(
                host="localhost",
                dbname="Expense_Tracker",
                user="postgres",
                password=st.secrets["password"],
                port=5432)

    return connection