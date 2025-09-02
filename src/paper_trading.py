import pandas as pd
from src.data_feed import fetch_ohlcv
from src.feature_engineering import add_indicators
from src.core_trend import generate_signal
from src.risk_management import apply_risk
from src.config import CONFIG

def paper_trade():
    df = fetch_ohlcv(limit=200)
    df = add_indicators(df)

    balance = CONFIG["trading"]["starting_balance"]
    price = df["close"].iloc[-1]
    signal = generate_signal(df)

    trade = apply_risk(signal, balance, price)
    print("Paper trade:", trade)

if __name__ == "__main__":
    paper_trade()
