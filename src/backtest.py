from src.data_feed import fetch_ohlcv
from src.feature_engineering import add_features
from src.core_trend import trend_signal
from src.risk_management import position_size
from src.config import load_config

def backtest():
    config = load_config()
    df = fetch_ohlcv(limit=1000)
    df = add_features(df)
    balance = config["trading"]["initial_balance"]

    for i in range(51, len(df)):
        sub_df = df.iloc[:i]
        signal = trend_signal(sub_df)
        if signal in ["buy","sell"]:
            size = position_size(balance,
                                 config["trading"]["risk_per_trade"],
                                 config["trading"]["stop_loss_pct"])
            # Dummy execution
            balance += size * sub_df["return"].iloc[-1]

    print(f"Final balance: {balance:.2f}")

if __name__ == "__main__":
    backtest()
