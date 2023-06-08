#!/usr/bin/env python3
# coding: utf-8

import uuid

from dash import Dash, Input, Output, State, dash_table, dcc, html
import dash_bootstrap_components as dbc

app = Dash(__name__)

app.layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Row(
            children=[
                dcc.Store(id="db", storage_type="local"),
                html.H1(
                    style={"text-align":"center"},
                    children="Web App com Armazenamento Local"
                )
            ]
        ),
        dbc.Row(
            style={"display":"flex", "flexDirection":"row"},
            children=[
                dbc.Col(
                    children=[
                        dbc.Input(id="input_dados", type="text", placeholder="Digite os dados")
                    ]
                ),
                dbc.Col(
                    children=[
                        dbc.Button("Salvar", id="botao_salvar")
                    ]
                ),
                dbc.Col(
                    children=[
                        html.Div(id="mensagem")
                    ]
                )
            ]
        ),
        dbc.Row(
            style={"display":"flex", "flexDirection":"row"},
            children=[
                dbc.Col(
                    children=[
                        dbc.Button("Mostrar Dados", id="botao_mostrar")
                    ]
                ),
                dbc.Col(
                    children=[
                        dbc.Button("Excluir Dados", id="botao_excluir")
                    ]
                )
            ]
        ),
        dbc.Row(
            justify="center",
            children=[
                dash_table.DataTable(id="dados_salvos")
            ]
        )
    ]
)

@app.callback(
    [
        Output("db", "data"),
        Output("dados_salvos", "data"),
        Output("input_dados", "value"),
        Output("mensagem", "children"),
    ],
    [
        Input("botao_salvar", "n_clicks"),
    ],
    [
        State("db", "data"),
        State("input_dados", "value"),
        State("dados_salvos", "data"),
    ],
    prevent_initial_call=True
)
def salvar_dados(bt_click, db, value, data):
    if not db:
        db = list()
    new = dict(uuid=uuid.uuid4().hex, value=value)
    db.append(new)
    if data:
        new_data = db
    else:
        new_data = []
    return [db, new_data, "", new.__str__()]

@app.callback(
    [
        Output("dados_salvos", "data", allow_duplicate=True),
        Output("botao_mostrar", "children"),
    ],
    [
        Input("botao_mostrar", "n_clicks"),
    ],
    [
        State("db", "data"),
    ],
    prevent_initial_call=True
)
def mostrar_dados(bt_click, data):
    if bt_click % 2 == 1:
        return [data, "Ocultar Dados"]
    else:
        return [[], "Mostrar Dados"]

@app.callback(
    [
        Output("db", "data", allow_duplicate=True),
        Output("dados_salvos", "data", allow_duplicate=True),
    ],
    [
        Input("botao_excluir", "n_clicks"),
    ],
    prevent_initial_call=True
)
def excluir_dados(bt_click):
    return [list(), []]


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
