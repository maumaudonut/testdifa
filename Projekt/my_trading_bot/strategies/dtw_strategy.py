import backtrader as bt

class DTWStrategy(bt.Strategy):
    params = dict(window=10, threshold=15)

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.pattern = list(range(self.p.window))

    def next(self):
        if len(self.dataclose) < self.p.window:
            return
        recent = [float(self.dataclose[-i]) for i in range(self.p.window, 0, -1)]
        distance = sum((recent[i] - self.pattern[i]) ** 2 for i in range(self.p.window)) ** 0.5
        if not self.position and distance < self.p.threshold:
            self.buy()
        elif self.position and distance > self.p.threshold * 1.5:
            self.close()
