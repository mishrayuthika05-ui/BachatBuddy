import pandas as pd
import streamlit as st

FILE = "data/transactions.csv"

def spending_by_category():
    try:
        df = pd.read_csv(FILE)
        st.write(df.groupby("category")["amount"].sum())
    except:
        st.write("No data")

def monthly_spending():
    try:
        df = pd.read_csv(FILE)
        st.write(df)
    except:
        st.write("No data")
