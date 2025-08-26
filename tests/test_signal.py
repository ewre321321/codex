from app import signal


def test_compute_signal(monkeypatch):
    def fake_klines(symbol, interval, limit=100):
        return [float(i) for i in range(1, limit + 1)]
    monkeypatch.setattr(signal, "get_klines", fake_klines)
    result = signal.compute_signal("TEST")
    assert result["signal"] == "long"
    assert result["symbol"] == "TEST"
