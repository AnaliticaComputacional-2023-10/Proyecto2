from dash import html
from apps import navigation
import dash_bootstrap_components as dbc

texto = '''Hola'''

inicio_layout = html.Div(children=[

    #Barra de Navegación
    navigation.navbar,
    html.Br(),

    #Titulo de la pagina
    html.H1(children = '¿Como se comportan nuestras variables?''',
            style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),

    #Botones para ir de la pagina de inicio a las instrucciones y programa
    html.Div(children=[
        html.Div(children=[
            dbc.Button("Instrucciones", size="lg", id="inicio_instrucciones", href="/instrucciones",
                       style={'margin-right': '10px', 'verticalAlign': 'middle'})],
            style={'display': 'inline-flex'}),
        html.Div(children=[
            dbc.Button("Programa", size="lg", id="inicio_programa", href="/programa",
                       style={'margin-left': '10px', 'verticalAlign': 'middle'})],
            style={'display': 'inline-flex'})],
        style={'margin-bottom': '10px',
              'display': 'flex',
              'justify-content': 'center'}),
    html.Br()
])