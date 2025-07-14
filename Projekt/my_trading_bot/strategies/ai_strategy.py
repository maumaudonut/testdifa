import backtrader as bt
from sklearn.linear_model import LogisticRegression

class AIStrategy(bt.Strategy):
    params = dict(train_period=200)

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.rsi = bt.indicators.RSI_SMA(self.dataclose, period=14)
        self.sma = bt.indicators.SimpleMovingAverage(self.dataclose, period=14)
        self.model = LogisticRegression()
        self.trained = False

    def prenext(self):
        if len(self) >= self.p.train_period and not self.trained:
            X = []
            y = []
            for i in range(-self.p.train_period, -1):
                rsi_val = float(self.rsi[i])
                sma_val = float(self.sma[i])
                if not (bt.math.isnan(rsi_val) or bt.math.isnan(sma_val)):
                    X.append([rsi_val, sma_val])
                    y.append(1 if self.dataclose[i+1] > self.dataclose[i] else 0)
            if X:
                self.model.fit(X, y)
                self.trained = True

    def next(self):
        if not self.trained:
            self.prenext()
            return
        pred = self.model.predict([[self.rsi[0], self.sma[0]]])[0]
        if not self.position and pred == 1:
            self.buy()
        elif self.position and pred == 0:
            self.close()
