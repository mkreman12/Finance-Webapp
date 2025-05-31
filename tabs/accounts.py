import streamlit as st
from utils import *


def make_accounts_tab():
    expense_data = st.session_state.expense_data
    borrow_data = st.session_state.borrow_data
    transfer_data = st.session_state.transfer_data
    
    st.subheader("Accounts")
    accounts = sorted(
        set(expense_data["Account"])
        | set(borrow_data["Account"])
        | set(transfer_data["From Account"])
        | set(transfer_data["To Account"])
    )
    cols = st.columns(max(1, len(accounts)))
    for col, account in zip(cols, accounts):
        account_amount = expense_data[expense_data["Account"] == account]['Amount'].sum() + \
        borrow_data[borrow_data["Account"] == account]['Amount'].sum() - \
        transfer_data[transfer_data["From Account"] == account]['Amount'].sum() + \
        transfer_data[transfer_data["To Account"] == account]['Amount'].sum()

        combined_data = pd.concat([
            expense_data.assign(Type="Expense")[expense_data.assign(Type="Expense")['Account'] == account],
            borrow_data.assign(Type="Borrow")[borrow_data.assign(Type="Borrow")['Account'] == account],
            transfer_data.assign(Type="Transfer")[transfer_data.assign(Type="Transfer")['From Account'] == account],
            transfer_data.assign(Type="Transfer")[transfer_data.assign(Type="Transfer")['To Account'] == account]
        ], ignore_index=True)
        
        with col:
            st.metric(account, account_amount)
            
            # Month filter
            months = combined_data["Date"].apply(lambda x: pd.to_datetime(x).strftime("%B %Y")).unique()
            selected_month = st.selectbox("Filter by Month", options=["All"] + sorted(months, reverse=True), key=f"month_filter_{account}")

            if selected_month != "All":
                filtered_data = combined_data[combined_data["Date"].apply(lambda x: pd.to_datetime(x).strftime("%B %Y")) == selected_month]
                display_data(filtered_data)
            else:
                display_data(combined_data)
            