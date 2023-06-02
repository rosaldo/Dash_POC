#!/usr/bin/env python3
# coding: utf-8

import plotly.express as px

from dash import Dash, dcc

app = Dash(__name__)

df = px.data.carshare()

fig = px.scatter_mapbox(
    data_frame=df,
    mapbox_style="open-street-map",
    title="POC: Car Share Scatter Map",
    lon=df["centroid_lon"],
    lat=df["centroid_lat"],
    color=df["peak_hour"],
    size=df["car_hours"],
    height=600,
)

app.layout = dcc.Graph(figure=fig)

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)

