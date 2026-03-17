import streamlit as st
import pickle
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

model = pickle.load(open("models/model.pkl", "rb"))

st.title("💰 ML Finance Tracker")

amount = st.number_input("Enter Amount")
description = st.text_input("Enter Description")

if st.button("Add Transaction"):

    category = model.predict([description])[0]

    data = {
        "date":[datetime.now().date()],
        "amount":[amount],
        "description":[description],
        "category":[category]
    }

    df = pd.DataFrame(data)

    try:
        old = pd.read_csv("data/user_transactions.csv")
        df = pd.concat([old, df])
    except:
        pass

    df.to_csv("data/user_transactions.csv", index=False)

    st.success("Transaction Added")
    st.write("Predicted Category:", category)

if st.button("Show Transactions"):

    df = pd.read_csv("data/user_transactions.csv")
    st.dataframe(df)
    import matplotlib.pyplot as plt

if st.button("Show Category Analysis"):

    df = pd.read_csv("data/user_transactions.csv")

    if df.empty:
        st.write("No data available")
    else:
        fig, ax = plt.subplots()
        df.groupby("category")["amount"].sum().plot(kind="bar", ax=ax)

        ax.set_title("Spending by Category")
        ax.set_xlabel("Category")
        ax.set_ylabel("Amount")

        st.pyplot(fig)