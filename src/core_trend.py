import pandas as pd

def generate_signal(df: pd.DataFrame) -> str:
    if df["ma_fast"].iloc[-1] > df["ma_slow"].iloc[-1]:
        return "buy"
    elif df["ma_fast"].iloc[-1] < df["ma_slow"].iloc[-1]:
        return "sell"
    return "hold"
