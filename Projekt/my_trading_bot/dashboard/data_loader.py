import os
import pickle
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULT_DIR = os.path.join(BASE_DIR, "results")

def get_available_results():
    files = [f for f in os.listdir(RESULT_DIR) if f.endswith(".pkl")]
    combinations = [f.replace(".pkl", "").split("_") for f in files]
    return combinations

def load_returns(symbol, strategy):
    file_path = os.path.join(RESULT_DIR, f"{symbol}_{strategy}.pkl")
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return pickle.load(f)
    return pd.Series()
