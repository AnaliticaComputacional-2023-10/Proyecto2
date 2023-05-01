# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# LIBRARIES
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
from apps import navigation
from app import app
import dash_bootstrap_components as dbc
import pandas as pd
from pgmpy.inference import VariableElimination
import plotly.express as px
from pgmpy.readwrite import BIFReader


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# LAYOUT
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

programa_layout = html.Div(children=[

    # ------------------------------------------------
    # Barra de Navegacion
    # ------------------------------------------------

    navigation.navbar,
    html.Br(),

    # ------------------------------------------------
    # Titulo de la pagina
    # ------------------------------------------------

    html.H1(children="Programa de Predicción de Enfermedades Cardíacas",
            style={'textAlign': 'center'}),
    html.Br(),

    # ------------------------------------------------
    # Inicio Inputs Outpus
    # ------------------------------------------------

    dbc.Row([

        # ------------------------------------------------
        # Columna Inputs
        # ------------------------------------------------

        dbc.Col([html.Div("Información del Paciente",
                          style={'font-weight': 'bold', 'font-size': 20}),

            # ------------------------------------------------
                 # Datos Demograficos
                 # ------------------------------------------------

                 dbc.Row([html.Div("Datos demográficos del paciente",
                                   style={'font-weight': 'bold', 'font-size': 16, 'padding': '10px 25px'})]),

                 dbc.Row([

                     # ------------------------------------------------
                     # Edad Paciente
                     # ------------------------------------------------

                     dbc.Col(html.Div([
                         html.Label('Edad del paciente (en años): '),
                         dcc.Input(
                             type="number",
                             debounce=True,
                             value='',
                             id='age'
                         )
                     ]), width={"size": 3}),

                     # ------------------------------------------------
                     # Sexo
                     # ------------------------------------------------

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

                 # ------------------------------------------------
                 # Salud del paciente
                 # ------------------------------------------------

                 dbc.Row([html.Div("Salud del paciente",
                                   style={'font-weight': 'bold', 'font-size': 16, 'padding': '10px 25px'})]),
                 dbc.Row([

                     # ------------------------------------------------
                     # Presion Arterial
                     # ------------------------------------------------

                     dbc.Col(html.Div([
                         html.Label('Presión arterial (mmHg): '),
                         dcc.Input(
                             type="number",
                             debounce=True,
                             value='',
                             id='resting_bp'
                         )
                     ]), width={"size": 3}, style={'padding': '10px 10px'}),

                     # ------------------------------------------------
                     # Frecuencia Cardiaca
                     # ------------------------------------------------

                     dbc.Col(html.Div([
                         html.Label('Frecuencia cardíaca máxima (bpm): '),
                         dcc.Input(
                             type="number",
                             debounce=True,
                             value='',
                             id='maximum_hr'
                         )
                     ]), width={"size": 3}, style={'padding': '10px 50px'}),

                     # ------------------------------------------------
                     # Colesterol Serico
                     # ------------------------------------------------

                     dbc.Col(html.Div([
                         html.Label('Colesterol sérico (mg/dL): '),
                         dcc.Input(
                             type="number",
                             debounce=True,
                             value='',
                             id='serum_cholesterol'
                         )
                     ]), width={"size": 3}, style={'padding': '10px 90px'}),

                     # ------------------------------------------------
                     # Azucar Sangre
                     # ------------------------------------------------

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

                     # ------------------------------------------------
                     # Tipo Dolor Pecho
                     # ------------------------------------------------

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

                     # ------------------------------------------------
                     # Angina Ejercicio
                     # ------------------------------------------------

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

                 # ------------------------------------------------
                 # Resultados ECG
                 # ------------------------------------------------

                 dbc.Row([html.Div("Resultados ECG",
                                   style={'font-weight': 'bold', 'font-size': 16, 'padding': '10px 25px'})]),
                 dbc.Row([

                     # ------------------------------------------------
                     # Resultados ECG Reposo
                     # ------------------------------------------------

                     dbc.Col(html.Div([
                         html.Label('Resultados ECG en reposo: '),
                         dcc.Dropdown(
                             options=[
                                 {'label': 'Normales', 'value': '0'},
                                 {'label': 'Anomalia en la onda ST', 'value': '1'},
                                 {'label': 'Hipertrofia ventricular izquierda',
                                     'value': '2'}
                             ],
                             value='',
                             id='resting_ecg'
                         )
                     ]), width={"size": 5}),

                     # ------------------------------------------------
                     # Depresion Segmento ST
                     # ------------------------------------------------

                     dbc.Col(html.Div([
                         html.Label('Depresión del ST: '),
                         dcc.Input(
                             type="number",
                             debounce=True,
                             value='',
                             id='ST_depression_exercise_vs_rest'
                         )
                     ]), width={"size": 3}),

                     # ------------------------------------------------
                     # Pendiente Segmento ST
                     # ------------------------------------------------

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

                 # ------------------------------------------------
                 # Prueba Esfuerzo Nuclear
                 # ------------------------------------------------

                 dbc.Row([html.Div("Resultados de la prueba de esfuerzo nuclear.",
                                   style={'font-weight': 'bold', 'font-size': 16, 'padding': '10px 25px'})]),
                 dbc.Row([

                     # ------------------------------------------------
                     # Talasemia
                     # ------------------------------------------------

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

                     # ------------------------------------------------
                     # Vasos Afectados
                     # ------------------------------------------------

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

        # ------------------------------------------------
        # Columna Outputs
        # ------------------------------------------------


        dbc.Col([

            # ------------------------------------------------
            # Texto Descripcion Paciente
            # ------------------------------------------------

            html.Div("Riesgo previsto de enfermedad cardiaca",
                     style={'font-weight': 'bold', 'font-size': 20}),
            html.Br(),
            html.Div(' '*1000, id='data_patient'),
            html.Br(),
            html.Br(),

            # ------------------------------------------------
            # Boton Predecir Modelo
            # ------------------------------------------------

            dbc.Button(
                "Predecir Modelo",
                id="collapse-button",
                className="mb-3",
                color='primary',
                n_clicks=0
            ),
            html.Br(),

            # ------------------------------------------------
            # Boton Eliminar Inputs
            # ------------------------------------------------

            dbc.Button(
                'Eliminar inputs',
                id='button_eliminar',
                className="mb-3",
                color='primary',
                n_clicks=0
            ),

            # ------------------------------------------------
            # Grafica
            # ------------------------------------------------

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

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# LOAD THE MODEL
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

reader = BIFReader('./Data/Models/Original.bif')
model = reader.get_model()
model.check_model()

nodos = list(model.nodes)

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# FUNCTIONS THAT HELP
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------
# Funciones para discretizar los datos del usuario
# ------------------------------------------------

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


# ------------------------------------------------
# Funcion para Inferir
# ------------------------------------------------

def inferenceEvidence(evidence, model):
    infer = VariableElimination(model)
    prob = infer.query(variables=['heartdis'], evidence=evidence)

    return prob.values.tolist()


# ------------------------------------------------
# Funcion para generar Tablas
# ------------------------------------------------

def generateTable(lineas):
    rows = [html.Tr(linea) for linea in lineas]

    return html.Table(rows)


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# CONSTANTES
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------
# Dictionary of variables meaning
# ------------------------------------------------

atributos = {
    'age': 'Edad',
    'sex': 'Sexo',
    'cp': 'Tipo de dolor en el pecho',
    'trestbps': 'Presión arterial',
    'chol': 'Colesterol sérico',
    'fbs': 'Azúcar en sangre en ayunas',
    'restecg': 'Resultados ECG en reposo',
    'thalach': 'Frecuencia cardíadaca máxima',
    'exang': 'Angina inducida por el ejercicio',
    'oldpeak': 'Depresión del ST',
    'slope': 'Pendiente del segmento ST',
    'ca': 'Vasos afectados',
    'thal': 'Presencia de talasemia'
}

# ------------------------------------------------
# Dictionary of variables values interpretation
# ------------------------------------------------

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


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# INFERENCE
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

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
    Input('collapse-button', 'n_clicks'))
def generate_matrix(age, sex_male, resting_bp, maximum_hr, serum_cholesterol, fasting_blood_sugar,
                    chest_pain_type, exercise_induced_angina_yes, resting_ecg, ST_depression_exercise_vs_rest,
                    peak_exercise_ST_segment_slope, thallium_stress_test_bf, num_affected_major_vessels, n_clicks):

    # ------------------------------------------------
    # Mensaje Introduccion Usuario
    # ------------------------------------------------

    if n_clicks == 0:
        lineas = [
            'Seleccione los datos que conoce del paciente.',
            'Una vez ha llenado los datos conocidos presione el botón -Predecir Modelo-.',
            '-',
            'Nota: No es necesario conocer todos los datos, con al menos uno bastará.'
        ]
        fig = px.pie()

        return generateTable(lineas), fig

    # ------------------------------------------------
    # Dictionary of variables values
    # ------------------------------------------------

    valores = {
        'age': age,
        'sex': sex_male,
        'cp': chest_pain_type,
        'trestbps': resting_bp,
        'chol': serum_cholesterol,
        'fbs': fasting_blood_sugar,
        'restecg': resting_ecg,
        'thalach': maximum_hr,
        'exang': exercise_induced_angina_yes,
        'oldpeak': ST_depression_exercise_vs_rest,
        'slope': peak_exercise_ST_segment_slope,
        'ca': num_affected_major_vessels,
        'thal': thallium_stress_test_bf,
    }

    # ------------------------------------------------
    # Dictionary of variable values filtered by not empty
    # ------------------------------------------------

    valores_filtrados = {key: value
                         for (key, value) in valores.items()
                         if value != '' and value is not None}

    # ------------------------------------------------
    # Dictionary of variable values discretized
    # ------------------------------------------------

    discrete_valores = valores_filtrados.copy()

    for k, v in valores_filtrados.items():
        if k == 'age':
            age_discrete = getAgeDiscrete(v)
            discrete_valores[k] = age_discrete
        if k == 'trestbps':
            trestbps_discrete = getTrestbpsDiscrete(v)
            discrete_valores[k] = trestbps_discrete
        if k == 'chol':
            chol_discrete = getCholDiscrete(v)
            discrete_valores[k] = chol_discrete
        if k == 'thalach':
            thalach_discrete = getThalachDiscrete(v)
            discrete_valores[k] = thalach_discrete
        if k == 'oldpeak':
            oldpeak_discrete = getOldpeakDiscrete(v)
            discrete_valores[k] = oldpeak_discrete

    # ------------------------------------------------
    # Filter the evidence with the nodes of the model
    # ------------------------------------------------

    discrete_valores_nodes = {key: value
                              for (key, value) in discrete_valores.items()
                              if key in nodos}

    # ------------------------------------------------
    # Filter the evidence with the nodes of the model
    # ------------------------------------------------

    evidence = {key: str(value)
                for (key, value) in discrete_valores_nodes.items()}

    print(evidence)

    # ------------------------------------------------
    # Sin evidencia, no se hace inferencia
    # ------------------------------------------------

    if evidence == {}:
        lineas = [
            'Seleccione los datos que conoce del paciente.',
            'Una vez ha llenado los datos conocidos presione el botón -Predecir Modelo-.',
            '-',
            'Nota: No es necesario conocer todos los datos, con al menos uno bastará.'
        ]
        fig = px.pie()

        return generateTable(lineas), fig

    # ------------------------------------------------
    # Inferencia con la evidencia
    # ------------------------------------------------

    try:
        prob = inferenceEvidence(evidence, model)

    except:
        prob = None

    print(prob)

    # ------------------------------------------------
    # Error en la inferencia
    # ------------------------------------------------

    if prob is None:
        lineas = [
            'Dados los siguientes parámetros: '
        ] + [
            f'{atributos[key]}: {significado[key][int(value)]}'
            for (key, value) in evidence.items()
        ] + [
            '-',
            f'La probabilidad de que el paciente tenga una enfermedad cardíaca no es posible calcularla ya que no hay suficientes datos'
        ]
        fig = px.pie()

        return generateTable(lineas), fig

    # ------------------------------------------------
    # Mensaje Resultado Usuario
    # ------------------------------------------------

    lineas = [
        'Dados los siguientes parámetros: '
    ] + [
        f'{atributos[key]}: {significado[key][int(value)]}'
        for (key, value) in evidence.items()
    ] + [
        '-',
        f'La probabilidad de que el paciente tenga una enfermedad cardíaca es: {round(prob[1], 2)}'
    ]

    # ------------------------------------------------
    # Grafico
    # ------------------------------------------------

    df_graph = pd.DataFrame(
        {
            'Tiene Enfermedad': [prob[1]],
            'No Tiene Enfermedad': [prob[0]],
        }
    )

    fig = px.bar(
        data_frame=df_graph,
        x=['Tiene Enfermedad', 'No Tiene Enfermedad'],
        orientation='h',
        barmode='stack',
        title='Probabilidad del Paciente de Tener Enfermedad Cardíaca',
        color_discrete_sequence=['#F97B72', '#80B1D3'],
    )

    fig.update_yaxes(
        showticklabels=False,
        title_text='',
    )

    fig.update_xaxes(
        title_text='Probability',
    )

    fig.update_layout(
        legend_title='',
        legend=dict(
            yanchor="top",
            y=1.15,
            xanchor="left",
            x=0.1
        ),
        height=400,
    )

    return generateTable(lineas), fig


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# CLEAR
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------
# Clear Inputs
# ------------------------------------------------

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


# ------------------------------------------------
# Clear Output
# ------------------------------------------------

@app.callback(Output('output2', 'children'),
              [Input('button_eliminar', 'n_clicks')])
def clear_output(n_clicks):
    if n_clicks == 0:
        return ''
