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

# Evaluation metric
table_header = [
    html.Thead(html.Tr([html.Th("Classifier"),
                        html.Th("Accuracy"), 
                        html.Th("Precision"),
                        html.Th("Recall"),
                        html.Th("F1 Score"),
                        html.Th("Speed (seconds)"),]))
]

row1 = html.Tr([html.Td("MNB"),
                html.Td("60.59%"), 
                html.Td("62.63%"), 
                html.Td("57.82%"),
                html.Td("60.13%"),
                html.Td("0.008")])

row2 = html.Tr([html.Td("Linear SVM"),
                html.Td("65.31%"), 
                html.Td("62.58%"), 
                html.Td("73.90%"), 
                html.Td("67.77%"),
                html.Td("0.179")])

row3 = html.Tr([html.Td("VADER"),
                html.Td("88.97%"), 
                html.Td("92.37%"), 
                html.Td("84.95%"), 
                html.Td("84.95%"),
                html.Td("0.540")])

table_body = [html.Tbody([row1, row2, row3])]
table = dbc.Table(table_header + table_body, bordered=True)


# Layout
layout = html.Div([
    html.H2('Models Evaluation',
            style={'textAlign':'center'}),
    html.Hr(),
    html.P(
        children="This section summarise the models evaluation results.",
        style={'textAlign': 'center'},
        className="lead"
    ),
    html.Br(),
    dbc.Card(
        dcc.Markdown('''
        #### Performance Metrics

        The MNB classifier, Linear SVM classifier and VADER classifier were evaluated by their accuracy, precision, recall, F1-score, and speed. 
        The speed referred to how fast the classifiers could train the model and the measured unit was second (s). 
        
        The table below the summarised performance of all classifiers.
        '''
        ),
        body=True, color="success", outline=True,className="mb-3"
    ),
    table,
    dbc.Card(
        dcc.Markdown('''
        From the table above can see that VADER has the highest rate for accuracy, precision, recall, F1-score but slowest processing speed.
        The MNB has the lowest rate for accuracy, precision, recall, and F1-score but the fastest processing speed.
        The VADER is the best model as it has the best performance even though is rather slower than the Linear SVM classifier and MNB classifier.  
        Hence, this research selected VADER to classify the remaining Tweets to positive or negative. 
        '''
        ),
        body=True, color="success", outline=True,className="mb-3"
    ),

])
