#!/usr/bin/env python3
# coding: utf-8


import clipboard as cb

from dash import Dash, Input, Output, State, dcc, html

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Button("Copiar para Área de Transferência", id="copy-button"),
        html.Br(),
        dcc.Textarea(id="input-text", placeholder="Digite o texto aqui"),
        html.Br(),
        dcc.Input(placeholder="Cole aqui!"),
        html.Br(),
        html.Div(id="output-div"),
    ],
)

@app.callback(
    [Output("output-div", "children")],
    [Input("copy-button", "n_clicks")],
    [State("input-text", "value")]
)
def copy_to_clipboard(n_clicks, input_text):
    if input_text:
        cb.copy(input_text)
        return [["O texto ",
                 html.B(input_text),
                 " foi copiado com sucesso. Use CTRL+V para colar."]]
    else:
        return [""]

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
