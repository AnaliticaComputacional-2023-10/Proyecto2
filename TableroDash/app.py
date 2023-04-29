import dash
import dash_bootstrap_components as dbc
#from dash import html
#from dash import dcc
#from dash.dependencies import Input, Output #callback

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY])
server = app.server

#url_contente_layout = html.Div(children=[
#    dcc.Location(id="url",refresh=False),
#    html.Div(id="output-div")
#])

#app.layout = url_contente_layout

#inicio_layout = html.Div(children=[
#    html.H1(children = "Bienvenido al Programa de Predicción de Enfermedades Cardíacas"),
#    dcc.Link('Inicio',href="/"),
#    html.Br(),
#    dcc.Link('Instrucciones',href="/instrucciones"),
#    html.Br(),
#    dcc.Link('Programa',href="/programa")
#])

#instrucciones_layout = html.Div(children=[
#    html.H1(children = "Aca encontrara las instrucciones para utilizar la aplicación"),
#    dcc.Link('Inicio',href="/"),
#    html.Br(),
#    dcc.Link('Programa',href="/programa")
#])

#programa_layout =html.Div(children=[
#    html.H1(children = "Aca encontrara la aplicación"),
#    dcc.Link('Inicio',href="/"),
#    html.Br(),
#    dcc.Link('Instrucciones',href="/instrucciones")
#])

#app.validation_layout = html.Div([
#    url_contente_layout,
#    inicio_layout,
#    instrucciones_layout,
#    programa_layout
#])

#@app.callback(Output(component_id='output-div', component_property='children'),
#              [Input(component_id='url', component_property='pathname')])
#def update_output_div(pathname):
#    if pathname == '/instrucciones':
#        return instrucciones_layout
#    elif pathname == '/programa':
#        return programa_layout
#    else:
#        return inicio_layout

#if __name__ == "__main__":
#    app.run_server(debug=True)
