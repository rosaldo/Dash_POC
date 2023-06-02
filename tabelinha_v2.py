#!/usr/bin/env python3
# coding: utf-8

import pandas as pd

from dash import Dash, dash_table, html

df = pd.DataFrame(
    {
        "Date": ["2018-08-30 22:52:25", "2021-09-29 13:33:49"],
        "Ticket ID": [1444008, 1724734],
        "Work Order": ["119846184", "122445397"],
        "Link(s)": [
            "[Google](https://www.google.com)",
            "[Twitter](https://www.twitter.com), [Facebook](https://www.facebook.com)",
        ],
    }
)

app = Dash()

app.layout = html.Div(
    children=[
        dash_table.DataTable(
            data=df.to_dict(orient="records"),
            columns=[
                {"id": x, "name": x, "presentation": "markdown"}
                if x == "Link(s)"
                else {"id": x, "name": x}
                for x in df.columns
            ],
        ),
        html.Div(style={"height": "10px"}),
        dash_table.DataTable(
            columns=[
                {"name": "link", "id": "link", "presentation": "markdown"},
                {"name": "botao", "id": "botao", "presentation": "markdown"},
            ],
            data=[
                {
                    "link": "<a href='https://www.google.com'>Google</a>",
                    "botao": "<button>Botão</button>",
                }
            ],
            markdown_options={"html": True},
        ),
    ]
)

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)

