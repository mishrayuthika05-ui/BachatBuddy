import streamlit as st
from src.tracker import add_transaction, show_transactions
from src.analysis import spending_by_category, monthly_spending

st.title("💰 ML Finance Tracker")

st.write("===== ML Finance Tracker =====")

choice = st.selectbox("Choose an option", [
    "1 Add Transaction",
    "2 View Transactions",
    "3 Category Analysis",
    "4 Monthly Spending",
    "5 Exit"
])

# Option 1
if choice == "1 Add Transaction":
    amount = st.number_input("Enter amount:")
    description = st.text_input("Enter description:")

    if st.button("Submit"):
        add_transaction(amount, description)
        st.success("Transaction added!")

# Option 2
elif choice == "2 View Transactions":
    st.write("Transactions:")
    show_transactions()

# Option 3
elif choice == "3 Category Analysis":
    st.write("Category Analysis:")
    spending_by_category()

# Option 4
elif choice == "4 Monthly Spending":
    st.write("Monthly Spending:")
    monthly_spending()

# Option 5
elif choice == "5 Exit":
    st.warning("App Closed (Refresh to restart)")
