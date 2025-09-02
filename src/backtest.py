import pandas as pd
from src.data_feed import fetch_ohlcv
from src.feature_engineering import add_indicators
from src.core_trend import generate_signal
from src.risk_management import apply_risk
from src.config import CONFIG

def backtest():
    df = fetch_ohlcv(limit=500)
    df = add_indicators(df)

    balance = CONFIG["trading"]["starting_balance"]
    position = None

    for i in range(len(df)):
        row = df.iloc[: i + 1]
        if len(row) < 30:
            continue

        signal = generate_signal(row)
        price = row["close"].iloc[-1]

        if signal == "buy" and not position:
            trade = apply_risk("buy", balance, price)
            position = trade
            print(f"BUY at {price:.2f}, size {trade['size']:.4f}")
        elif signal == "sell" and position:
            pnl = (price - position["stop_loss"]) * position["size"]
            balance += pnl
            print(f"SELL at {price:.2f}, balance {balance:.2f}")
            position = None

    print(f"Final balance: {balance:.2f}")

if __name__ == "__main__":
    backtest()
