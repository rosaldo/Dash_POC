#!/usr/bin/env python3
# coding: utf-8

import numpy as np
import plotly.graph_objs as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd

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
    html.H1("POC de Tabulação"),
    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='Gráfico', value='tab-1'),
        dcc.Tab(label='Dados', value='tab-2'),
    ]),
    html.Div(id='tab-content')
])

@app.callback(
    Output('tab-content', 'children'),
    Input('tabs', 'value')
)
def render_content(tab):
    if tab == 'tab-1':
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
    elif tab == 'tab-2':
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
