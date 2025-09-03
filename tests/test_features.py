import pandas as pd
from src.feature_engineering import add_indicators

def test_indicators():
    data = {
        "close": [i for i in range(50)],
        "open": [i for i in range(50)],
        "high": [i+1 for i in range(50)],
        "low": [i-1 for i in range(50)],
        "volume": [100 for _ in range(50)],
    }
    df = pd.DataFrame(data)
    df = add_indicators(df)
    assert "ma_fast" in df.columns
    assert "rsi" in df.columns
