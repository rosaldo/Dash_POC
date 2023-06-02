#!/usr/bin/env python3
# coding: utf-8

import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash import Dash

app = Dash()
app.layout = dl.Map(
    center=(-12.862, -50.510),
    zoom=4,
    style={"width": "100hw", "height": "97vh"},
    children=[
        dl.TileLayer(),
        dl.GeoJSON(
            data=dlx.dicts_to_geojson([{"lat": -12.862, "lon": -50.510}]),
            options={"style": {"color": "red"}},
        ),
    ],
)

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)

