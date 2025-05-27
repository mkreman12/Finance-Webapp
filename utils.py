import pandas as pd
import streamlit as st


def save_data():
    """
    Save the DataFrame to a CSV file.
    """
    st.session_state.expense_data.to_csv("data/expense_data.csv", index=False)
    st.session_state.borrow_data.to_csv("data/borrow_data.csv", index=False)
    st.session_state.transfer_data.to_csv("data/transfer_data.csv", index=False)
    st.session_state.accounts.to_csv("data/accounts.csv", index=False)
    st.session_state.categories.to_csv("data/categories.csv", index=False)


def display_data(df):
    """
    Display the DataFrame in a Streamlit app.
    """
    prev_date = None
    for _, row in df.iterrows():
        current_date = pd.to_datetime(row["Date"]).date()
        if current_date != prev_date:
            st.markdown("---")
            st.write(current_date.strftime("%d/%m/%y"))
        
        if 'From Account' in df.columns and not pd.isna(row['From Account']):
            display_row(row, type='transfer')
        elif 'Name' in df.columns and not pd.isna(row['Name']):
            display_row(row, type='borrow')
        elif row["Amount"] < 0:
            display_row(row, type='expense')
        else:
            display_row(row, type='income')
        
        prev_date = current_date


def display_row(row, type='expense'):
    """
    Display the DataFrame in a Streamlit app.
    """
    match type:
        case 'expense':
            with st.container(border=True):
                col1, col2, col3, col4 = st.columns(4, gap="small", vertical_alignment="center")
                with col1:
                    st.write(f"**{row['Item']}**")
                    st.write(row['Account'])
                with col2:
                    st.write(f"**{row['Category']}**")
                with col3:
                    st.write(f"<span style='color:red; font-size:20px'><b>{row['Amount']} ₹</b></span>", unsafe_allow_html=True)
                with col4:
                    st.write(f"{pd.to_datetime(row['Date']).strftime('%I:%M %p')}")

        case 'income':
            with st.container(border=True):
                col1, col2, col3, col4 = st.columns(4, gap="small", vertical_alignment="center")
                with col1:
                    st.write(f"**{row['Item']}**")
                with col2:
                    st.write(f"**{row['Account']}**")
                with col3:
                    st.write(f"<span style='color:green; font-size:20px'><b>{row['Amount']} ₹</b></span>", unsafe_allow_html=True)
                with col4:
                    st.write(f"{pd.to_datetime(row['Date']).strftime('%I:%M %p')}")

        case 'borrow':
            with st.container(border=True):
                col1, col2, col3, col4 = st.columns(4, gap="small", vertical_alignment="center")
                with col1:
                    st.write(f"**{row['Name']}**")
                    if row['Amount'] < 0:
                        st.write("Borrowed")
                    else:
                        st.write("Lent")
                with col2:
                    st.write(f"**{row['Account']}**")
                with col3:
                    st.write(f"<span style='color:blue; font-size:20px'><b>{row['Amount']} ₹</b></span>", unsafe_allow_html=True)
                with col4:
                    st.write(f"{pd.to_datetime(row['Date']).strftime('%I:%M %p')}")
        case 'transfer':
            with st.container(border=True):
                col1, col2, col3, col4 = st.columns(4, gap="small", vertical_alignment="center")
                with col1:
                    st.write(f"**{row['From Account']}**")
                    st.write("From")
                with col2:
                    st.write(f"**{row['To Account']}**")
                    st.write("To")
                with col3:
                    st.write(f"<span style='color:orange; font-size:20px'><b>{row['Amount']} ₹</b></span>", unsafe_allow_html=True)
                with col4:
                    st.write(f"{pd.to_datetime(row['Date']).strftime('%I:%M %p')}")
