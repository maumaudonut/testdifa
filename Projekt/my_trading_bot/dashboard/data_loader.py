"""Utility functions for loading backtest results for the dashboard."""

import os
import pickle
import pandas as pd
from config.logger import get_logger

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULT_DIR = os.path.join(BASE_DIR, "results")

logger = get_logger(__name__)

def get_available_results():
    """Return a list of tuples of available (symbol, strategy) results."""
    files = [f for f in os.listdir(RESULT_DIR) if f.endswith("_returns.pkl")]
    combos = []
    for f in files:
        name = f.replace("_returns.pkl", "")
        strat, symbol = name.split("_")
        combos.append((symbol, strat))
    logger.debug("Found result combinations: %s", combos)
    return combos

def load_returns(symbol, strategy):
    """Load pickled return series for a strategy and symbol."""
    file_path = os.path.join(RESULT_DIR, f"{strategy}_{symbol}_returns.pkl")
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            series = pickle.load(f)
        logger.debug("Loaded returns for %s-%s", strategy, symbol)
        return series
    logger.warning("Result file not found: %s", file_path)
    return pd.Series()
