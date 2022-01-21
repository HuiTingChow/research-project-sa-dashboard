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

# row3 = html.Tr([html.Td("retweet"),
#                 html.Td("Integer"), 
#                 html.Td("ReTweet count"),
#                 html.Td("6000")])

# row4 = html.Tr([html.Td("like"),
#                 html.Td("Integer"), 
#                 html.Td("Liked count"),
#                 html.Td("6000")])

row4 = html.Tr([html.Td("sentiment"),
                html.Td("Integer"), 
                html.Td("Annotated sentiment; 0 = Negative; 1 = Positve"),
                html.Td("0")])

table_body = [html.Tbody([row1, row2, row4])]
table = dbc.Table(table_header + table_body, bordered=True)

# Most frequent word
authors_notflat = [a.split() for a in df['new_tweet_text']]
counter = Counter(chain.from_iterable(authors_notflat))
tweet_counts = [count for tag, count in counter.most_common(20)]
word_content = [tag for tag, count in counter.most_common(20)]
df_freq = pd.DataFrame(
            {'word': word_content,
            'count': tweet_counts
            })


# Layout
layout = html.Div([
    html.H1('Exploratory Data Analysis',
            style={'textAlign':'center'}),
    html.Hr(),
    html.P(
        children="This section analysis and explore the cleaned dataset.",
        style={'textAlign': 'center'},
        className="lead"
    ),
    dbc.Card(
        dcc.Markdown('''
        #### Dataset

        Total 2377 random Malaysian English Tweets that posted on Twitter.com from 2019 to 2021 
        and contain any one of the identified keywords were collected. The table below shows 
        the summary of the cleaned dataset. The cleaning process included handle missing value, 
        normalise string & date to suitable format, and remove duplicated rows. Attributes such 
        as user id, user profile link, Tweet link that were not related to this were not collected. 

        There were 700 Tweets annotated with sentiment mannually for training classification models.
        After determinded the best model, used the model to classify the remain Tweets. 

        List of identifies keyword: depress, failure, hopeless, nervous, restless, tired, 
        worthless, annoy, guilt, bad, cut,fat, shame, scare, panic
        '''
        ),
        body=True, color="success", outline=True,className="mb-3"
    ),
    
    table,
    html.Br(),
    dbc.Card(
        dcc.Markdown('''
        #### 20 Most Frequent Words

        The figure below shows the distribution of frequent words in the raw dataset. 
        From the figure can observe that majority of the words which appeared most frequently 
        were common words and did not add much information to the text. These common words 
        were removed in the Text Pre-process stage to reduce the training time of the model
        and to increase the accuracy of the model.
        '''
        ),
        body=True, color="success", outline=True,className="mb-3"
    ),
    
    dcc.Graph(id='bargraph',
            figure=px.bar(df_freq, barmode='group', x="word", y="count"))
])


# @app.callback(
#     Output("page-content", "children"),
#     [Input("url", "pathname")]
# )