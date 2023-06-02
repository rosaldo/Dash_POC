#!/usr/bin/env python3
# coding: utf-8

import random

import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash_extensions.javascript import Namespace

from dash import Dash, html

# Create some markers.
points = [
    dict(lat=55.5 + random.random(), lon=9.5 + random.random(), value=random.random())
    for i in range(100)
]
data = dlx.dicts_to_geojson(points)

# Create geojson.
ns = Namespace("myNamespace", "mySubNamespace")
geojson = dl.GeoJSON(data=data, options=dict(pointToLayer=ns("pointToLayer")))

# Create the app.
app = Dash()
app.layout = html.Div(
    [
        dl.Map([dl.TileLayer(), geojson], center=(56, 10), zoom=8, style={"height": "97vh"}),
    ]
)

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
