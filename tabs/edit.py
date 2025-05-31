import streamlit as st
from utils import save_data
import pandas as pd


def make_edit_tab():
    st.subheader("✏️ Edit")
    st.write("Edit the records")

    record_type = st.selectbox(
        "Select record type to edit",
        ("Expense", "Borrow", "Transfer")
    )

    if record_type == "Expense":
        st.subheader("Expense Records")
        column_config = {
            "Category": st.column_config.SelectboxColumn(
                "Category",
                options=st.session_state.categories.Categories.values,
            ),
            "Account": st.column_config.SelectboxColumn(
                "Account",
                options=st.session_state.accounts.Accounts.values,
            ),
        }

        data = st.session_state.expense_data.sort_values(by='Date', ascending=False).reset_index(drop=True)
        months = data["Date"].apply(lambda x: pd.to_datetime(x).strftime("%B %Y")).unique()
        selected_month = st.selectbox("📅 Filter by Month", options=["All"] + sorted(months, reverse=True), index=1)
        if selected_month != "All":
            filtered_data = data[data["Date"].apply(lambda x: pd.to_datetime(x).strftime("%B %Y")) == selected_month].reset_index(drop=True)
        else:
            filtered_data = data

        st.data_editor(
            filtered_data,
            column_config=column_config,
            num_rows="dynamic"
        )

    elif record_type == "Borrow":
        st.subheader("Borrow Records")
        column_config = {
            "Account": st.column_config.SelectboxColumn(
                "Account",
                options=st.session_state.accounts.Accounts.values,
            ),
        }

        data = st.session_state.borrow_data.sort_values(by='Date', ascending=False).reset_index(drop=True)
        months = data["Date"].apply(lambda x: pd.to_datetime(x).strftime("%B %Y")).unique()
        selected_month = st.selectbox("📅 Filter by Month", options=["All"] + sorted(months, reverse=True), index=1)
        if selected_month != "All":
            filtered_data = data[data["Date"].apply(lambda x: pd.to_datetime(x).strftime("%B %Y")) == selected_month].reset_index(drop=True)
        else:
            filtered_data = data
            
        st.data_editor(
            data,
            column_config=column_config,
            num_rows="dynamic"
        )

    elif record_type == "Transfer":
        st.subheader("Transfer Records")
        column_config = {
            "From Account": st.column_config.SelectboxColumn(
                "From Account",
                options=st.session_state.accounts.Accounts.values,
            ),
            "To Account": st.column_config.SelectboxColumn(
                "To Account",
                options=st.session_state.accounts.Accounts.values,
            ),
        }

        data = st.session_state.transfer_data.sort_values(by='Date', ascending=False).reset_index(drop=True)
        months = data["Date"].apply(lambda x: pd.to_datetime(x).strftime("%B %Y")).unique()
        selected_month = st.selectbox("📅 Filter by Month", options=["All"] + sorted(months, reverse=True), index=1)
        if selected_month != "All":
            filtered_data = data[data["Date"].apply(lambda x: pd.to_datetime(x).strftime("%B %Y")) == selected_month].reset_index(drop=True)
        else:
            filtered_data = data

        st.data_editor(
            data,
            column_config=column_config,
            num_rows="dynamic"
        )
    
    if st.button("💾 Save Changes"):
        save_data()
        st.success("Transfer records saved.")
        st.rerun()
        