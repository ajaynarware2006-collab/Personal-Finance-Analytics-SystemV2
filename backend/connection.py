import psycopg as pg
import streamlit as st

def connecting():
    connection=pg.connect(
                host=st.secrets["DB_HOST"],
                dbname=st.secrets["DB_NAME"],
                user=st.secrets["DB_USER"],
                password=st.secrets["DB_PASSWORD"],
                port=st.secrets["DB_PORT"],
                sslmode=st.secrets["DB_SSLMODE"])

    return connection