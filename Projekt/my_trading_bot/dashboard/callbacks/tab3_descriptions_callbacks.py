# ==================== dashboard/callbacks/tab3_descriptions_callbacks.py ====================
"""Callbacks for Tab 3 - strategy descriptions."""

import os
from dash import Output, Input
from dash import callback
import dash
from dash import html
from dash import dcc
from config.logger import get_logger

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOC_DIR = os.path.join(BASE_DIR, "docs", "strategy_descriptions")

logger = get_logger(__name__)


@callback(
    Output("strategy-description-content", "children"),
    Input("description-strategy-dropdown", "value")
)
def update_strategy_description(strategy_name):
    """Load and display markdown description for selected strategy."""
    if not strategy_name:
        logger.debug("Description tab called without strategy selection")
        return "Bitte wähle eine Strategie aus dem Dropdown-Menü aus."

    file_path = os.path.join(DOC_DIR, f"{strategy_name}_description.md")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        logger.debug("Loaded description for %s", strategy_name)
        return dcc.Markdown(content)
    logger.warning("No description found for %s", strategy_name)
    return "Keine Beschreibung für die ausgewählte Strategie gefunden."
