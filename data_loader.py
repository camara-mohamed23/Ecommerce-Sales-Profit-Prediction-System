import pandas as pd


def load_data(path):
    df = pd.read_csv(path)
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    return df