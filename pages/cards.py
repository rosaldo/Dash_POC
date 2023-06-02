#!/usr/bin/env python3
# coding: utf-8

import dash
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(__name__, path_template="/cards")


def layout():
    card = dbc.Card([dbc.CardHeader("Header"), dbc.CardBody("Body")])
    graph_card = dbc.Card([dbc.CardHeader("Here's a graph"), dbc.CardBody("An amazing graph")])
    return dbc.Container(
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card([card] * 4, style={"height": "250px"}),
                        html.H2("Based on forecase done an approximate amount..."),
                        dbc.Card([graph_card] * 2, style={"height": "400px"}),
                    ],
                    width=8,
                ),
                dbc.Col(
                    dbc.Card(
                        [dbc.CardHeader("Header"), dbc.CardBody("Body")],
                        className="h-100",
                    ),
                    width=2,
                ),
            ],
            justify="center",
        ),
        fluid=True,
        className="mt-3",
    )
