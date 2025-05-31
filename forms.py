import streamlit as st
from utils import *
from datetime import datetime

def expense_form():
    accounts = st.session_state.accounts['Accounts'].values
    categories = st.session_state.categories['Categories'].values
    with st.form("expense_form", clear_on_submit=True):
        date_part = st.date_input("📅 Date", key="entry_date", value=datetime.now())
        time_part = st.time_input("⏰ Time", key="entry_time", value=datetime.now().time())
        date = datetime.combine(date_part, time_part)

        item_name = st.text_input("🛒 Item Name", key="entry_item_name", value="")

        account = st.selectbox("🏦 Account", accounts, key="entry_account", index=1)

        category = st.selectbox("📂 Category", categories, key="entry_category", index=0)

        amount = st.number_input("💸 Amount", min_value=0, key="entry_amount")

        col1, col2 = st.columns([1, 4.4], gap="small", vertical_alignment="center")

        save = col1.form_submit_button("💾 Save Record")
        cancel = col2.form_submit_button("❌ Cancel")
        if save:
            new_row = {"Item": item_name, "Date": date, "Account": account, "Category": category, "Amount": -round(float(amount), 2)}
            st.session_state.expense_data = pd.concat([
                st.session_state.expense_data, pd.DataFrame([new_row])
            ], ignore_index=True)
            save_data()
            st.success("✅ Record added successfully!")
            st.session_state.show_expense_form = False
            st.rerun()
        if cancel:
            st.session_state.show_expense_form = False
            st.rerun()

def income_form():
    accounts = st.session_state.accounts['Accounts'].values
    with st.form("income_form", clear_on_submit=True):
        date_part = st.date_input("📅 Date", key="income_date", value=datetime.now())
        time_part = st.time_input("⏰ Time", key="income_time", value=datetime.now().time())
        date = datetime.combine(date_part, time_part)

        item_name = st.text_input("💼 Item Name", key="income_item_name", value="")

        account = st.selectbox("🏦 Account", accounts, key="income_category", index=0)

        amount = st.number_input("💰 Amount", min_value=0, key="income_amount")

        col1, col2 = st.columns([1, 4.4], gap="small", vertical_alignment="center")

        save = col1.form_submit_button("💾 Save Income")
        cancel = col2.form_submit_button("❌ Cancel")
        if save:
            new_row = {"Item": item_name, "Date": date, "Account": account, "Amount": round(float(amount), 2)}
            st.session_state.expense_data = pd.concat([
                st.session_state.expense_data, pd.DataFrame([new_row])
            ], ignore_index=True)
            save_data()
            st.success("✅ Record added successfully!")
            st.session_state.show_income_form = False
            st.rerun()
        if cancel:
            st.session_state.show_income_form = False
            st.rerun()

def borrow_form():
    accounts = st.session_state.accounts['Accounts'].values
    with st.form("borrow_form", clear_on_submit=True):
        date_part = st.date_input("📅 Date", key="borrow_date", value=datetime.now())
        time_part = st.time_input("⏰ Time", key="borrow_time", value=datetime.now().time())
        date = datetime.combine(date_part, time_part)

        name = st.text_input("👤 Name", key="borrow_name")

        account = st.selectbox("🏦 Account", accounts, key="borrow_account", index=0)

        amount = st.number_input("💵 Amount", key="borrow_amount")

        col1, col2 = st.columns([1, 4.4], gap="small", vertical_alignment="center")

        save = col1.form_submit_button("💾 Save Borrow")
        cancel = col2.form_submit_button("❌ Cancel")
        if save:
            new_row = {"Date": date, "Name":name, "Account": account, "Amount": float(amount)}
            st.session_state.borrow_data = pd.concat([
                st.session_state.borrow_data, pd.DataFrame([new_row])
            ], ignore_index=True)
            save_data()
            st.success("✅ Record added successfully!")
            st.session_state.show_borrow_form = False
            st.rerun()
        if cancel:
            st.session_state.show_borrow_form = False
            st.rerun()

def transfer_form():
    accounts = st.session_state.accounts['Accounts'].values
    with st.form("transfer_form", clear_on_submit=True):
        date_part = st.date_input("📅 Date", key="transfer_date", value=datetime.now())
        time_part = st.time_input("⏰ Time", key="transfer_time", value=datetime.now().time())
        date = datetime.combine(date_part, time_part)

        from_account = st.selectbox("⬅️ From Account", accounts, key="transfer_from_account", index=0)
        to_account = st.selectbox("➡️ To Account", accounts, key="transfer_to_account", index=0)

        amount = st.number_input("🔄 Amount", min_value=0, key="transfer_amount")

        col1, col2 = st.columns([1, 4.4], gap="small", vertical_alignment="center")

        save = col1.form_submit_button("💾 Save Transfer")
        cancel = col2.form_submit_button("❌ Cancel")
        if save:
            new_row = {"Date": date, "From Account": from_account, "To Account": to_account, "Amount": float(amount)}
            st.session_state.transfer_data = pd.concat([
                st.session_state.transfer_data, pd.DataFrame([new_row])
            ], ignore_index=True)
            save_data()
            st.success("✅ Record added successfully!")
            st.session_state.show_transfer_form = False
            st.rerun()
        if cancel:
            st.session_state.show_transfer_form = False
            st.rerun()
