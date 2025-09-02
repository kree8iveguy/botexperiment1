from src.data_feed import fetch_ohlcv
from src.feature_engineering import add_features
from src.core_trend import trend_signal

def paper_trade():
    df = fetch_ohlcv(limit=500)
    df = add_features(df)
    signal = trend_signal(df)
    print(f"Paper trade signal: {signal}")

if __name__ == "__main__":
    paper_trade()
