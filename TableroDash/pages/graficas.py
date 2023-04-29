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

df = pd.read_csv("./Data/processed.cleveland.data", names = columnas)

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
diccionario = {'Edad': 'age', 'Sexo': 'sex', 'Dolor en Pecho': 'cp'}

columnas = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
            'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']

#Layout
graficas_layout = html.Div(children=[

    #Barra de Navegación
    navigation.navbar,
    html.Br(),

    #Titulo de la pagina
    html.H1(children = '''¿Cómo se comportan nuestras variables?''',
            style={'textAlign': 'center'}),
    html.Br(),

    html.Div(
        dbc.Row(
            [
                #Eje Y
                dbc.Col(
                    html.Div([
                        html.Label('Seleccione un valor para el eje Y:'),
                        dcc.Dropdown(
                            id='xaxis-column',
                            options=[{'label': i, 'value': diccionario[i]} for i in diccionario],
                            value='age'
                        )
                    ],style={'width': '30rem', 'display': 'inline-block'}),
                ),
                #Eje X
                dbc.Col(
                    html.Div([
                        html.Label('Seleccione un valor para el eje X:'),
                        dcc.Dropdown(
                            id='yaxis-column',
                            options=[{'label': i, 'value': diccionario[i]} for i in diccionario],
                            value='sex'
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
            dcc.Graph(id='indicator-graphic'),
    ]),

    html.Br()

])

@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value')
)
def update_graph(xaxis_column_name, yaxis_column_name):

    fig = px.scatter(df, x=xaxis_column_name, y=yaxis_column_name,
                 color='heartdis',
                 hover_data=variable,
                 color_discrete_sequence=['red', 'blue'])

    fig.update_layout(transition_duration=500)

    return fig



