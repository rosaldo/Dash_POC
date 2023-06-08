#!/usr/bin/env python3
# coding: utf-8

from dash import ClientsideFunction, Dash, Input, Output, State, dcc, html
from dash_table import DataTable as dtt

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Web App com Armazenamento Local usando IndexedDB"),
    dcc.Input(id="input_dados", type="text", placeholder="Digite os dados"),
    
    html.Button("Salvar", id="botao_salvar", n_clicks=0),
    html.Div(id="mensagem"),
    
    html.Button("Mostrar Dados", id="botao_mostrar", n_clicks=0),
    dtt(id="dados_salvos"),
])

app.clientside_callback(
    ClientsideFunction(
        namespace="clientside",
        function_name="salvar_dados"
    ),
    Output("mensagem", "children"),
    Input("botao_salvar", "n_clicks"),
    State("input_dados", "value"),
    prevent_initial_call=True
)

app.clientside_callback(
    ClientsideFunction(
        namespace="clientside",
        function_name="obter_dados"
    ),
    Output("dados_salvos", "data"),
    Input("botao_mostrar", "n_clicks"),
    prevent_initial_call=True
)



if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
