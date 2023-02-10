import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, State
import pandas as pd

df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')
scrolling = html.Div([
            dbc.Row([
                dbc.Col([
                    dcc.Dropdown(
                        id='segment',
                        options=[{'label': i, 'value': i} for i in df['Country Name'].unique()],
                        persistence=True, persistence_type='memory',
                        multi=True,
                        style={'width': '500px', 'display': 'inline-block'}, optionHeight=70,
                        placeholder='Segment'),
                ], style={'margin-top': 80, 'margin-left': 15, 'display': 'table-cell', 'verticalAlign': 'middle',
                          })
            ])])

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    scrolling
])

if __name__ == '__main__':
    app.run_server(debug=True)