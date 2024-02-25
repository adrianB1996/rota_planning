import dash
from dash import html
import dash
from dash import dash_table as table
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from components.navbbar import nav

dash.register_page(__name__, path="/rota-tool")


dropdown_options = ["Standard", "Oncall", "Night", "Off"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

layout = html.Div(
    [
        html.H1("Shift Schedule"),
        table.DataTable(
            id="shift-table",
            columns=[
                {"name": "Rota Line", "id": "rota-line", "editable": False},
                {"name": "Monday", "id": "monday", "presentation": "dropdown"},
                {"name": "Tuesday", "id": "tuesday", "presentation": "dropdown"},
                {"name": "Wednesday", "id": "wednesday", "presentation": "dropdown"},
                {"name": "Thursday", "id": "thursday", "presentation": "dropdown"},
                {"name": "Friday", "id": "friday", "presentation": "dropdown"},
                {"name": "Saturday", "id": "saturday", "presentation": "dropdown"},
                {"name": "Sunday", "id": "sunday", "presentation": "dropdown"},
            ],
            data=[
                {
                    "rota-line": 1,
                    "monday": "Standard",
                    "tuesday": "Oncall",
                    "wednesday": "Night",
                    "thursday": "Zero",
                    "friday": "Standard",
                    "saturday": "Off",
                    "sunday": "Off",
                },
                # ... add more rows with initial values
            ],
            editable=True,
            dropdown={
                "monday": {
                    "options": [{"label": i, "value": i} for i in dropdown_options]
                }
            },
            row_deletable=True,
        ),
        html.Button("Add Row", id="add-row-button", n_clicks=0),
    ]
)


@dash.callback(
    Output("shift-table", "data"),
    Input("add-row-button", "n_clicks"),
    State("shift-table", "data"),
)
def add_row(n_clicks, rows):
    if n_clicks > 0:
        rows.append(
            {"rota-line": n_clicks + 1}
        )  # Add empty values for dropdown columns
    return rows
