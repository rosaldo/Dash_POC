#!/usr/bin/env python3
# coding: utf-8

import dash_leaflet as dl
from dash import Dash, Input, Output, html

app = Dash(prevent_initial_callbacks=True)
app.layout = html.Div(
    [
        dl.Map(
            [dl.TileLayer(), dl.LayerGroup(id="layer")],
            id="map",
            style={"width": "100hw", "height": "97vh", "margin": "auto", "display": "block"},
        ),
    ]
)


@app.callback(Output("layer", "children"), [Input("map", "click_lat_lng")])
def map_click(click_lat_lng):
    return [
        dl.Marker(
            # position=click_lat_lng, children=dl.Tooltip("({:.3f}, {:.3f})".format(*click_lat_lng))
            position=click_lat_lng,
            children=dl.Tooltip(f"{click_lat_lng}"),
        )
    ]


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
