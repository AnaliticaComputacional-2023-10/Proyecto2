# -------------------------------------------------------------------------------------------------------
# Librerias
# -------------------------------------------------------------------------------------------------------

from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
from apps import navigation
from app import app
import dash_bootstrap_components as dbc
import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import plotly.express as px

# -------------------------------------------------------------------------------------------------------
# html
# -------------------------------------------------------------------------------------------------------

programa_layout = html.Div(children=[
    navigation.navbar,
    html.Br(),
    html.H1(children="Programa de Predicción de Enfermedades Cardíacas",
            style={'textAlign': 'center'}),
    html.Br(),

    dbc.Row([
        dbc.Col([html.Div("Información del Paciente",
                          style={'font-weight': 'bold', 'font-size': 20}),
            dbc.Row([html.Div("Datos demográficos del paciente",
                              style={'font-weight': 'bold', 'font-size': 16, 'padding': '10px 25px'})]),
            dbc.Row([
                dbc.Col(html.Div([
                    html.Label('Edad del paciente (en años): '),
                    dcc.Input(
                        type="number",
                        debounce=True,
                        value='',
                        id='age'
                    )
                ]), width={"size": 3}),
                dbc.Col(html.Div([
                    html.Label('Sexo: '),
                    dcc.Dropdown(
                        options=[
                            {'label': 'Hombre', 'value': '1'},
                            {'label': 'Mujer', 'value': '0'}
                        ],
                        value='',
                        id='sex_male'
                    )
                ]), width={"size": 3}, style={'margin-left': '50px'}),
            ], style={'padding': '10px 25px'}),
            dbc.Row([html.Div("Salud del paciente",
                              style={'font-weight': 'bold', 'font-size': 16, 'padding': '10px 25px'})]),
            dbc.Row([
                dbc.Col(html.Div([
                    html.Label('Presión arterial (mmHg): '),
                    dcc.Input(
                        type="number",
                        debounce=True,
                        value='',
                        id='resting_bp'
                    )
                ]), width={"size": 3}, style={'padding': '10px 10px'}),
                dbc.Col(html.Div([
                    html.Label('Frecuencia cardíaca máxima (bpm): '),
                    dcc.Input(
                        type="number",
                        debounce=True,
                        value='',
                        id='maximum_hr'
                    )
                ]), width={"size": 3}, style={'padding': '10px 50px'}),
                dbc.Col(html.Div([
                    html.Label('Colesterol sérico (mg/dL): '),
                    dcc.Input(
                        type="number",
                        debounce=True,
                        value='',
                        id='serum_cholesterol'
                    )
                ]), width={"size": 3}, style={'padding': '10px 90px'}),
                dbc.Col(html.Div([
                    html.Label('Azúcar en sangre en ayunas: '),
                    dcc.Input(
                        type="number",
                        debounce=True,
                        value='',
                        id='fasting_blood_sugar'
                    )
                ]), width={"size": 3}, style={'padding': '10px 10px'}),
            ], style={'padding': '10px 25px'}),
            dbc.Row([
                dbc.Col(html.Div([
                    html.Label('Tipo de dolor en el pecho: '),
                    dcc.Dropdown(
                        options=[
                            {'label': 'Angina típica', 'value': '1'},
                            {'label': 'Angina atípica', 'value': '2'},
                            {'label': 'No anginoso', 'value': '3'},
                            {'label': 'Asintomático', 'value': '4'}
                        ],
                        value='',
                        id='chest_pain_type'
                    )
                ]), width={"size": 3}),
                dbc.Col(html.Div([
                    html.Label('Angina inducida por el ejercicio: '),
                    dcc.Dropdown(
                        options=[
                            {'label': 'Si', 'value': '1'},
                            {'label': 'No', 'value': '0'}
                        ],
                        value='',
                        id='exercise_induced_angina_yes'
                    )
                ]), width={"size": 3}),
            ], style={'padding': '10px 25px'}),
            dbc.Row([html.Div("Resultados ECG",
                              style={'font-weight': 'bold', 'font-size': 16, 'padding': '10px 25px'})]),
            dbc.Row([
                dbc.Col(html.Div([
                    html.Label('Resultados ECG en reposo: '),
                    dcc.Dropdown(
                        options=[
                            {'label': 'Normales', 'value': '0'},
                            {'label': 'Anomalia en la onda ST', 'value': '1'},
                            {'label': 'Hipertrofia ventricular izquierda', 'value': '2'}
                        ],
                        value='',
                        id='resting_ecg'
                    )
                ]), width={"size": 5}),
                dbc.Col(html.Div([
                    html.Label('Depresión del ST: '),
                    dcc.Input(
                        type="number",
                        debounce=True,
                        value='',
                        id='ST_depression_exercise_vs_rest'
                    )
                ]), width={"size": 3}),
                dbc.Col(html.Div([
                    html.Label('Pendiente del segmento ST: '),
                    dcc.Dropdown(
                        options=[
                            {'label': 'Ascendente', 'value': '1'},
                            {'label': 'Plana', 'value': '2'},
                            {'label': 'Descendente', 'value': '3'}
                        ],
                        value='',
                        id='peak_exercise_ST_segment_slope'
                    )
                ]), width={"size": 3}, style={'margin-left': '50px'}),
            ], style={'padding': '10px 25px'}),
            dbc.Row([html.Div("Resultados de la prueba de esfuerzo nuclear.",
                              style={'font-weight': 'bold', 'font-size': 16, 'padding': '10px 25px'})]),
            dbc.Row([
                dbc.Col(html.Div([
                    html.Label('Presencia de talasemia: '),
                    dcc.Dropdown(
                        options=[
                            {'label': 'Normal', 'value': '3'},
                            {'label': 'Defecto fijo', 'value': '6'},
                            {'label': 'Defecto reversible', 'value': '7'}
                        ],
                        value='',
                        id='thallium_stress_test_bf'
                    )
                ]), width={"size": 4}),
                dbc.Col(html.Div([
                    html.Label('Vasos afectados: '),
                    dcc.Dropdown(
                        options=[
                            {'label': '0 vasos coloreados', 'value': '0'},
                            {'label': '1 vasos coloreados', 'value': '1'},
                            {'label': '2 vasos coloreados', 'value': '2'},
                            {'label': '3 vasos coloreados', 'value': '3'}
                        ],
                        value='',
                        id='num_affected_major_vessels'
                    )
                ]), width={"size": 4}),
            ], style={'padding': '10px 25px'}),
        ], style={'padding': '10px 25px'}
        ),

        # Columna de la derecha con la información del riesgo previsto de enfermedad cardíaca
        dbc.Col([

            html.Div("Riesgo previsto de enfermedad cardiaca",
                     style={'font-weight': 'bold', 'font-size': 20}),
            html.Br(),
            html.Div(' '*1000, id='data_patient'),
            html.Br(),
            html.Br(),
            dbc.Button(
                "Predecir Modelo",
                id="collapse-button",
                className="mb-3",
                color='primary',
                n_clicks=0
            ),
            html.Br(),
            dbc.Button(
                'Eliminar inputs',
                id='button_eliminar',
                className="mb-3",
                color='primary',
                n_clicks=0
            ),
            dcc.Graph(id='pie-chart'),
            html.Div(
                id='output2'
            )
        ],
            style={'padding': '10px 25px'}
        ),
    ]),
]
)

