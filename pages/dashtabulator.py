#!/usr/bin/env python3
# coding: utf-8


from dash import dcc, html, register_page
from dash_tabulator import DashTabulator

register_page(__name__, path_template="/tabulator")

styles = {"pre": {"border": "thin lightgrey solid", "overflowX": "scroll"}}

# Additional options can be setup here
# these are passed directly to tabulator
# In this example we are enabling selection
# Allowing you to select only 1 row
# and grouping by the col (color) column
options = {}  # {"groupBy": "col", "selectable": 1}

# downloadButtonType
# takes
#       css     => class names
#       text    => Text on the button
#       type    => type of download (csv/ xlsx / pdf, remember to include appropriate 3rd party js libraries)
#       filename => filename prefix defaults to data, will download as filename.type
downloadButtonType = {"css": "btn btn-primary", "text": "Export", "type": "xlsx"}


# clearFilterButtonType
# takes
#       css     => class names
#       text    => Text on the button
clearFilterButtonType = {"css": "btn btn-outline-dark", "text": "Clear Filters"}


# Add a dash_tabulator table
# columns=columns,
# data=data,
# Can be setup at initialization or added with a callback as shown below
# thank you @AnnMarieW for that fix
def layout():
    return html.Div(
        [
            DashTabulator(
                id="tabulator",
                # columns=columns,
                # data=data,
                options=options,
                downloadButtonType=downloadButtonType,
                clearFilterButtonType=clearFilterButtonType,
            ),
            html.Div(id="output"),
            dcc.Interval(
                id="interval-component-iu",
                interval=1 * 10,  # in milliseconds
                n_intervals=0,
                max_intervals=0,
            ),
        ]
    )
