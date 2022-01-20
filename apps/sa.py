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


df = pd.read_csv("../datasets/final_tweets.csv")
df['new_tweet_text'] = df['new_tweet_text'].astype(str)

# Dataset summaru table
table_header = [
    html.Thead(html.Tr([html.Th("Attribute"), 
                        html.Th("Data Type"),
                        html.Th("Description"),
                        html.Th("Example"),]))
]

row1 = html.Tr([html.Td("tweet"),
                html.Td("String"), 
                html.Td("Tweet content"),
                html.Td("When can I leave Malaysia? I am tired.")])

row2 = html.Tr([html.Td("date"),
                html.Td("Date"), 
                html.Td("Tweet posted date"),
                html.Td("2019-03-18")])

row3 = html.Tr([html.Td("retweet"),
                html.Td("Integer"), 
                html.Td("ReTweet count"),
                html.Td("6000")])

row4 = html.Tr([html.Td("like"),
                html.Td("Integer"), 
                html.Td("Liked count"),
                html.Td("6000")])

row4 = html.Tr([html.Td("sentiment"),
                html.Td("Integer"), 
                html.Td("Annotated sentiment; 0 = Negative; 1 = Positve"),
                html.Td("0")])

table_body = [html.Tbody([row1, row2, row3, row4])]
# table = dbc.Table(table_header + table_body, bordered=True)

# Time Series
df['date'] = pd.to_datetime(df['date'])
df['month_year'] = df['date'].dt.to_period('M')
data_ts = pd.crosstab(df['year_month'],df['sentiment'])\
           .apply(lambda x: round(x / x.sum() * 100, 2), axis = 1)

data_ts = data_ts.add_prefix('sentiment_').reset_index().rename_axis(None, axis=1) 
# fig = px.bar(data_ts, x="month_year", y=["sentiment_0","sentiment_1"], barmode="group")

# Layout
layout = html.Div([
    html.H2('Changes In Sentiment Before and During the Pandemic',
            style={'textAlign':'center'}),
    html.Hr(),
    html.P(
        children="This section compares changes in sentiment before and during the pandemic.",
        className="lead",style={'textAlign':'center'}
    ),
    html.Br(),
    
#     dcc.RadioItems(
#         id='xaxis_year',
#         options=[{'label': i, 'value': i} for i in ['All', 2019, 2020,2021]],
#         value='All',
#         labelStyle={'display': 'inline-block', 'padding-left':'1rem'},
#         style={'width': '48%', 'float': 'center', 'display': 'inline-block'}
#     ),
    dbc.Card(
        dcc.Markdown('''
        #### Time Series Analysis

        The figure below shows the distribution percentage of positive and negative Tweets before and during the pandemic. 
        '''
        ),
        body=True, color="success", outline=True,className="mb-3"
    ),
    dcc.Graph(id='linegraph'
        ,
        figure ={
          'data': [
             {'x':data_ts.year_month,'y':data_ts.sentiment_0,'type':'line','name':'Negative','line_color':'red'},
             {'x':data_ts.year_month,'y':data_ts.sentiment_1,'type':'line','name':'Positve','line_color':'blue'}
          ],
          'layout': { 'title':'Distribution of The Tweets Sentiment' }
        }
    ),
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
    ),
  
])


# @app.callback(
#     Output("linegraph", "figure"),
#     [Input("xaxis_year", "value")])
# def update_graph(xaxis_year):
#         df = pd.read_csv("../datasets/final_tweets.csv")

#         if xaxis_year == 'All':
#                 df1 = df
#         else:
#                 df1 = df[df['year'] == xaxis_year]

#         df1['date'] = pd.to_datetime(df1['date'])
#         df1['month_year'] = df1['date'].dt.to_period('M')
#         data_ts = pd.crosstab(df1['year_month'],df1['sentiment'])\
#                         .apply(lambda x: round(x / x.sum() * 100, 2), axis = 1)

#         data_ts = data_ts.add_prefix('sentiment_').reset_index().rename_axis(None, axis=1) 

#         fig ={
#           'data': [
#              {'x':data_ts.year_month,'y':data_ts.sentiment_0,'type':'line','name':'Negative','line_color':'red'},
#              {'x':data_ts.year_month,'y':data_ts.sentiment_1,'type':'line','name':'Positve','line_color':'blue'}
#           ],
#           'layout': { 'title':'Distribution of The Tweets Sentiment' }
#         }
#         # fig =px.line(data_ts, x='year_month', y=['sentiment_0', 'sentiment_1'])

#         fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

#         fig.update_xaxes(title='Year')

#         fig.update_yaxes(title='Percentage(%)')
        
#         return fig 