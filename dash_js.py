#!/usr/bin/env python3
# coding: utf-8

from dash import ClientsideFunction, Dash, Input, Output, html

app = Dash(__name__)

app.layout = html.Div(
    html.Center(
        [
            html.H1("Exemplo de Execução de Código JavaScript usando clientside_callback"),
            html.Button('Clique aqui', id='botao-clique', n_clicks=0),
            html.H2(id='resultado', style={"margin-top":"50px"})
        ]
    )
)

app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='executar_codigo'
    ),
    Output('resultado', 'children'),
    Input('botao-clique', 'n_clicks')
)

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
