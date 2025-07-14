"""Download and prepare historical price data."""
import os
import yfinance as yf
import pandas as pd
from config.logger import get_logger

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "historical_prices")

from config.settings import PREDEFINED_SYMBOLS

logger = get_logger(__name__)

def download_and_save_data():
    os.makedirs(DATA_DIR, exist_ok=True)
    logger.info("Downloading historical price data")
    for symbol in PREDEFINED_SYMBOLS:
        logger.debug("Downloading data for %s", symbol)
        df = yf.download(symbol, start="2015-01-01", end="2023-01-01")
        df.dropna(inplace=True)
        df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
        df.columns = ['open', 'high', 'low', 'close', 'volume']
        df.index.name = 'datetime'
        df.to_csv(os.path.join(DATA_DIR, f"{symbol}.csv"), index=True)
    logger.info("Data download finished")

