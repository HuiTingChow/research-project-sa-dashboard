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
    html.H1('Overview',
            style={'textAlign':'center'}),
    html.Hr(),
    html.P(
        children="An overview about the research.",
        style={'textAlign': 'center'},
        className="lead"
    ),
    dbc.Card(
        dcc.Markdown('''
        #### Introduction

        The COVID-19 pandemic has been affecting Malaysians daily life and is slowing down the global economy. 
        This research investigates changes in the mental health status of Malaysian using sentiment analysis. 
        Related Tweets are collected for analysing. 
        This research compares the supervised machine learning technique and unsupervised machine learning technique to find a suitable model to classify the polarity of collected Tweets. 
        A portion of collected Tweets was manually labelled to train the supervised machine learning model. 
        The results show that the VADER classifier outperformed the other classifiers with an 89% accuracy 
        where the Linear Support Vector Machine classifier achieved 65% accuracy and 
        the Multinomial Naïve Bayes classifier achieved 61% accuracy. 
        The VADER classifier was selected to classify the sentiment of the remaining Tweets. 
        The sentiment classified Tweets were analysed using various techniques including Time series analysis, Word Cloud, and LDA. 
        The result indicates that Tweets posted during the pandemic have more change to be classified as 
        negative sentiment compared to the Tweets posted before the pandemic. 
        The findings of this research suggest that Malaysian mental health is highly impacted 
        by the COVID-19 pandemic and political crisis in Malaysia.  
        '''
        ),
        body=True, color="success", outline=True,className="mb-3"
    ),
    dbc.Card(
        dcc.Markdown('''
        #### About this dashboard

        This dashboard was developed to give an simple introduction and overview of how the research was conducted and to
        demonstrate and visualise the results and findings of this research. Below is the content structure of this dashboard:

        * Overview - Introduction to this research
        * Methodology - Briefly describe the system design of the research
        * Exploratory Data Analysis - Analysis and explore the cleaned dataset
        * Changes In Sentiment - Compare changes in sentiment before and during the pandemic
        * LDA Topic Model - Compare the common features in Tweets before and during the pandemic
        '''
        ),
        body=True, color="success", outline=True,className="mb-3"
    )
])


# @app.callback(
#     Output("page-content", "children"),
#     [Input("url", "pathname")]
# )