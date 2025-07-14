# Architektur

Dieses Dokument beschreibt die grobe Struktur des Projekts und den Datenfluss zwischen den Modulen.

* `backtest_runner.py` orchestriert die Backtests und speichert Ergebnisse im Ordner `results/`.
* Die Strategien befinden sich im Paket `strategies` und werden dynamisch geladen.
* `data/data_handler.py` kümmert sich um den Download historischer Kursdaten.
* Das Plotly Dash Dashboard im Ordner `dashboard/` lädt die Resultate über `data_loader.py` und stellt sie interaktiv dar.
* `config/logger.py` richtet das zentrale Logging ein, welches von allen Modulen genutzt wird.

