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
    html.H1('Introduction',
            style={'textAlign':'center'}),
    html.Hr(),
    dbc.Card(
        dcc.Markdown('''
        From the figure above can observe that the Tweets posted during the pandemic have more negative Tweets and lesser positive Tweets compares to the Tweets posted before the pandemic. Before the pandemic, around 60% to 70% of the Tweets in each month usually are predicted as negative sentiment. 
        Ever since the first Malaysian Movement Control Order (MCO), the number of Tweets got predicted as negative increased by 10%. 

        Below lists down the events that affected sentiment changes significantly:

        * In May 2020, the phase 4 of MCO was going to finally end after three extensions of MCO. 
        
        * In August 2020, Malaysia has implemented mandatory face mask-wearing in public starting from August 2020. Most of the Malaysians financial situation was impacted by COVID-19 pandemic, an extra expense which is purchasing face mask will definitely make their financial situation and mental health worse. In fact, the most frequent words during August 2020 include ‘bad’, ‘tired’, ‘find’, ‘work’, ‘corruption’, and ‘country’. The frequent words of August 2020 implies that Malaysian were struggle with financial problem and concern with politic corruption. 
        
        * In September 2021, Malaysia government announced that all the federal government employees are mandatory to be vaccinated. Having a hope that the more population being vaccinated, the more unlikely being infected, Malaysian could be feeling safer.
        
        As a conclusion, compared to text data before the pandemic, the text data during pandemic tend to be classified as a negative sentiment. The feeling and mental state often impacted by the important COVID-19 related events that have happened during the pandemic.

        '''
        ),
        body=True, color="success", outline=True,className="mb-3"
    )
])


# @app.callback(
#     Output("page-content", "children"),
#     [Input("url", "pathname")]
# )