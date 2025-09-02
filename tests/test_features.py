import pandas as pd
from src.feature_engineering import add_features

def test_add_features():
    df = pd.DataFrame({
        "close": [1,2,3,4,5,6,7,8,9,10]*10,
        "open":  [1]*100,
        "high":  [1]*100,
        "low":   [1]*100,
        "volume":[1]*100,
        "timestamp": pd.date_range("2021-01-01", periods=100, freq="h")
    })
    df = add_features(df)
    assert "ma_fast" in df.columns
    assert "ma_slow" in df.columns
    assert "volatility" in df.columns
