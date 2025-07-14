import backtrader as bt

class DTWStrategy(bt.Strategy):
    params = dict(window=10, threshold=5)

    def __init__(self):
        self.dataclose = self.datas[0].close

    def next(self):
        if len(self) <= self.p.window:
            return
        recent = [float(self.dataclose[-i]) for i in range(self.p.window, 0, -1)]
        pattern = [recent[0] + i * (recent[-1] - recent[0]) / (self.p.window - 1)
                   for i in range(self.p.window)]
        distance = sum(abs(recent[i] - pattern[i]) for i in range(self.p.window))
        if not self.position and distance < self.p.threshold:
            self.buy()
        elif self.position and distance > self.p.threshold * 2:
            self.close()
