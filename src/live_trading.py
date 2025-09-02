import ccxt
import os
from dotenv import load_dotenv
from src.data_feed import fetch_ohlcv
from src.feature_engineering import add_indicators
from src.core_trend import generate_signal
from src.risk_management import apply_risk
from src.config import CONFIG

load_dotenv()

def live_trade():
    exchange = ccxt.binance({
        "apiKey": os.getenv("API_KEY"),
        "secret": os.getenv("API_SECRET"),
    })

    df = fetch_ohlcv(limit=200)
    df = add_indicators(df)

    signal = generate_signal(df)
    price = df["close"].iloc[-1]
    balance = CONFIG["trading"]["starting_balance"]

    trade = apply_risk(signal, balance, price)

    if trade["signal"] == "buy":
        print(f"Executing BUY order for {trade['size']:.4f} BTC")
        # exchange.create_market_buy_order(CONFIG["trading"]["pair"], trade["size"])
    elif trade["signal"] == "sell":
        print("Executing SELL order (placeholder)")
        # exchange.create_market_sell_order(CONFIG["trading"]["pair"], trade["size"])
    else:
        print("No trade executed")

if __name__ == "__main__":
    live_trade()
