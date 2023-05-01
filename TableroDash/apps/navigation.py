import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output, State
import dash

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# NAVIGATION BAR
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------


navbar = dbc.Navbar(
    dbc.Container(
        [

            # ------------------------------------------------
            # Titulo
            # ------------------------------------------------

            dbc.Row([
                dbc.Col([
                    html.Img(src=dash.get_asset_url(
                        'logo.png'), height="40px"),
                    dbc.NavbarBrand(
                        "Predicción de Enfermedades Cardíacas", className="ms-2")
                ],
                    width={"size": "auto"})
            ],
                align="center",
                className="g-0"),

            # ------------------------------------------------
            # Botones
            # ------------------------------------------------

            dbc.Row([
                dbc.Col([
                    dbc.Nav([

                        # ------------------------------------------------
                        # Inicio
                        # ------------------------------------------------

                        dbc.NavItem(dbc.NavLink("Inicio", href="/")),

                        # ------------------------------------------------
                        # Instrucciones
                        # ------------------------------------------------

                        dbc.NavItem(dbc.NavLink(
                                    "Instrucciones", href="/instrucciones")),

                        # ------------------------------------------------
                        # Programa
                        # ------------------------------------------------

                        dbc.NavItem(dbc.NavLink(
                                    "Programa", href="/programa")),

                        # ------------------------------------------------
                        # Graficas
                        # ------------------------------------------------

                        dbc.NavItem(dbc.NavLink(
                                    "Graficas", href="/graficas")),

                    ],
                        navbar=True
                    )
                ],
                    width={"size": "auto"})
            ],
                align="center"),
        ],
        fluid=True
    ),
    color="primary",
    dark=True
)
