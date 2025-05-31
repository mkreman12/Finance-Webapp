import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def make_analysis_tab():
    st.header("Analysis Tab")

    df = st.session_state.expense_data
    col1, col2 = st.columns(2)
    with col1:
        category_totals = df.groupby('Category')['Amount'].sum().reset_index()

        # Set seaborn style for better aesthetics
        sns.set_theme(style="whitegrid")

        fig, ax = plt.subplots(figsize=(6, 6), facecolor='none')
        wedges, texts, autotexts = ax.pie(
            np.abs(category_totals['Amount']),
            labels=category_totals['Category'],
            autopct='%1.1f%%',
            startangle=90,
            wedgeprops=dict(edgecolor='w', linewidth=1, alpha=0.85)
        )
        # Set background transparent
        fig.patch.set_alpha(0.0)
        ax.set_facecolor('none')
        for text in texts + autotexts:
            text.set_color('white')
            text.set_fontsize(12)
        ax.set_title('Total Amount by Category', fontsize=16, fontweight='bold')
        ax.legend(title='Categories', loc='upper left', bbox_to_anchor=(1, 1))
        ax.axis('equal')

        st.pyplot(fig)

    with col2:
        category_totals = df.groupby('Account')['Amount'].sum().reset_index()

        # Set seaborn style for better aesthetics
        sns.set_theme(style="whitegrid")

        fig, ax = plt.subplots(figsize=(6, 6), facecolor='none')
        wedges, texts, autotexts = ax.pie(
            np.abs(category_totals['Amount']),
            labels=category_totals['Account'],
            autopct='%1.1f%%',
            startangle=90,
            wedgeprops=dict(edgecolor='w', linewidth=1, alpha=0.85)
        )
        # Set background transparent
        fig.patch.set_alpha(0.0)
        ax.set_facecolor('none')
        for text in texts + autotexts:
            text.set_color('white')
            text.set_fontsize(12)
        ax.set_title('Total Amount by Account', fontsize=16, fontweight='bold')
        ax.legend(title='Accounts', loc='upper left', bbox_to_anchor=(1, 1))
        ax.axis('equal')

        st.pyplot(fig)

    st.subheader("Monthly Trends")
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_totals = df.groupby('Month')['Amount'].sum().reset_index()
    monthly_totals['Month'] = monthly_totals['Month'].dt.to_timestamp()
    monthly_totals['Month'] = monthly_totals['Month'].dt.strftime('%Y-%m')
    monthly_totals['Amount'] = monthly_totals['Amount'].abs()
    monthly_totals = monthly_totals.sort_values('Month')
    fig, ax = plt.subplots(figsize=(10, 5), facecolor='none')
    sns.lineplot(data=monthly_totals, x='Month', y='Amount', marker='o', ax=ax)
    ax.set_title('Monthly Expense Trends', fontsize=16, fontweight='bold')
    ax.set_xlabel('Month', fontsize=14)
    ax.set_ylabel('Total Amount (₹)', fontsize=14)
    ax.set_xticklabels(monthly_totals['Month'], rotation=45)
    ax.set_facecolor('none')
    fig.patch.set_alpha(0.0)
    st.pyplot(fig)
    