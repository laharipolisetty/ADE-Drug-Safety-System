import pandas as pd
import re
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.utils import shuffle

# ------------------------------------
# LOAD DRUG REVIEW DATASET
# ------------------------------------
df = pd.read_csv(
    "data/drug_reviews/drugsComTrain_raw.csv",
    low_memory=False
)

# ------------------------------------
# KEEP REQUIRED COLUMNS
# ------------------------------------
df = df[["drugName", "condition", "review", "rating"]]
df.dropna(inplace=True)

# ------------------------------------
# CREATE LABELS
# rating <=4  → ADE
# rating >=7  → SAFE
# ------------------------------------
def create_label(r):
    if r <= 4:
        return 1
    elif r >= 7:
        return 0
    else:
        return None

df["label"] = df["rating"].apply(create_label)
df.dropna(inplace=True)

# ------------------------------------
# TEXT MERGING
# ------------------------------------
df["text"] = (
    df["drugName"].astype(str) + " " +
    df["condition"].astype(str) + " " +
    df["review"].astype(str)
)

# ------------------------------------
# CLEAN TEXT
# ------------------------------------
def clean(text):
    text = text.lower()
    text = re.sub(r"[^a-z ]", "", text)
    return text

df["text"] = df["text"].apply(clean)

df = shuffle(df)

# ------------------------------------
# TF-IDF VECTOR
# ------------------------------------
vectorizer = TfidfVectorizer(
    max_features=8000,
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(df["text"])
y = df["label"]

# ------------------------------------
# TRAIN MODEL
# ------------------------------------
model = SGDClassifier(
    loss="log_loss",
    max_iter=50,
    alpha=1e-5,
    class_weight="balanced"
)

model.fit(X, y)

# ------------------------------------
# SAVE MODEL
# ------------------------------------
joblib.dump(model, "models/ade_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("✅ Drug review ML model trained successfully")
