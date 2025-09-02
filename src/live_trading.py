from src.data_feed import fetch_ohlcv
from src.feature_engineering import add_features
from src.core_trend import trend_signal
from src.config import load_config

def live_trade():
    config = load_config()
    df = fetch_ohlcv(limit=200)
    df = add_features(df)
    signal = trend_signal(df)
    print(f"Live trade signal: {signal}")
    # Here you'd place a real order with ccxt

if __name__ == "__main__":
    live_trade()
