import streamlit as st
from src.tracker import add_transaction, show_transactions
from src.analysis import spending_by_category, monthly_spending

st.title("💰 ML Finance Tracker")

menu = st.sidebar.selectbox(
    "Choose option",
    ["Add Transaction", "View Transactions", "Category Analysis", "Monthly Spending"]
)

if menu == "Add Transaction":
    st.header("Add Transaction")

    amount = st.number_input("Enter amount")
    description = st.text_input("Enter description")

    if st.button("Add"):
        add_transaction(amount, description)
        st.success("Transaction added!")

elif menu == "View Transactions":
    st.header("All Transactions")
    show_transactions()

elif menu == "Category Analysis":
    st.header("Spending by Category")
    spending_by_category()

elif menu == "Monthly Spending":
    st.header("Monthly Spending")
    monthly_spending()
