# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import os
import pathlib
from app import app

# get relative data folder
# PATH = pathlib.Path(__file__).parent
# DATA_PATH = PATH.joinpath("../datasets").resolve()

# Change working directory to script location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


df0 = pd.read_csv("../datasets/students.csv")
df = pd.read_csv("../datasets/final_tweets.csv")

layout = html.Div([
    html.H1('INTRODUCTION',
            style={'textAlign':'center'}),
    html.Hr(),
    html.P(
        children="Analyze the behavior of avocado prices"
        " and the number of avocados sold in the US"
        " between 2015 and 2018",
        className="lead"
    ),
    dcc.Markdown('''
    #### Dash and Markdown

    Dash supports [Markdown](http://commonmark.org/help).

    test

    Markdown is a simple way to write and format text.
    It includes a syntax for things like **bold text** and *italics*,
    [links](http://commonmark.org/help), inline `code` snippets, lists,
    quotes, and more.
    '''
    ),
    # dcc.Graph(id='bargraph',
    #         figure=px.bar(df, barmode='group', x="year_month", y="like"))
])


# @app.callback(
#     Output("page-content", "children"),
#     [Input("url", "pathname")]
# )