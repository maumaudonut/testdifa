import backtrader as bt

class BollingerStrategy(bt.Strategy):
    params = dict(period=20, devfactor=2)

    def __init__(self):
        self.bbands = bt.indicators.BollingerBands(self.datas[0].close,
                                                   period=self.p.period,
                                                   devfactor=self.p.devfactor)

    def next(self):
        if not self.position and self.datas[0].close[0] < self.bbands.lines.bot[0]:
            self.buy()
        elif self.position and self.datas[0].close[0] > self.bbands.lines.mid[0]:
            self.close()
