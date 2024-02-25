import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from components.navbbar import nav


# Dash app initialization
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)

# App layout with NHS-branded navbar
app.layout = html.Div(
    [
        html.Div(nav, className="navbar"),
        dash.page_container,
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
