#!/usr/bin/env python3
# coding: utf-8

import dash_bootstrap_components as dbc
from dash_tabulator import DashTabulator

from dash import Dash, Input, Output, html

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)


app.layout = html.Div(
    children=[
        DashTabulator(
            id="tabelinha",
            columns=[
                {"title": "Nome", "field": "nome", "editor": "input"},
                {"title": "Cel", "field": "cel", "editor": "input"},
            ],
            data=[
                {"id": "1", "nome": "primeiro", "cel": "123456"},
                {"id": "2", "nome": "segundo", "cel": "23452345"},
                {"id": "3", "nome": "terceiro", "cel": "252"},
                {"id": "4", "nome": "quarto", "cel": "2345234523"},
                {"id": "5", "nome": "quinto", "cel": "567858"},
                {"id": "6", "nome": "sexto", "cel": "9679879"},
                {"id": "7", "nome": "[Twitter](https://www.twitter.com)", "cel": "2828476946"},
            ],
        ),
        html.Div(id="saida"),
    ]
)


@app.callback(
    Output("saida", "children"),
    Input("tabelinha", "cellEdited"),
)
def saida(valor):
    return f"{valor}"


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)

