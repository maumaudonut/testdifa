# My Trading Bot Dashboard

This repository contains a small prototype for a trading strategy backtesting framework. It includes example strategies, historical data and a Plotly Dash web interface to analyze the backtest results.

## Folder structure

```
Projekt/
  my_trading_bot/                # Python package with the trading logic
    backtest_runner.py          # Executes backtests for each strategy/symbol
    config/                     # Global settings
    data/                       # Data download helpers and CSV files
    dashboard/                  # Plotly Dash application
    docs/                       # Markdown descriptions for strategies
    results/                    # Pickled returns from completed backtests
    strategies/                 # Example trading strategies
  requirements.txt
```

## Usage
1. Install dependencies:
   ```bash
   pip install -r Projekt/requirements.txt
   ```
2. Run the backtests to generate result files:
   ```bash
   python Projekt/my_trading_bot/backtest_runner.py
   ```
3. Start the dashboard:
   ```bash
   python Projekt/my_trading_bot/dashboard/app.py
   ```
   Open the displayed address in your browser to interact with the three tabs:
   - **Übersicht & Vergleich** – compare strategies across symbols
   - **Strategiedetails** – deep dive into a single strategy/symbol
   - **Strategiebeschreibungen** – read the markdown descriptions

This prototype uses local CSV files for historical price data and stores backtest results in `results/` as pickled Pandas Series.
