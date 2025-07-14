"""Run backtests for all strategies and symbols."""
import os
import pickle
import pandas as pd
import backtrader as bt
from data.data_handler import download_and_save_data
from config.logger import get_logger

logger = get_logger(__name__)
from strategies.macd_strategy import MACDStrategy
from strategies.rsi_strategy import RSIStrategy
from strategies.sma_strategy import SMAStrategy
from strategies.dummy_strategy import DummyStrategy
from strategies.ai_strategy import AIStrategy
from strategies.dtw_strategy import DTWStrategy
from strategies.horizontal_pattern_strategy import HorizontalPatternStrategy
from strategies.bollinger_strategy import BollingerStrategy
from strategies.zigzag_strategy import ZigZagStrategy
from config.settings import PREDEFINED_SYMBOLS, CAPITAL, COMMISSION

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULT_DIR = os.path.join(BASE_DIR, "results")
DATA_DIR = os.path.join(BASE_DIR, "data", "historical_prices")

def run_backtests():
    """Execute all backtests and store the return series."""
    logger.info("Starting backtests")
    strategies = {
        "MACD": MACDStrategy,
        "RSI": RSIStrategy,
        "SMA": SMAStrategy,
        "DUMMY": DummyStrategy,
        "AI": AIStrategy,
        "DTW": DTWStrategy,
        "HORIZONTAL": HorizontalPatternStrategy,
        "BOLLINGER": BollingerStrategy,
        "ZIGZAG": ZigZagStrategy
    }

    os.makedirs(RESULT_DIR, exist_ok=True)
    download_and_save_data()
    logger.info("Historical data downloaded")

    for symbol in PREDEFINED_SYMBOLS:
        logger.info("Running backtests for symbol %s", symbol)
        df = pd.read_csv(os.path.join(DATA_DIR, f"{symbol}.csv"), index_col="datetime", parse_dates=True)

        for strat_name, strat_class in strategies.items():
            logger.debug("Running strategy %s on %s", strat_name, symbol)
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

            filename = f"{strat_name}_{symbol}_returns.pkl"
            with open(os.path.join(RESULT_DIR, filename), "wb") as f:
                pickle.dump(returns_series, f)
            logger.info("Saved results: %s", filename)

if __name__ == "__main__":
    run_backtests()
    logger.info("Backtests completed")

