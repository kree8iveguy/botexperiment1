import pandas as pd

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df["ma_fast"] = df["close"].rolling(window=10).mean()
    df["ma_slow"] = df["close"].rolling(window=30).mean()
    df["rsi"] = compute_rsi(df["close"])
    return df

def compute_rsi(series: pd.Series, period=14) -> pd.Series:
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))
