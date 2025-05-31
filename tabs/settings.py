import streamlit as st
from utils import save_data


def make_settings_tab():
    st.subheader("Settings")
    st.write("Configure your preferences here.")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Accounts")
        edited_accounts = st.data_editor(
            st.session_state.accounts,
            num_rows="dynamic",
            use_container_width=True,
            key="accounts_editor"
        )
        if st.button("Save Accounts Changes"):
            st.session_state.accounts = edited_accounts
            save_data()
            st.success("Accounts updated.")
            st.rerun()
    with col2:
        st.write("Categories")
        edited_categories = st.data_editor(
            st.session_state.categories,
            num_rows="dynamic",
            use_container_width=True,
            key="categories_editor"
        )
        if st.button("Save Categories Changes"):
            st.session_state.categories = edited_categories
            save_data()
            st.success("Categories updated.")
            st.rerun()
