import ccxt
import pandas as pd
from src.config import load_config, API_KEY, API_SECRET

config = load_config()

def get_exchange():
    return ccxt.binance({
        "apiKey": API_KEY,
        "secret": API_SECRET
    })

def fetch_ohlcv(symbol=None, timeframe=None, limit=500):
    exchange = get_exchange()
    symbol = symbol or config["trading"]["symbol"]
    timeframe = timeframe or config["trading"]["timeframe"]
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=["timestamp","open","high","low","close","volume"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df
