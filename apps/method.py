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
from itertools import chain
from collections import Counter

from app import app


# Change working directory to script location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


# df = pd.read_csv("../datasets/final_tweets.csv")
# df['new_tweet_text'] = df['new_tweet_text'].astype(str)

# Load LDA
sys_design = html.Iframe(src=app.get_asset_url("system overview.png"), className="center")


# Layout
layout = html.Div([
    html.H2('Methodology',
            style={'textAlign':'center'}),
    html.Hr(),
    html.P(
        children="This section briefly describe the system design of the research.",
        style={'textAlign': 'center'},
        className="lead"
    ),
    html.Br(),
    dbc.Card(
        dcc.Markdown('''
        In this research, sentiment analysis is performed on Malaysian social media posts before and during the COVID-19 pandemic. 
        The input will be the Tweets extracted from social media platforms. 
        The procedure of sentiment analysis involves text pre-processing, feature extraction, classification, and result analysation. 
        The output will be an online dashboard that displays the classified sentiment and visualisation of common features in each sentiment class. 
        The figure below illustrates the system design of this research.
        '''
        ),
        body=True, color="success", outline=True,className="mb-3"
    ),
    sys_design
    

])


# @app.callback(
#     Output("page-content", "children"),
#     [Input("url", "pathname")]
# )