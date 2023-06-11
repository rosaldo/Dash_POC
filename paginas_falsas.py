#!/usr/bin/env python3
# coding: utf-8

import numpy as np
import pandas as pd
import plotly.graph_objs as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

# Inicialize o aplicativo Dash
app = Dash(__name__)

# Dados aleatórios
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = np.random.randn(100)

# DataFrame de exemplo
df = pd.DataFrame({'x': x, 'y': y})

# Defina o layout do aplicativo
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.H1("POC Páginas Falsas"),
    dcc.Link('Gráfico', href='/graph'),
    html.Br(),
    dcc.Link('Dados', href='/data'),
    html.Br(),
    html.Div(id='page-content')
])

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def render_page_content(pathname):
    if pathname == '/graph':
        return dcc.Graph(
            id='graph',
            figure={
                'data': [
                    go.Scatter(
                        x=df['x'],
                        y=df['y'],
                        mode='lines',
                        name='Dados Aleatórios'
                    )
                ],
                'layout': go.Layout(
                    title='Gráfico de Linhas',
                    xaxis={'title': 'Eixo X'},
                    yaxis={'title': 'Eixo Y'},
                    hovermode='closest'
                )
            }
        )
    elif pathname == '/data':
        return html.Div([
            html.H3('Dados'),
            html.Table([
                html.Thead(html.Tr([
                    html.Th('Índice'),
                    html.Th('X'),
                    html.Th('Y')
                ])),
                html.Tbody([
                    html.Tr([
                        html.Td(index),
                        html.Td(row['x']),
                        html.Td(row['y'])
                    ]) for index, row in df.iterrows()
                ])
            ])
        ])

# Execute o aplicativo
if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
