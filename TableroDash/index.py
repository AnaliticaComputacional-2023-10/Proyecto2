# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# LIBRARIES
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

from app import app
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from pages import inicio, instrucciones, programa, graficas

url_contente_layout = html.Div(children=[
    dcc.Location(id="url", refresh=False),
    html.Div(id="output-div")
])

app.layout = url_contente_layout

app.validation_layout = html.Div([
    url_contente_layout,
    inicio.inicio_layout,
    graficas.graficas_layout,
    instrucciones.instrucciones_layout,
    programa.programa_layout
])


@app.callback(Output(component_id='output-div', component_property='children'),
              [Input(component_id='url', component_property='pathname')])
def update_output_div(pathname):
    if pathname == '/instrucciones':
        return instrucciones.instrucciones_layout
    elif pathname == '/graficas':
        return graficas.graficas_layout
    elif pathname == '/programa':
        return programa.programa_layout
    else:
        return inicio.inicio_layout


if __name__ == "__main__":
    app.run_server(debug=True)
