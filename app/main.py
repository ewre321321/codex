import json
import sys

from .signal import compute_signal


def main() -> None:
    symbol = sys.argv[1] if len(sys.argv) > 1 else "BTCUSDT"
    interval = sys.argv[2] if len(sys.argv) > 2 else "1h"
    result = compute_signal(symbol, interval)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
