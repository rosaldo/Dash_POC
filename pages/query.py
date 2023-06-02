#!/usr/bin/env python3
# coding: utf-8

import dash
from dash import html

dash.register_page(__name__, path_template="/report/<id>")


def layout(id=None):
    return html.Div(f"The user requested report ID: {id}.")
