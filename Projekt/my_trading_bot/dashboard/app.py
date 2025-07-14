"""Main entry point for the Plotly Dash dashboard."""

import dash
from dash import dcc, html
from dashboard.layouts import (
    tab1_overview_layout,
    tab2_details_layout,
    tab3_descriptions_layout,
)

app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Trading Dashboard"

app.layout = html.Div([
    dcc.Tabs(id="tabs", value="tab1", children=[
        dcc.Tab(label="Übersicht & Vergleich", value="tab1"),
        dcc.Tab(label="Strategiedetails", value="tab2"),
        dcc.Tab(label="Strategiebeschreibungen", value="tab3")
    ]),
    html.Div(id="tabs-content")
])

@app.callback(
    dash.dependencies.Output('tabs-content', 'children'),
    [dash.dependencies.Input('tabs', 'value')]
)
def render_tab_content(tab):
    """Return the layout for the currently active tab."""
    if tab == 'tab1':
        return tab1_overview_layout.layout
    elif tab == 'tab2':
        return tab2_details_layout.layout
    elif tab == 'tab3':
        return tab3_descriptions_layout.layout

if __name__ == '__main__':
    from dashboard.callbacks import tab1_overview_callbacks, tab2_details_callbacks, tab3_descriptions_callbacks
    app.run(debug=True)
