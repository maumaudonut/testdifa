"""Central logging configuration used across the project."""

import logging
from logging.handlers import RotatingFileHandler
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, 'trading_bot.log')

DEFAULT_LOG_LEVEL = logging.INFO

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=3)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logging.basicConfig(level=DEFAULT_LOG_LEVEL, handlers=[file_handler, stream_handler])


def get_logger(name: str) -> logging.Logger:
    """Return a logger configured with the project settings."""
    return logging.getLogger(name)
