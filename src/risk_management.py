from src.config import CONFIG

def position_size(balance: float, price: float) -> float:
    risk = CONFIG["trading"]["risk_per_trade"]
    stop_loss_pct = CONFIG["trading"]["stop_loss_pct"]
    capital_at_risk = balance * risk
    return capital_at_risk / (price * stop_loss_pct)

def apply_risk(signal: str, balance: float, price: float) -> dict:
    size = position_size(balance, price)
    stop_loss = price * (1 - CONFIG["trading"]["stop_loss_pct"])
    take_profit = price * (1 + CONFIG["trading"]["take_profit_pct"])
    return {
        "signal": signal,
        "size": size,
        "stop_loss": stop_loss,
        "take_profit": take_profit,
    }
