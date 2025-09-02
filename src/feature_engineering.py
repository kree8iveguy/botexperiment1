import pandas as pd

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df["return"] = df["close"].pct_change()
    df["ma_fast"] = df["close"].rolling(10).mean()
    df["ma_slow"] = df["close"].rolling(50).mean()
    df["volatility"] = df["return"].rolling(20).std()
    df.dropna(inplace=True)
    return df
