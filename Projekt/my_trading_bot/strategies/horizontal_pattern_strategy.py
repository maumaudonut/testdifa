import backtrader as bt

class HorizontalPatternStrategy(bt.Strategy):
    params = dict(lookback=20)

    def next(self):
        if len(self) < self.p.lookback:
            return
        highs = [self.data.high[-i] for i in range(1, self.p.lookback + 1)]
        lows = [self.data.low[-i] for i in range(1, self.p.lookback + 1)]
        max_high = max(highs)
        min_low = min(lows)
        if not self.position and self.data.close[0] > max_high:
            self.buy()
        elif self.position and self.data.close[0] < min_low:
            self.close()
