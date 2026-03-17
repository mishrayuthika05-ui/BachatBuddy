import pandas as pd
import matplotlib.pyplot as plt

FILE = "data/user_transactions.csv"

def spending_by_category():

    df = pd.read_csv(FILE)

    result = df.groupby("category")["amount"].sum()

    print("\nSpending by Category\n")
    print(result)

    result.plot(kind="bar")

    plt.title("Spending by Category")
    plt.ylabel("Amount")

    plt.show()


def monthly_spending():

    df = pd.read_csv(FILE)

    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.month

    result = df.groupby("month")["amount"].sum()

    print("\nMonthly Spending\n")
    print(result)

    result.plot(kind="line", marker="o")

    plt.title("Monthly Spending Trend")
    plt.ylabel("Amount")

    plt.show()