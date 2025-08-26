from typing import Dict

from .binance import get_klines
from .indicators import ema, rsi


def compute_signal(symbol: str, interval: str = "1h") -> Dict[str, float]:
    prices = get_klines(symbol, interval, limit=100)
    ema20 = ema(prices, 20)[-1]
    ema50 = ema(prices, 50)[-1]
    rsi14 = rsi(prices, 14)[-1]
    last = prices[-1]
    if last > ema20 > ema50 and rsi14 > 55:
        direction = "long"
    elif last < ema20 < ema50 and rsi14 < 45:
        direction = "short"
    else:
        direction = "neutral"
    return {
        "symbol": symbol,
        "interval": interval,
        "price": last,
        "ema20": ema20,
        "ema50": ema50,
        "rsi14": rsi14,
        "signal": direction,
    }
