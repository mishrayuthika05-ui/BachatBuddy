import pickle

model = pickle.load(open("models/model.pkl", "rb"))

def predict_category(text):
    category = model.predict([text])
    return category[0]