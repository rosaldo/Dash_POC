#!/usr/bin/env python3
# coding: utf-8

import dash_leaflet as dl
from dash import Dash

app = Dash()
app.layout = dl.Map(dl.TileLayer(), style={"width": "100hw", "height": "97vh"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)

