import pandas as pd

def get_trend_data():
    df = pd.read_csv("data/predictions.csv")

    df = df[df["prediction"] == 1]

    trend = (
        df.groupby("timestamp")
        .size()
        .reset_index(name="ade_count")
    )

    return trend.to_dict(orient="records")
