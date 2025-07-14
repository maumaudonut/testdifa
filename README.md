# My Trading Bot Dashboard
This repository contains a small prototype for a trading strategy backtesting framework. It includes example strategies, historical data and a Plotly Dash web interface to analyze the backtest results. The dashboard consists of three tabs:
1. **Übersicht & Vergleich** – mehrere Strategien und Symbole gleichzeitig vergleichen
2. **Strategiedetails** – detaillierte Metriken für eine Strategie/Symbol-Kombination
3. **Strategiebeschreibungen** – Textbeschreibungen aus dem `docs/` Ordner


## Folder structure

```
Projekt/
  my_trading_bot/                # Python package with the trading logic
    backtest_runner.py          # Executes backtests for each strategy/symbol
    config/                     # Global settings
    data/                       # Data download helpers and CSV files
    dashboard/                  # Plotly Dash application
    docs/                       # Markdown descriptions for strategies
    results/                    # Pickled returns named <STRATEGY>_<SYMBOL>_returns.pkl
    strategies/                 # Example trading strategies
  requirements.txt

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

All modules use a central logging configuration defined in `my_trading_bot/config/logger.py`. Log files are written to `Projekt/my_trading_bot/logs/trading_bot.log`.

## Dokumentation
Technische Dokumentation wird mit [Sphinx](https://www.sphinx-doc.org) generiert. Im Ordner `Projekt/my_trading_bot/docs/source` befinden sich die Konfigurationsdateien. Die HTML-Dokumente lassen sich mit folgendem Befehl erstellen:

```bash
sphinx-build Projekt/my_trading_bot/docs/source docs_build
```

