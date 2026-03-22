import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
from src.tracker import add_transaction, show_transactions
from src.analysis import spending_by_category, monthly_spending

st.title("💰 ML Finance Tracker")

menu = st.sidebar.selectbox(
    "Choose option",
    ["Add Transaction", "View Transactions", "Category Analysis", "Monthly Spending"]
)

if menu == "Add Transaction":
    amount = st.number_input("Enter amount")
    description = st.text_input("Enter description")

    if st.button("Add"):
        add_transaction(amount, description)
        st.success("Added!")

elif menu == "View Transactions":
    show_transactions()

elif menu == "Category Analysis":
    spending_by_category()

elif menu == "Monthly Spending":
    monthly_spending()
