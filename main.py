from src.tracker import add_transaction, show_transactions
from src.analysis import spending_by_category, monthly_spending

while True:

    print("\n===== ML Finance Tracker =====")

    print("1 Add Transaction")
    print("2 View Transactions")
    print("3 Category Analysis")
    print("4 Monthly Spending")
    print("5 Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        amount = float(input("Enter amount: "))
        description = input("Enter description: ")

        add_transaction(amount, description)

    elif choice == "2":

        show_transactions()

    elif choice == "3":

        spending_by_category()

    elif choice == "4":

        monthly_spending()

    elif choice == "5":

        break

    else:

        print("Invalid option")