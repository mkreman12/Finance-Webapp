import streamlit as st
from utils import *


def make_borrow_tab():
    data = st.session_state.borrow_data
    
    st.subheader("Borrowings")
    people = data["Name"].unique()
    cols = st.columns(max(1, len(people)))
    for col, person in zip(cols, people):
        person_data = data[data["Name"] == person]
        total_borrowed = person_data["Amount"].sum()
        
        with col:
            st.metric(person, f"{total_borrowed} ₹")
            
            # Month filter
            months = person_data["Date"].apply(lambda x: pd.to_datetime(x).strftime("%B %Y")).unique()
            selected_month = st.selectbox("Filter by Month", options=["All"] + sorted(months, reverse=True), key=f"month_filter_{person}")
            
            if selected_month != "All":
                filtered_data = person_data[person_data["Date"].apply(lambda x: pd.to_datetime(x).strftime("%B %Y")) == selected_month]
                display_data(filtered_data)
            else:
                display_data(person_data)
    