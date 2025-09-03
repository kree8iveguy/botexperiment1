from src.backtest import backtest
from src.paper_trading import paper_trade
from src.live_trading import live_trade

if __name__ == "__main__":
    print("Select mode: backtest / paper / live")
    mode = input("Enter mode: ").strip().lower()

    if mode == "backtest":
        backtest()
    elif mode == "paper":
        paper_trade()
    elif mode == "live":
        live_trade()
    else:
        print("Invalid mode")
