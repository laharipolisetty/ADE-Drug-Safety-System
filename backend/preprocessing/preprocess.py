import pandas as pd

def load_faers(path, usecols=None, nrows=200000):
    return pd.read_csv(
        path,
        sep="$",
        encoding="latin1",
        engine="python",
        on_bad_lines="skip",
        usecols=usecols,
        nrows=nrows
    )

# ---- load limited rows ----
demo = load_faers(
    "data/raw/DEMO.csv",
    usecols=["caseid", "sex", "age"]
)

drug = load_faers(
    "data/raw/DRUG.csv",
    usecols=["caseid", "drugname"]
)

reac = load_faers(
    "data/raw/REAC.csv",
    usecols=["caseid", "pt"]
)

outc = load_faers(
    "data/raw/OUTC.csv",
    usecols=["caseid", "outc_cod"]
)

# ---- merge ----
df = demo.merge(drug, on="caseid", how="inner")
df = df.merge(reac, on="caseid", how="inner")
df = df.merge(outc, on="caseid", how="left")

df.columns = [
    "case_id",
    "sex",
    "age",
    "drug",
    "reaction",
    "outcome"
]

df.dropna(inplace=True)

df.to_csv("data/processed/merged_data.csv", index=False)

print("✅ FAERS SAMPLE preprocessing completed successfully")
