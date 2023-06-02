#!/usr/bin/env python3
# coding: utf-8

from dash import Dash, Input, Output, dcc, html

app = Dash(__name__)


app.layout = html.Div(
    dcc.Input(
        id="tel",
        type="tel",
        pattern="^([(]\d{2}[)] [\d{1}]?\d{4}[-]\d{4})$",
    )
)


@app.callback(
    [
        Output("tel", "value"),
    ],
    [
        Input("tel", "value"),
    ],
)
def set_mask_tel(value):
    return [value]


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)

