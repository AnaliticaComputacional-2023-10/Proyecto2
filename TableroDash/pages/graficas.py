from dash import html
from apps import navigation
from app import app
from dash import html
from dash import dcc
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px

columnas = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
            'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']

df = pd.read_csv("./Data/Original/processed.cleveland.data", names = columnas)

df.age = df.age.astype(int)
df.sex = df.sex.astype(int)
df.cp = df.cp.astype(int)
df.trestbps = df.trestbps.astype(int)
df.chol = df.chol.astype(int)
df.fbs = df.fbs.astype(int)
df.restecg = df.restecg.astype(int)
df.thalach = df.thalach.astype(int)
df.exang = df.exang.astype(int)
df.slope = df.slope.astype(int)

# ------------
# Null values
# ------------

df['caNull'] = df['ca']
df.loc[df['caNull'] == '?', 'ca'] = float(df.ca.mode()[0])
df.loc[df['caNull'] != '?', 'ca'] = df['ca']
df['ca'] = pd.to_numeric(df['ca']).astype('int32')

df['thalNull'] = df['thal']
df.loc[df['thalNull'] == '?', 'thal'] = float(df.thal.mode()[0])
df.loc[df['thalNull'] != '?', 'thal'] = df['thal']
df['thal'] = pd.to_numeric(df['thal']).astype('int32')

# ------------
# Target
# ------------

df.loc[df['num'] == 0, 'heartdis'] = 0
df.loc[df['num'] != 0, 'heartdis'] = 1
df.heartdis = df.heartdis.astype(int)

# ------------
# Drop columns
# ------------
df.drop(['num', 'caNull', 'thalNull'], axis=1, inplace=True)

variable = df.columns
diccionario_cat = {'Sexo': 'sex', 'Tipo de dolor en el Pecho': 'cp','Azucar en sangre en ayunas': 'fbs',
               'Resultados electrocardiograficos en reposo': 'restecg',
               'Angina inducida por ejercicio': 'exang','Pendiente del segmento ST': 'slope',
               'Numero de vasos coloreados': 'ca','Talasemia': 'thal',
               'Presencia de enfermedad cardiaca': 'heartdis'}

diccionario_num = {'Edad': 'age', 'Presión arterial en reposo': 'trestbps',
               'Colesterol serico': 'chol','Frecuencia cardiaca maxima': 'thalach',
               'Depresión del segmento ST': 'oldpeak'}

