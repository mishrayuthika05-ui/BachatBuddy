import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

data = pd.read_csv("data/training_data.csv")

X = data["description"]
y = data["category"]

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

model.fit(X, y)

pickle.dump(model, open("models/model.pkl", "wb"))

print("Model trained successfully")