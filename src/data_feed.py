import ccxt
import pandas as pd
from src.config import CONFIG

def fetch_ohlcv(exchange_name="binance", pair=None, timeframe=None, limit=500):
    pair = pair or CONFIG["trading"]["pair"]
    timeframe = timeframe or CONFIG["trading"]["timeframe"]

    exchange = getattr(ccxt, exchange_name)()
    ohlcv = exchange.fetch_ohlcv(pair, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df