#Layout
graficas_layout = html.Div(children=[

    #Barra de Navegación
    navigation.navbar,
    html.Br(),

    #Titulo de la pagina
    html.H1(children = '''¿Cómo se comportan las variables?''',
            style={'textAlign': 'center'}),
    html.Br(),

    #Categoricas vs Categoricas
    html.H4(children = '''Graficas variables Categoricas vs Categoricas''',
            style={'textAlign': 'center'}),
    html.Div(
        dbc.Row(
            [
                #Eje Y
                dbc.Col(
                    html.Div([
                        html.Label('Seleccione un valor para el eje X:'),
                        dcc.Dropdown(
                            id='graph-x1',
                            options=[{'label': i, 'value': diccionario_cat[i]} for i in diccionario_cat],
                            value='sex'
                        )
                    ],style={'width': '30rem', 'display': 'inline-block'}),
                ),
                #Eje X
                dbc.Col(
                    html.Div([
                        html.Label('Seleccione un valor para el eje Y:'),
                        dcc.Dropdown(
                            id='graph-y1',
                            options=[{'label': i, 'value': diccionario_cat[i]} for i in diccionario_cat],
                            value='cp'
                        )
                    ],style={'width': '30rem', 'float': 'right', 'display': 'inline-block'})
                ),
            ],
            className="mt-4",
        ),
        style={'display': 'flex',
              'justify-content': 'center'}
    ),

    #Grafica
    html.Div(
        style={'textAlign': 'center','margin': '50px auto','maxWidth': '1200px'},
        children=[
            dcc.Graph(id='graphic-catcat'),
    ]),
    html.Br(),

    #Categoricas vs Numericas
    html.H4(children = '''Graficas variables Categoricas vs Numericas''',
            style={'textAlign': 'center'}),
    html.Div(
        dbc.Row(
            [
                #Eje Y
                dbc.Col(
                    html.Div([
                        html.Label('Seleccione un valor para el eje X:'),
                        dcc.Dropdown(
                            id='graph-x2',
                            options=[{'label': i, 'value': diccionario_cat[i]} for i in diccionario_cat],
                            value='sex'
                        )
                    ],style={'width': '30rem', 'display': 'inline-block'}),
                ),
                #Eje X
                dbc.Col(
                    html.Div([
                        html.Label('Seleccione un valor para el eje Y:'),
                        dcc.Dropdown(
                            id='graph-y2',
                            options=[{'label': i, 'value': diccionario_num[i]} for i in diccionario_num],
                            value='age'
                        )
                    ],style={'width': '30rem', 'float': 'right', 'display': 'inline-block'})
                ),
            ],
            className="mt-4",
        ),
        style={'display': 'flex',
              'justify-content': 'center'}
    ),

    #Grafica
    html.Div(
        style={'textAlign': 'center','margin': '50px auto','maxWidth': '1200px'},
        children=[
            dcc.Graph(id='graphic-catnum'),
    ]),
    html.Br(),

    #Numericas vs Numericas
    html.H4(children = '''Graficas variables Numericas vs Numericas''',
            style={'textAlign': 'center'}),
    html.Div(
        dbc.Row(
            [
                #Eje Y
                dbc.Col(
                    html.Div([
                        html.Label('Seleccione un valor para el eje X:'),
                        dcc.Dropdown(
                            id='graph-x3',
                            options=[{'label': i, 'value': diccionario_num[i]} for i in diccionario_num],
                            value='age'
                        )
                    ],style={'width': '30rem', 'display': 'inline-block'}),
                ),
                #Eje X
                dbc.Col(
                    html.Div([
                        html.Label('Seleccione un valor para el eje Y:'),
                        dcc.Dropdown(
                            id='graph-y3',
                            options=[{'label': i, 'value': diccionario_num[i]} for i in diccionario_num],
                            value='oldpeak'
                        )
                    ],style={'width': '30rem', 'float': 'right', 'display': 'inline-block'})
                ),
            ],
            className="mt-4",
        ),
        style={'display': 'flex',
              'justify-content': 'center'}
    ),

    #Grafica
    html.Div(
        style={'textAlign': 'center','margin': '50px auto','maxWidth': '1200px'},
        children=[
            dcc.Graph(id='graphic-numnum'),
    ]),
    html.Br(),
])

@app.callback(
    Output('graphic-catcat', 'figure'),
    Input('graph-x1', 'value'),
    Input('graph-y1', 'value')
)
def update_graph(xaxis_column_name, yaxis_column_name):

    fig_cat = px.histogram(df, x=xaxis_column_name, y=yaxis_column_name,
                     color=yaxis_column_name, barmode='group',histfunc='count')
    return fig_cat


@app.callback(
    Output('graphic-catnum', 'figure'),
    Input('graph-x2', 'value'),
    Input('graph-y2', 'value')
)
def update_graph(xaxis_column_name, yaxis_column_name):

    fig_bar = px.violin(df, x=xaxis_column_name, y=yaxis_column_name,
                         color=xaxis_column_name
                         )
    return fig_bar

@app.callback(
    Output('graphic-numnum', 'figure'),
    Input('graph-x3', 'value'),
    Input('graph-y3', 'value')
)
def update_graph(xaxis_column_name, yaxis_column_name):

    fig_disp = px.scatter(df, x=xaxis_column_name, y=yaxis_column_name)

    return fig_disp








