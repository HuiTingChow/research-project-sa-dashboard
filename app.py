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


# Change working directory to script location
# abspath = os.path.abspath(__file__)
# dname = os.path.dirname(abspath)
# os.chdir(dname)

# import sys
# sys.path.insert(0, '/apps/')
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },dbc.themes.BOOTSTRAP
]
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)
server = app.server

from apps import introduction,eda,sa,method,evaluation

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

height_top = "4rem"

# styling the sidebar
# SIDEBAR_STYLE = {
#     "position": "fixed",
#     "top": height_top,
#     "left": 0,
#     "bottom": 0,
#     "width": "16rem",
#     "padding": "2rem 1rem",
#     "background-color": "#f8f9fa",
# }

# NAVBAR_STYLE = {
#     "position": "fixed",
#     "top": 0,
#     "left": 0,
#     "right": 0,
#     "height": height_top,
#     "background-color": "white",
# }



# navbar = dbc.NavbarSimple(
#     # children=[
#     #     dbc.NavItem(dbc.NavLink("SENTIMENT ANALYSIS: MALAYSIAN MENTAL HEALTH DURING PANDEMIC", 
#     #                                 active=True, href="/")),
#     # ],
#     brand=["SENTIMENT ANALYSIS: MALAYSIAN MENTAL HEALTH DURING PANDEMIC",],
#     brand_href="/",
#     color="dark",
#     dark=True,
#     sticky="top",
#     style=NAVBAR_STYLE,
# )

# sidebar = html.Div(
#     [
#         html.P("Content"),
#         html.Hr(),
#         # html.P(
#         #     "Number of students per education level", className="lead"
#         # ),
#         dbc.Nav(
#             [
#                 dbc.NavLink("Introduction", href="/", active="exact",style={'backgroundColor':'black'}),
#                 dbc.NavLink("Exploratory Data Analysis", href="/eda", active="exact"),
#                 dbc.NavLink("Methodology", href="/methodology", active="exact"),
#                 dbc.NavLink("Models Evaluation", href="/models-evaluation", active="exact"),
#                 dbc.NavLink("Sentiment Analysis", href="/sentiment-analysis", active="exact"),
#                 dbc.NavLink("LDA Topic Model", href="/lda", active="exact"),
#             ],
#             vertical=True,
#             pills=True
#         ),
#     ],
#     style=SIDEBAR_STYLE,
# )

lda_node_during = html.Div([
    html.P(
        children="LDA topic model based on Tweets during pandemic",
        style={'textAlign': 'center'},
        className="lead"
    ),
    html.Iframe(src=app.get_asset_url("ldavis_prepared_4.html"),
                style=dict(position="absolute", width="100%", height="100%")
    )
])

lda_node_before = html.Div([
    html.P(
        children="LDA topic model based on Tweets before pandemic",
        style={'textAlign': 'center'},
        className="lead"
    ),
    html.Iframe(src=app.get_asset_url("ldavis_prepared_19_4.html"),
                style=dict(position="absolute", width="100%", height="100%")
    )
])

lda_page = html.Div([
    html.H2('LDA Topic Model',
            style={'textAlign':'center'}),
    html.Hr(),
    html.P(
        children="This section shows the common features in Tweets before and during the pandemic using LDA topic model.",
        style={'textAlign': 'center'},
        className="lead"
    ),
    html.Br(),
    dbc.Card(
        dcc.Markdown('''
        #### LDA (Latent Dirichlet Allocation) Topic Model Visualisation

        Topic modelling is one of the statistical language models that cluster words for a set of corpuses. 
        It is a useful model for revealing hidden pattern or structure from the text data. 
        If often be used in Natural Language Processing (NLP) to find common text terms and to reveal hidden relationship between word and the documents. 
        Here implements LDA, a topic model, to determine common themes or features in the whole corpus (the collected Tweets). 

        Method to interpret the graph below:
        * Each bubble represents a topic. The larger the bubble, the higher percentage of the number of tweets in the corpus is about that topic.
        * Blue bars represent the overall frequency of each word in the corpus. If no topic is selected, the blue bars of the most frequently used words will be displayed.
        * Red bars give the estimated number of times a given term was generated by a given topic. 
        
        Graph below visualises the LDA topic model based on Tweets from defferent periods. Select the radio button to view the differen LDA graph.
        '''
        ),
        body=True, color="success", outline=True,className="mb-3"
    ),
    dbc.Card(
        html.Div([
            dcc.RadioItems(
                id='period',
                options=[{'label': i, 'value': i} for i in ['Before','During']],
                value='During',
                labelStyle={'display': 'inline-block', 'padding-left':'1rem', 'padding-top':'1rem'},
                
            )], 
            style={'width': '100%', 'text-align':'center','display': 'inline-block'},
            className = 'mb-3'
        ),
        body=True, color="success", outline=True,className="mb-4 mt-4"
    ),
    html.Div(id="lda")
    

])

header_node = html.Div(
    [
        html.Br(),
        html.H2(children="SENTIMENT ANALYSIS: MALAYSIAN MENTAL HEALTH DURING PANDEMIC",
                className="HEADER_STYLE"),
        html.Br(),
        dbc.Nav(
            [
                dbc.NavLink("Overview", href="/", active="exact"),
                dbc.NavLink("Methodology", href="/methodology", active="exact"),
                dbc.NavLink("Exploratory Data Analysis", href="/eda", active="exact"),
                dbc.NavLink("Models Evaluation", href="/models-evaluation", active="exact"),
                dbc.NavLink("Changes In Sentiment", href="/sentiment-analysis", active="exact"),
                dbc.NavLink("LDA Topic Model", href="/lda", active="exact"),
            ],
            pills=True, fill=True
        ),
    ],
    className="HEADER_C_STYLE"
)
    

content = html.Div(id="page-content", children=[], className="CONTENT_STYLE")

app.layout = html.Div([
    dcc.Location(id="url"),
    header_node,
    # navbar,
    # sidebar,
    content
])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return introduction.layout
    elif pathname == "/eda":
        return eda.layout
    elif pathname == "/sentiment-analysis":
        return sa.layout
    elif pathname == "/lda":
        return lda_page
    elif pathname == "/methodology":
        return method.layout
    elif pathname == "/models-evaluation":
        return evaluation.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

@app.callback(Output("lda", "children"),Input("period", "value"))
def update_graph(period):
    if period == 'Before':
        return lda_node_before
    else:
        return lda_node_during 

if __name__ == '__main__':
    app.run_server(debug=True)


# Code reference
# https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Bootstrap/Side-Bar/side_bar.py
# https://realpython.com/python-dash/#style-your-dash-application
# https://community.plotly.com/t/holy-grail-layout-with-dash-bootstrap-components/40818/2
# https://commonmark.org/help/
# https://dash-bootstrap-components.opensource.faculty.ai/docs/components/
# https://dash.plotly.com/basic-callbacks