import streamlit as st
from forms import *


def make_entry_tab():
    col1, col2, col3, col4 = st.columns(4)
    balance = st.session_state.expense_data["Amount"].sum()
    expense = st.session_state.expense_data[st.session_state.expense_data["Amount"] < 0]["Amount"].sum()
    income = st.session_state.expense_data[st.session_state.expense_data["Amount"] > 0]["Amount"].sum()
    borrow = st.session_state.borrow_data["Amount"].sum()

    col1.metric("Balance", value=f"{balance+borrow:,}")
    col2.metric("Expense", value=f"{-expense:,}")
    col3.metric("Income", value=f"{income:,}")
    col4.metric("Borrow", value=f"{borrow:,}")

    if 'show_expense_form' not in st.session_state:
        st.session_state.show_expense_form = False
        st.session_state.show_borrow_form = False
        st.session_state.show_income_form = False
        st.session_state.show_transfer_form = False

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Expense"):
            st.session_state.show_expense_form = True
    with col2:
        if st.button("Income"):
            st.session_state.show_income_form = True
    with col3:
        if st.button("Borrow"):
            st.session_state.show_borrow_form = True
    with col4:
        if st.button("Transfer"):
            st.session_state.show_transfer_form = True

    if st.session_state.show_expense_form:
        expense_form()

    if st.session_state.show_income_form:
        income_form()

    if st.session_state.show_borrow_form:
        borrow_form()

    if st.session_state.show_transfer_form:
        transfer_form()

    # Show only the 10 most recent records
    combined_data = pd.concat([
        st.session_state.expense_data.assign(Type="Expense"),
        st.session_state.borrow_data.assign(Type="Borrow"),
        st.session_state.transfer_data.assign(Type="Transfer")
    ], ignore_index=True)
    recent_data = combined_data.sort_values(by="Date", ascending=False).head(10)

    # Month filter
    months = combined_data["Date"].apply(lambda x: pd.to_datetime(x).strftime("%B %Y")).unique()
    selected_month = st.selectbox("Filter by Month", options=["All"] + sorted(months, reverse=True), key="month_filter")

    if selected_month != "All":
        filtered_data = combined_data[combined_data["Date"].apply(lambda x: pd.to_datetime(x).strftime("%B %Y")) == selected_month]
        display_data(filtered_data)
    else:
        display_data(recent_data)
