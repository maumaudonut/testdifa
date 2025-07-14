import os
import pickle
import pandas as pd
import backtrader as bt
from data.data_handler import download_and_save_data
from strategies.macd_strategy import MACDStrategy
from strategies.rsi_strategy import RSIStrategy
from strategies.sma_strategy import SMAStrategy
from strategies.dummy_strategy import DummyStrategy
from config.settings import PREDEFINED_SYMBOLS, CAPITAL, COMMISSION

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULT_DIR = os.path.join(BASE_DIR, "results")
DATA_DIR = os.path.join(BASE_DIR, "data", "historical_prices")

def run_backtests():
    strategies = {
        "MACD": MACDStrategy,
        "RSI": RSIStrategy,
        "SMA": SMAStrategy,
        "DUMMY": DummyStrategy
    }

    os.makedirs(RESULT_DIR, exist_ok=True)
    download_and_save_data()

    for symbol in PREDEFINED_SYMBOLS:
        df = pd.read_csv(os.path.join(DATA_DIR, f"{symbol}.csv"), index_col="datetime", parse_dates=True)

        for strat_name, strat_class in strategies.items():
            cerebro = bt.Cerebro()
            data = bt.feeds.PandasData(dataname=df)
            cerebro.adddata(data)
            cerebro.addstrategy(strat_class)
            #Batch Size anpassen bei Bedarf aktuell 10%-> 10% des Kapitals pro Trade
            cerebro.addsizer(bt.sizers.PercentSizer, percents=10)
            cerebro.broker.set_cash(CAPITAL)
            cerebro.broker.setcommission(commission=COMMISSION)
            cerebro.addanalyzer(bt.analyzers.TimeReturn, _name='timereturn')
            results = cerebro.run()

            returns = results[0].analyzers.timereturn.get_analysis()
            returns_series = pd.Series(returns)

            with open(os.path.join(RESULT_DIR, f"{symbol}_{strat_name}.pkl"), "wb") as f:
                pickle.dump(returns_series, f)

if __name__ == "__main__":
    run_backtests()
