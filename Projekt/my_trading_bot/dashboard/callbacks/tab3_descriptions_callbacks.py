# ==================== dashboard/callbacks/tab3_descriptions_callbacks.py ====================

import os
from dash import Output, Input
from dash import callback
import dash
from dash import html
from dash import dcc

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOC_DIR = os.path.join(BASE_DIR, "docs", "strategy_descriptions")


@callback(
    Output("strategy-description-content", "children"),
    Input("description-strategy-dropdown", "value")
)
def update_strategy_description(strategy_name):
    if not strategy_name:
        return "Bitte wähle eine Strategie aus dem Dropdown-Menü aus."

    file_path = os.path.join(DOC_DIR, f"{strategy_name}_description.md")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        return dcc.Markdown(content)

    return "Keine Beschreibung für die ausgewählte Strategie gefunden."