# -------------------------------------------------------------------------------------------------------
# Carga de Datos
# -------------------------------------------------------------------------------------------------------

columnas = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
            'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']

df = pd.read_csv("./Data/processed.cleveland.data", names=columnas)

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
# Discretizacion
# ------------

#  Age

df['ageNum'] = df['age']

q1 = df['ageNum'].describe()['25%']
q2 = df['ageNum'].describe()['50%']
q3 = df['ageNum'].describe()['75%']

df.loc[df['ageNum'] < q1, 'age'] = 1
df.loc[(q1 <= df['ageNum']) & (df['ageNum'] < q2), 'age'] = 2
df.loc[(q2 <= df['ageNum']) & (df['ageNum'] < q3), 'age'] = 3
df.loc[(q3 <= df['ageNum']) & (df['ageNum'] < 80), 'age'] = 4

# Trestbps

df['trestbpsNum'] = df['trestbps']

mean = df['trestbps'].mean()

df.loc[df['trestbpsNum'] < mean, 'trestbps'] = 1
df.loc[(mean <= df['trestbpsNum']) & (
    df['trestbpsNum'] < 100000), 'trestbps'] = 2

# Chol

df['cholNum'] = df['chol']

mean = df['chol'].mean()

df.loc[df['cholNum'] < mean, 'chol'] = 1
df.loc[(mean <= df['cholNum']) & (df['cholNum'] < 100000), 'chol'] = 2

