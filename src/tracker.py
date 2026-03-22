import pandas as pd
import os
from src.predictor import predict_category

FILE = "data/transactions.csv"

# ensure folder exists
os.makedirs(os.path.dirname(FILE), exist_ok=True)

def add_transaction(amount, description):
    category = predict_category(description)

    new_data = {
        "amount": amount,
        "description": description,
        "category": category
    }

    try:
        df = pd.read_csv(FILE)
    except:
        df = pd.DataFrame(columns=["amount", "description", "category"])

    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv(FILE, index=False)

def show_transactions():
    try:
        df = pd.read_csv(FILE)
        import streamlit as st
        st.write(df)
    except:
        import streamlit as st
        st.write("No data found")
