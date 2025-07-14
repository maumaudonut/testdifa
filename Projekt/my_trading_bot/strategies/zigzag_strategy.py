import backtrader as bt

class ZigZagStrategy(bt.Strategy):
    params = dict(perc=5)

    def __init__(self):
        self.last_pivot = None

    def next(self):
        price = self.data.close[0]
        if self.last_pivot is None:
            self.last_pivot = price
            return
        change = (price - self.last_pivot) / self.last_pivot * 100
        if not self.position and change >= self.p.perc:
            self.buy()
            self.last_pivot = price
        elif self.position and change <= -self.p.perc:
            self.close()
            self.last_pivot = price
