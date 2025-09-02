def position_size(balance, risk_per_trade, stop_loss_pct):
    return balance * risk_per_trade / stop_loss_pct
