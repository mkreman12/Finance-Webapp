import streamlit as st
import streamlit_authenticator as stauth
import os
import pandas as pd

st.set_page_config(layout="wide")

if not os.path.exists("data/expense_data.csv"):
    st.session_state.expense_data = pd.DataFrame(columns=["Item", "Date", "Account", "Category", "Amount"])
    st.session_state.borrow_data = pd.DataFrame(columns=["Name", "Date", "Account", "Amount"])
    st.session_state.transfer_data = pd.DataFrame(columns=["Date", "From Account", "To Account", "Amount"])
    st.session_state.accounts = pd.DataFrame(columns=["Accounts"])
    st.session_state.categories = pd.DataFrame(columns=["Categories"])
else:
    st.session_state.expense_data = pd.read_csv("data/expense_data.csv")
    st.session_state.borrow_data = pd.read_csv("data/borrow_data.csv")
    st.session_state.transfer_data = pd.read_csv("data/transfer_data.csv")
    st.session_state.accounts = pd.read_csv("data/accounts.csv")
    st.session_state.categories = pd.read_csv("data/categories.csv")

from utils import *
from forms import *
from tabs import *


st.header("Financial Tracker")
st.subheader("Track your expenses, income, and borrowings")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "Entry",
        "Accounts",
        "Borrowings",
        "Analysis",
        "Settings"
    ]
)

with tab1:
    make_entry_tab()

with tab2:
    make_accounts_tab()

with tab3:
    make_borrow_tab()

with tab4:
    make_analysis_tab()
    
with tab5:
    make_settings_tab()
