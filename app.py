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

from apps import introduction,eda,sa,lda

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

HEADER_STYLE = {
    "color": "white",
    "margin": "4px auto",
    "text-align": "center",
    # "max-width": "384px",
}

HEADER_C_STYLE = {
    "position": "absolute",
    "top": 0,
    "left": 0,
    "right": 0,
    "height": "10rem",
    "color":"white",
    "background-color": "#800000",
    "text-align": "center",
}

CONTENT_STYLE = {
    "margin-top": "9rem",
    "margin-left": "5rem",
    "margin-right": "5rem",
    "padding": "2rem 1rem",
}

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

header_node = html.Div(
    [
        html.Br(),
        html.H2(children="SENTIMENT ANALYSIS: MALAYSIAN MENTAL HEALTH DURING PANDEMIC",
                style=HEADER_STYLE),
        # html.H1(
        #     children="Avocado Analytics" ,
        #     style=HEADER_STYLE ),
        # html.P(
        #     children="Sentiment analysis Malaysian Tweets before and during the COVID-19 pandemic"
        #     " using Machine Learning Models"
        #     " to study changes in Malaysian mental health status.",
        #     style=HEADER_STYLE,
        # ),
        html.Br(),
        dbc.Nav(
            [
                dbc.NavLink("Introduction", href="/", active="exact"),
                dbc.NavLink("Methodology", href="/methodology", active="exact"),
                dbc.NavLink("Exploratory Data Analysis", href="/eda", active="exact"),
                dbc.NavLink("Models Evaluation", href="/models-evaluation", active="exact"),
                dbc.NavLink("Sentiment Analysis", href="/sentiment-analysis", active="exact"),
                dbc.NavLink("LDA Topic Model", href="/lda", active="exact"),
            ],
            pills=True, fill=True
        ),
    ],
    style=HEADER_C_STYLE
)
    

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

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
        return lda.layout
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


# Code reference
# https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Bootstrap/Side-Bar/side_bar.py
# https://realpython.com/python-dash/#style-your-dash-application
# https://community.plotly.com/t/holy-grail-layout-with-dash-bootstrap-components/40818/2