from typing import List

def ema(prices: List[float], period: int) -> List[float]:
    if len(prices) < period:
        raise ValueError("not enough prices for EMA")
    k = 2 / (period + 1)
    sma = sum(prices[:period]) / period
    ema_vals = [sma]
    for price in prices[period:]:
        ema_vals.append(price * k + ema_vals[-1] * (1 - k))
    return ema_vals

def rsi(prices: List[float], period: int = 14) -> List[float]:
    if len(prices) <= period:
        raise ValueError("not enough prices for RSI")
    gains = []
    losses = []
    for i in range(1, len(prices)):
        delta = prices[i] - prices[i - 1]
        gains.append(max(delta, 0))
        losses.append(abs(min(delta, 0)))
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    if avg_loss:
        rs = avg_gain / avg_loss
        rsi_vals = [100 - (100 / (1 + rs))]
    else:
        rsi_vals = [100.0 if avg_gain else 0.0]
    for i in range(period, len(gains)):
        avg_gain = (avg_gain * (period - 1) + gains[i]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i]) / period
        if avg_loss:
            rs = avg_gain / avg_loss
            rsi_vals.append(100 - (100 / (1 + rs)))
        else:
            rsi_vals.append(100.0 if avg_gain else 0.0)
    return rsi_vals
