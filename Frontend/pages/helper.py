import streamlit as st

def button():
    st.markdown("""
    <style>
    div.stButton > button {
        width: 180px;
        height: 42px;
        border-radius: 10px;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

def page_config(page_title,page_icon,layout="wide"):
    st.set_page_config(
    page_title=page_title,
    page_icon=page_icon,
    layout=layout,
    initial_sidebar_state="collapsed"
    )

def hide_sidebar():
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
    
def card_css():
    st.markdown("""
            <style>

            /* Hide Sidebar */
            [data-testid="stSidebar"]{
                display:none;
            }

            [data-testid="stSidebarCollapsedControl"]{
                display:none;
            }

            /* Card */
            .card{
                background-color:#1e1e1e;
                padding:35px;
                border-radius:18px;
                border:1px solid #2f2f2f;
                box-shadow:0px 0px 15px rgba(255,255,255,0.05);
            }

            /* Button */

            .stButton>button{
                width:100%;
                height:50px;
                border-radius:10px;
                font-size:18px;
                font-weight:bold;
            }

            /* Number Input */

            div[data-baseweb="input"]{
                border-radius:10px;
            }

            </style>
            """, unsafe_allow_html=True)
    
def text_gredient(text):
    st.markdown(f"<h1 style='background: linear-gradient(to right, #08203E, #557C93); -webkit-background-clip: text; background-clip: text; color: transparent;text-align:center;'>{text}</h1>",unsafe_allow_html=True)