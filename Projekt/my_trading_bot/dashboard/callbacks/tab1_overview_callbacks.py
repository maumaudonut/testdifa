# ==================== dashboard/callbacks/tab1_overview_callbacks.py ====================

import dash
from dash.dependencies import Input, Output
from dashboard.data_loader import load_returns
from dash import html
import plotly.graph_objs as go
import quantstats.reports as qsr

@dash.callback(
    [Output("performance-table", "children"),
     Output("overview-comparison-graph", "figure")],
    [Input("overview-symbol-dropdown", "value"),
     Input("overview-strategy-dropdown", "value")]
)
def update_overview_tab(selected_symbols, selected_strategies):
    if not selected_symbols or not selected_strategies:
        return dash.no_update, dash.no_update

    rows = []
    fig = go.Figure()

    for symbol in selected_symbols:
        for strategy in selected_strategies:
            returns = load_returns(symbol, strategy)
            if not returns.empty:
                stats_df = qsr.metrics(returns, display=False)
                stats_dict = stats_df.iloc[:, 0].to_dict()  # Zugriff auf die erste Spalte
                stats = (
                    stats_dict.get("cagr", 0),
                    stats_dict.get("sharpe", 0),
                    stats_dict.get("max_drawdown", 0)
                )
                rows.append(html.Tr([
                    html.Td(symbol),
                    html.Td(strategy),
                    html.Td(f"{stats[0]:.2%}"),
                    html.Td(f"{stats[1]:.2f}"),
                    html.Td(f"{stats[2]:.2%}")
                ]))
                fig.add_trace(go.Scatter(x=returns.index, y=(1 + returns).cumprod(), mode='lines', name=f"{symbol}-{strategy}"))

    table = html.Table([
        html.Thead(html.Tr([html.Th("Symbol"), html.Th("Strategie"), html.Th("CAGR"), html.Th("Sharpe"), html.Th("Max Drawdown")])),
        html.Tbody(rows)
    ])

    fig.update_layout(title="Kumulierte Rendite", xaxis_title="Datum", yaxis_title="Wert")
    return table, fig
