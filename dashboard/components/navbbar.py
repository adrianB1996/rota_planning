import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

nav = dbc.Navbar(
    [
        html.A(
            dbc.Row(
                [
                    dbc.Col(html.Img(src="assets/nhs_logo.png", height="30px")),
                    dbc.Col(
                        dbc.NavbarBrand(
                            "Unnoffical Rota Planning Tool", className="nav-title"
                        )
                    ),
                ],
                align="center",
                className="g-0",
            ),
            href="/",
            style={"textDectoration": "none"},
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(
            [
                dbc.Nav(
                    [
                        dbc.NavItem(
                            dbc.NavLink("Home", href="/")
                        ),  # these should go to the left
                        dbc.NavItem(dbc.NavLink("Rota Tool", href="/rota-tool")),
                        dbc.NavItem(dbc.NavLink("About Us", href="/about-us")),
                        dbc.NavItem(
                            dbc.NavLink("Contribute", href="/contribute")
                        ),  # these should go the right
                    ],
                    pills=True,
                    navbar=True,
                )
            ],
            id="navbar-collapse",
            is_open=False,
            navbar=True,
        ),
    ],
    color="#005EB8",
)


# add callback for toggling the collapse on small screens
@dash.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
