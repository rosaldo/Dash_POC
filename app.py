#!/usr/bin/env python3
# coding: utf-8

import dash_bootstrap_components as dbc

import dash
from dash import Dash, Input, Output, dcc, html

# initialize your dash app as normal
app = Dash(
    __name__,
    use_pages=True,
    # bootstrap css
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    # 3rd party js to export as xlsx
    external_scripts=["https://oss.sheetjs.com/sheetjs/xlsx.full.min.js"],
)

app.layout = html.Div(
    [
        html.H1("Multi-page app with Dash Pages"),
        html.Div(
            [
                html.Div(dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"]))
                for page in dash.page_registry.values()
            ]
        ),
        html.Div(),
        dash.page_container,
    ]
)

# Setup some columns
# This is the same as if you were using tabulator directly in js
# Notice the column with "editor": "input" - these cells can be edited
# See tabulator editor for options http://tabulator.info/docs/4.8/edit
columns = [
    {"title": "Name", "field": "name", "width": 150, "headerFilter": True, "editor": "input"},
    {"title": "Age", "field": "age", "hozAlign": "left", "formatter": "progress"},
    {"title": "Favourite Color", "field": "col", "headerFilter": True},
    {"title": "Date Of Birth", "field": "dob", "hozAlign": "center"},
    {"title": "Rating", "field": "rating", "hozAlign": "center", "formatter": "star"},
    {"title": "Passed?", "field": "passed", "hozAlign": "center", "formatter": "tickCross"},
]

# Setup some data
data = [
    {"id": 1, "name": "Oli Bob", "age": "12", "col": "red", "dob": ""},
    {"id": 2, "name": "Mary May", "age": "1", "col": "blue", "dob": "14/05/1982"},
    {"id": 3, "name": "Christine Lobowski", "age": "42", "col": "green", "dob": "22/05/1982"},
    {"id": 4, "name": "Brendon Philips", "age": "125", "col": "orange", "dob": "01/08/1980"},
    {"id": 5, "name": "Margret Marmajuke", "age": "16", "col": "yellow", "dob": "31/01/1999"},
    {
        "id": 6,
        "name": "Fred Savage",
        "age": "16",
        "col": "yellow",
        "rating": "1",
        "dob": "31/01/1999",
    },
    {
        "id": 7,
        "name": "Brie Larson",
        "age": "30",
        "col": "blue",
        "rating": "1",
        "dob": "31/01/1999",
    },
]

# dash_tabulator can be populated from a dash callback
@app.callback(
    [Output("tabulator", "columns"), Output("tabulator", "data")],
    [Input("interval-component-iu", "n_intervals")],
)
def initialize(val):
    return columns, data


# dash_tabulator can register a callback on rowClicked,
# cellEdited => a cell with a header that has "editor":"input" etc.. will be returned with row, initial value, old value, new value
# dataChanged => full table upon change (use with caution)
# dataFiltering => header filters as typed, before filtering has occurred (you get partial matching)
# dataFiltered => header filters and rows of data returned
# to receive a dict of the row values
@app.callback(
    Output("output", "children"),
    [
        Input("tabulator", "rowClicked"),
        Input("tabulator", "cellClick"),
        Input("tabulator", "cellDblClick"),
        Input("tabulator", "cellEdited"),
        Input("tabulator", "dataChanged"),
        Input("tabulator", "dataFiltering"),
        Input("tabulator", "dataFiltered"),
    ],
)
def display_output(row_clk, cell_clk, cell_tap, cell, data_changed, filters, data_filtered):
    print(row_clk)
    print(cell_clk)
    print(cell_tap)
    print(cell)
    print(data_changed)
    print(filters)
    print(data_filtered)
    return f"You have clicked row {row_clk} ; cell {cell_clk} ; cell (tap) {cell_tap}"


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
