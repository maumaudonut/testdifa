import backtrader as bt

class ZigZagStrategy(bt.Strategy):
    params = dict(perc=5)

    def __init__(self):
        self.last_pivot = None
        self.direction = None  # "up" oder "down"

    def next(self):
        price = self.data.close[0]

        if self.last_pivot is None:
            self.last_pivot = price
            return

        change_pct = (price - self.last_pivot) / self.last_pivot * 100

        if not self.position:
            if change_pct >= self.p.perc:
                self.buy()
                self.last_pivot = price
                self.direction = "up"
            elif change_pct <= -self.p.perc:
                self.sell()
                self.last_pivot = price
                self.direction = "down"
        else:
            # Close position bei Umkehr
            if self.direction == "up" and change_pct <= -self.p.perc:
                self.close()
                self.last_pivot = price
                self.direction = "down"
            elif self.direction == "down" and change_pct >= self.p.perc:
                self.close()
                self.last_pivot = price
                self.direction = "up"
