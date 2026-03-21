import streamlit as st
from src.tracker import add_transaction, show_transactions
from src.analysis import spending_by_category, monthly_spending

st.title("💰 ML Finance Tracker")

menu = st.selectbox("Choose option", [
    "Add Transaction",
    "View Transactions",
    "Category Analysis",
    "Monthly Spending"
])

if menu == "Add Transaction":
    amount = st.number_input("Enter amount")
    description = st.text_input("Enter description")

    if st.button("Add"):
        add_transaction(amount, description)
        st.success("Transaction Added!")

elif menu == "View Transactions":
    st.write("Transactions:")
    show_transactions()

elif menu == "Category Analysis":
    st.write("Category Analysis:")
    spending_by_category()

elif menu == "Monthly Spending":
    st.write("Monthly Spending:")
    monthly_spending()
