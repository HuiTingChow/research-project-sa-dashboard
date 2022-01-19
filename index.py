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

from app import app
from app import server
from apps import introduction,eda

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

height_top = "4rem"

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": height_top,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

NAVBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "right": 0,
    "height": height_top,
    "background-color": "white",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-top": "5rem",
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

navbar = dbc.NavbarSimple(
    # children=[
    #     dbc.NavItem(dbc.NavLink("SENTIMENT ANALYSIS: MALAYSIAN MENTAL HEALTH DURING PANDEMIC", 
    #                                 active=True, href="/")),
    # ],
    brand=["SENTIMENT ANALYSIS: MALAYSIAN MENTAL HEALTH DURING PANDEMIC",],
    brand_href="/",
    color="dark",
    dark=True,
    sticky="top",
    style=NAVBAR_STYLE,
)

sidebar = html.Div(
    [
        html.P("Content"),
        html.Hr(),
        # html.P(
        #     "Number of students per education level", className="lead"
        # ),
        dbc.Nav(
            [
                dbc.NavLink("Introduction", href="/", active="exact"),
                dbc.NavLink("Exploratory Data Analysis", href="/eda", active="exact"),
                dbc.NavLink("Models Evaluation", href="/models-evaluation", active="exact"),
                dbc.NavLink("Sentiment Analysis", href="/sentiment-analysis", active="exact"),
                dbc.NavLink("LDA Topics", href="/lda", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    navbar,
    sidebar,
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
    elif pathname == "/page-1":
        return [
                html.H1('Grad School in Iran',
                        style={'textAlign':'center'}),
                # dcc.Graph(id='bargraph',
                #          figure=px.bar(df0, barmode='group', x='Years',
                #          y=['Girls Grade School', 'Boys Grade School']))
                ]
    elif pathname == "/page-2":
        return [
                html.H1('High School in Iran',
                        style={'textAlign':'center'}),
                # dcc.Graph(id='bargraph',
                #          figure=px.bar(df0, barmode='group', x='Years',
                #          y=['Girls High School', 'Boys High School']))
                ]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )



if __name__ == '__main__':
    app.run_server(debug=True)