# Thalach

df['thalachNum'] = df['thalach']

q1 = df['thalachNum'].describe()['50%']

df.loc[df['thalachNum'] < q1, 'thalach'] = 1
df.loc[(q1 <= df['thalachNum']) & (df['thalachNum'] < 100000), 'thalach'] = 2

# Oldpeak

df['oldpeakNum'] = df['oldpeak']

df.loc[df['oldpeakNum'] < 0.5, 'oldpeak'] = 1
df.loc[(0.5 <= df['oldpeakNum']) & (df['oldpeakNum'] < 1), 'oldpeak'] = 2
df.loc[(1 <= df['oldpeakNum']) & (df['oldpeakNum'] < 1.5), 'oldpeak'] = 3
df.loc[(1.5 <= df['oldpeakNum']) & (df['oldpeakNum'] < 2), 'oldpeak'] = 4
df.loc[(2 <= df['oldpeakNum']) & (df['oldpeakNum'] < 10), 'oldpeak'] = 5

df.oldpeak = df.oldpeak.astype(int)

# ------------
# Drop columns
# ------------
df.drop(['num', 'caNull', 'thalNull', 'ageNum', 'trestbpsNum',
        'cholNum', 'thalachNum', 'oldpeakNum'], axis=1, inplace=True)

# -------------------------------------------------------------------------------------------------------
# Red Bayesiana
# -------------------------------------------------------------------------------------------------------

# Creacion del modelo del grafo

model = BayesianNetwork(
    [
        ('sex', 'thal'),
        ('sex', 'heartdis'),
        ('cp', 'exang'),
        ('exang', 'oldpeak'),
        ('exang', 'thalach'),
        ('slope', 'heartdis'),
        ('slope', 'oldpeak'),
        ('slope', 'thalach'),
        ('ca', 'heartdis'),
        ('thal', 'exang'),
        ('thal', 'heartdis'),
        ('thal', 'oldpeak'),
        ('heartdis', 'cp'),
        ('heartdis', 'oldpeak'),
        ('age', 'ca'),
        ('age', 'thalach'),
        ('age', 'trestbps'),
    ]
)
nodos = list(model.nodes())

# Parametrizacion

model.fit(
    data=df,
    estimator=MaximumLikelihoodEstimator
)

# ------------------------------
# Funciones para discretizar
# ------------------------------


def getAgeDiscrete(age):
    if age < 48:
        return 1
    elif age < 56:
        return 2
    elif age < 61:
        return 3
    else:
        return 4


def getTrestbpsDiscrete(trestbps):
    if trestbps < 131.689769:
        return 1
    else:
        return 2


def getCholDiscrete(chol):
    if chol < 246.693069:
        return 1
    else:
        return 2


def getThalachDiscrete(thalach):
    if thalach < 153:
        return 1
    else:
        return 2


def getOldpeakDiscrete(oldpeak):
    if oldpeak < 0.5:
        return 1
    elif oldpeak < 1:
        return 2
    elif oldpeak < 1.5:
        return 3
    elif oldpeak < 2:
        return 4
    else:
        return 5


# -------------------------------------------------------------------------------------------------------
# Funcion de inferencia
# -------------------------------------------------------------------------------------------------------

def inferenceEvidence(evidence):
    infer = VariableElimination(model)

    prob = infer.query(variables=['heartdis'], evidence=evidence)

    return prob.values.tolist()

# ------------------------------
# Funcion para generar Tablas
# ------------------------------


def generateTable(lineas):
    rows = [html.Tr(linea) for linea in lineas]

    return html.Table(
        rows
    )

# -------------------------------------------------------------------------------------------------------
# Predecir Modelo
# -------------------------------------------------------------------------------------------------------


