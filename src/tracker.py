import pandas as pd
from datetime import datetime
from src.predictor import predict_category

FILE = "data/user_transactions.csv"

def add_transaction(amount, description):

    category = predict_category(description)

    transaction = {
        "date": datetime.today().strftime("%Y-%m-%d"),
        "amount": amount,
        "description": description,
        "category": category
    }

    df_new = pd.DataFrame([transaction])

    try:
        df_old = pd.read_csv(FILE)
        df = pd.concat([df_old, df_new])
    except:
        df = df_new

    df.to_csv(FILE, index=False)

    print("\nTransaction Added")
    print("Predicted Category:", category)


def show_transactions():

    try:
        df = pd.read_csv(FILE)
        print("\nTransactions:\n")
        print(df)
    except:
        print("No transactions found.")