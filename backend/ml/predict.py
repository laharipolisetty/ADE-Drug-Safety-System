import joblib
import re

model = joblib.load("models/ade_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def clean(text):
    text = text.lower()
    text = re.sub(r"[^a-z ]", "", text)
    return text

def predict_ade(text):
    text = clean(text)
    vec = vectorizer.transform([text])

    probability = model.predict_proba(vec)[0][1]

    prediction = 1 if probability >= 0.6 else 0

    return {
        "prediction": prediction,
        "confidence": round(probability * 100, 2)
    }
