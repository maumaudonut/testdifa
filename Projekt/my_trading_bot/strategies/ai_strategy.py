"""AI-based strategy using logistic regression on RSI and SMA."""
import backtrader as bt
from sklearn.linear_model import LogisticRegression

class AIStrategy(bt.Strategy):

    params = dict(train_period=200, prob_threshold=0.55)

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.rsi = bt.indicators.RSI_SMA(self.dataclose, period=14)
        self.sma = bt.indicators.SimpleMovingAverage(self.dataclose, period=14)

        self.model = LogisticRegression(solver="liblinear")

    def next(self):
        if len(self) < self.p.train_period:
            return
        X, y = [], []
        for i in range(-self.p.train_period, -1):
            rsi_val = float(self.rsi[i])
            sma_val = float(self.sma[i])
            if not (bt.math.isnan(rsi_val) or bt.math.isnan(sma_val)):
                X.append([rsi_val, sma_val])
                y.append(1 if self.dataclose[i+1] > self.dataclose[i] else 0)
        if X:
            self.model.fit(X, y)
            prob = self.model.predict_proba([[self.rsi[0], self.sma[0]]])[0, 1]
            if not self.position and prob > self.p.prob_threshold:
                self.buy()
            elif self.position and prob < 1 - self.p.prob_threshold:
                self.close()

