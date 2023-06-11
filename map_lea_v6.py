#!/usr/bin/env python3
# coding: utf-8

import dash_leaflet as dl
from dash import Dash

app = Dash()

# Defina o layout do aplicativo
app.layout = dl.Map(
    style={"width": "100hw", "height": "98vh"},
    center=[-23.5505, -46.6333],
    zoom=15,
    children=[
        dl.TileLayer(),
        dl.Marker(
            children=[
                dl.Tooltip("Alerta"),
                dl.Popup("Precisa de atenção!")
            ],
            icon={"iconUrl":"./assets/pin-fill-orange.svg"},
            position=[-23.5505, -46.6333],
            riseOnHover=True,
        ),
        dl.Marker(
            children=[
                dl.Tooltip("Ativo"),
                dl.Popup("Tudo funcionando!")
            ],
            icon={"iconUrl":"./assets/pin-fill-green.svg"},
            position=[-23.555, -46.635],
            riseOnHover=True,
        ),
        dl.Marker(
            children=[
                dl.Tooltip("Desativado"),
                dl.Popup("Tudo desligado!")
            ],
            icon={"iconUrl":"./assets/pin-fill-black.svg"},
            position=[-23.56, -46.64],
            riseOnHover=True,
        ),
        dl.Marker(
            children=[
                dl.Tooltip("Pane Catastrofica"),
                dl.Popup("Precisa de uma ação urgente!")
            ],
            icon={"iconUrl":"./assets/pin-fill-red.svg"},
            position=[-23.565, -46.645],
            riseOnHover=True,
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(host="127.0.0.1", debug=True)