@app.callback(
    Output('data_patient', 'children'),
    Output('pie-chart', 'figure'),
    State('age', 'value'),
    State('sex_male', 'value'),
    State('resting_bp', 'value'),
    State('maximum_hr', 'value'),
    State('serum_cholesterol', 'value'),
    State('fasting_blood_sugar', 'value'),
    State('chest_pain_type', 'value'),
    State('exercise_induced_angina_yes', 'value'),
    State('resting_ecg', 'value'),
    State('ST_depression_exercise_vs_rest', 'value'),
    State('peak_exercise_ST_segment_slope', 'value'),
    State('thallium_stress_test_bf', 'value'),
    State('num_affected_major_vessels', 'value'),
    Input('collapse-button', 'n_clicks')

)
def generate_matrix(age, sex_male, resting_bp, maximum_hr, serum_cholesterol, fasting_blood_sugar,
                    chest_pain_type, exercise_induced_angina_yes, resting_ecg, ST_depression_exercise_vs_rest,
                    peak_exercise_ST_segment_slope, thallium_stress_test_bf, num_affected_major_vessels, n_clicks):

    # Solo al presionar el botón

    if n_clicks == 0:
        lineas = [
            'Seleccione los datos que conoce del paciente.',
            'Una vez ha llenado los datos conocidos presione el botón -Predecir Modelo-.',
            '-',
            'Nota: No es necesario conocer todos los datos, con al menos uno bastará.'
        ]
        fig = px.pie()
        return generateTable(lineas), fig

    # Crear matriz con datos del usuario

    values = [age, sex_male, resting_bp, maximum_hr, serum_cholesterol, fasting_blood_sugar, chest_pain_type,
              exercise_induced_angina_yes, resting_ecg, ST_depression_exercise_vs_rest, peak_exercise_ST_segment_slope,
              thallium_stress_test_bf, num_affected_major_vessels]

    column_names = ['Edad', 'Sexo', 'Presión arterial', 'Frecuencia cardíaca máxima', 'Colesterol sérico',
                    'Azúcar en sangre en ayunas', 'Tipo de dolor en el pecho', 'Angina inducida por el ejercicio',
                    'Resultados ECG en reposo', 'Depresión del ST', 'Pendiente del segmento ST', 'Presencia de talasemia',
                    'Vasos afectados']

    x_patient = pd.DataFrame(data=[values],
                             columns=column_names)

    matriz = x_patient.to_dict()

    atributos = {
        'age': 'Edad',
        'sex': 'Sexo',
        'cp': 'Tipo de dolor en el pecho',
        'trestbps': 'Presi\u00f3n arterial',
        'chol': 'Colesterol s\u00e9rico',
        'fbs': 'Az\u00facar en sangre en ayunas',
        'restecg': 'Resultados ECG en reposo',
        'thalach': 'Frecuencia card\u00edaca m\u00e1xima',
        'exang': 'Angina inducida por el ejercicio',
        'oldpeak': 'Depresi\u00f3n del ST',
        'slope': 'Pendiente del segmento ST',
        'ca': 'Vasos afectados',
        'thal': 'Presencia de talasemia'
    }

    significado = {
        'age': {
            1: 'Menor a 48',
            2: 'Mayor o igual a 48 y menor de 56',
            3: 'Mayor o igual a 56 y menor de 61',
            4: 'Mayor o igual a 61',
        },
        'sex': {
            0: 'Femenino',
            1: 'Masculino',
        },
        'cp': {
            1: 'Angina típica',
            2: 'Angina atípica',
            3: 'No anginoso',
            4: 'Asintomático',
        },
        'trestbps': {
            1: 'Menor a 131.68 mm Hg',
            2: 'Mayor o igual a 131.68 mm Hg',
        },
        'chol': {
            1: 'Menor a 246.69',
            2: 'Mayor o igual a 246.69',
        },
        'fbs': {
            0: 'Azúcar en sangre en ayunas menor o igual a 120 mg/dl',
            1: 'Azúcar en sangre en ayunas mayor a 120 mg/dl',
        },
        'restecg': {
            0: 'Normal',
            1: 'Anomalia en la onda ST',
            2: 'Hipertrofia Ventricular Izquierda',
        },
        'thalach': {
            1: 'Menor a 153',
            2: 'Mayor o igual a 153',
        },
        'exang': {
            0: 'Angina no producida por ejercicio',
            1: 'Angina producida por ejercicio',
        },
        'oldpeak': {
            1: 'Menor a 0.5',
            2: '0.5 a 1',
            3: '1 a 1.5',
            4: '1.5 a 2',
            5: 'Mayor a 0.5',
        },
        'slope': {
            1: 'Ascendente',
            2: 'Plana',
            3: 'Descendente',
        },
        'ca': {
            0: '0',
            1: '1',
            2: '2',
            3: '3',
        },
        'thal': {
            3: 'Normal',
            6: 'Defecto Fijo',
            7: 'Defecto Reversible',
        },
    }

    resultados = {}
    for atributo in atributos:
        valor = atributos[atributo]
        resultados[atributo] = matriz[valor][0]
    evidence = {k: int(v) for (k, v) in resultados.items()
                if v != '' and v != None}

    for k, v in evidence.items():
        if k == 'age':
            age_discrete = getAgeDiscrete(v)
            evidence[k] = age_discrete
        if k == 'trestbps':
            trestbps_discrete = getTrestbpsDiscrete(v)
            evidence[k] = trestbps_discrete
        if k == 'chol':
            chol_discrete = getCholDiscrete(v)
            evidence[k] = chol_discrete
        if k == 'thalach':
            thalach_discrete = getThalachDiscrete(v)
            evidence[k] = thalach_discrete
        if k == 'oldpeak':
            oldpeak_discrete = getOldpeakDiscrete(v)
            evidence[k] = oldpeak_discrete

    nodos = list(model.nodes())

    evidence = {k: v for (k, v) in evidence.items() if k in nodos}

    # Solo cuando se halla llenado algun dato

    if evidence == {}:
        lineas = [
            'Seleccione los datos que conoce del paciente.',
            'Una vez ha llenado los datos conocidos presione el botón -Predecir Modelo-.',
            '-',
            'Nota: No es necesario conocer todos los datos, con al menos uno bastará.'
        ]
        fig = px.pie()
        return generateTable(lineas), fig

    prob = inferenceEvidence(evidence)

    lineas = [
        'Dados los siguientes parámetros: '
    ] + [f'{k}, con un valor de {significado[k][v]}' for (k, v) in evidence.items()] + [
        '-',
        f'La probabilidad de que el paciente tenga una enfermedad cardíaca es {round(prob[1], 2)}'
    ]

    if pd.isna(prob[1]):
        lineas = [
            'Dados los siguientes parámetros: '
        ] + [f'{k}, con un valor de {significado[k][v]}' for (k, v) in evidence.items()] + [
            '-',
            f'La probabilidad de que el paciente tenga una enfermedad cardíaca no es posible calcularla ya que no hay suficientes datos'
        ]

    # Grafico
    df_graph = pd.DataFrame(
        {'label': ['No Tiene Enfermedad', 'Tiene Enfermedad'], 'prob': prob})
    fig = px.pie(df_graph, names='label', values='prob',
                 title='Probabilidad Enfermedad Cardíaca')

    return generateTable(lineas), fig


# -------------------------------------------------------------------------------------------------------
# Borrar
# -------------------------------------------------------------------------------------------------------

@app.callback(Output('age', 'value'),
              Output('sex_male', 'value'),
              Output('resting_bp', 'value'),
              Output('maximum_hr', 'value'),
              Output('serum_cholesterol', 'value'),
              Output('fasting_blood_sugar', 'value'),
              Output('chest_pain_type', 'value'),
              Output('exercise_induced_angina_yes', 'value'),
              Output('resting_ecg', 'value'),
              Output('ST_depression_exercise_vs_rest', 'value'),
              Output('peak_exercise_ST_segment_slope', 'value'),
              Output('thallium_stress_test_bf', 'value'),
              Output('num_affected_major_vessels', 'value'),
              [Input('button_eliminar', 'n_clicks')])
def clear_inputs(n_clicks):

    if n_clicks is not None:
        return '', '', '', '', '', '', '', '', '', '', '', '', ''


@app.callback(Output('output2', 'children'),
              [Input('button_eliminar', 'n_clicks')])
def clear_output(n_clicks):
    if n_clicks == 0:
        return ''
