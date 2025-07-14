import backtrader as bt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
import numpy as np

class AIStrategy(bt.Strategy):
    params = dict(train_period=200, prob_threshold=0.55)

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.rsi = bt.indicators.RSI_SMA(self.dataclose, period=14)
        self.sma = bt.indicators.SimpleMovingAverage(self.dataclose, period=14)
        self.model = LogisticRegression(solver="liblinear")
        self.scaler = MinMaxScaler()
        self.X = []
        self.y = []

    def next(self):
        if len(self) < self.p.train_period + 1:
            return

        # Aktuellen RSI/SMA-Wert abrufen
        rsi_val = float(self.rsi[0])
        sma_val = float(self.sma[0])

        # Trainingsdaten aufbauen
        self.X = []
        self.y = []
        for i in range(-self.p.train_period, -1):
            rsi_i = float(self.rsi[i])
            sma_i = float(self.sma[i])
            if not (bt.math.isnan(rsi_i) or bt.math.isnan(sma_i)):
                self.X.append([rsi_i, sma_i])
                self.y.append(1 if self.dataclose[i + 1] > self.dataclose[i] else 0)

        # Training durchführen
        X_np = np.array(self.X)
        X_scaled = self.scaler.fit_transform(X_np)
        self.model.fit(X_scaled, self.y)

        # Vorhersage auf aktuelle Daten anwenden
        current_features = self.scaler.transform([[rsi_val, sma_val]])
        prob = self.model.predict_proba(current_features)[0, 1]

        if not self.position and prob > self.p.prob_threshold:
            self.buy()
        elif self.position and prob < 1 - self.p.prob_threshold:
            self.close()
