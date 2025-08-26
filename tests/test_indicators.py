from app.indicators import ema, rsi


def test_ema_last_value():
    prices = list(range(1, 61))
    assert round(ema(prices, 20)[-1], 2) == 50.5


def test_rsi_range():
    prices = list(range(1, 100))
    values = rsi(prices, 14)
    assert all(0 <= v <= 100 for v in values)
