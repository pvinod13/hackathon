import dash
import dash_bootstrap_components as dbc
import random
from dash import Dash, Input, Output, dcc, html, callback
import pandas as pd
import os
# from dash_extensions.enrich import Input, Output, State, callback, dcc, html

def drawFigure():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Img(src='assets/pic2.jpg'),
                print("image updated")
            ])
        ),
    ])


layer_names = ['a','b','c','d']
net_names = random.sample(range(0, 10), 7)

# Text field
def drawText(text="Text"):
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.Plaintext(str(text)),
                ], style={'textAlign': 'center'})
            ])
        ),
    ])

net_names = {'Net Name': ["net-1","net-2","net-3","net-4","net-5","net-6","net-7","net-8"]}
df = pd.DataFrame(net_names)
# Data
# df = px.data.iris()
scrolling = html.Div([
            dbc.Row([
                dbc.Col([
                    dcc.Dropdown(
                        id='segment',
                        options=[{'label': i, 'value': i} for i in df['Net Name'].unique()],
                        persistence=True, persistence_type='memory',
                        multi=True,
                        style={'width': '500px', 'display': 'inline-block'}, optionHeight=70,
                        placeholder='Select Net Names for Clipping'),
                ], style={'margin-top': 80, 'margin-left': 15, 'display': 'table-cell', 'verticalAlign': 'middle',
                          })
            ])])


cardbody_one = dbc.CardBody([
                dbc.Row([
                    dbc.Col(html.Div("Upload Ansys .anf file")),
                    dbc.Col([
                        html.P("adding plane text")
                    ]),
                ]),
                html.Div(id='output-file'),
            ])

validation_button = dbc.Button(
        "Validate",
        className="me-2", #"btn btn-primary",
        id="Validate_id2",
        style={
            "margin-right": "10px",
            "margin-bottom": '10px',
        },
        n_clicks=0,
    )

inputs = html.Div([
        dbc.Input(placeholder="Valid input...", valid=True, className="mb-2")])

accordion2_homepage = html.Div([
    dbc.Accordion([
        dbc.AccordionItem([
            # inputs,
            scrolling
        ], title="Select the clipping region")
    ])
])

def page_layout():
    return html.Div([
        accordion2_homepage,
        # cardbody_one
])

@callback(
    dash.dependencies.Output("txt_id2", 'children'),
    dash.dependencies.Input("upload_id2","filename"),
    # dash.dependencies.State("upload_id","filename")
    #Input("Validate", 'children') # Input("upload_id","filename")
)
def update_file_validation(validate_filename): # only_uploaded_filename
    file_name = []
    file_name = validate_filename
    [name,extension] = file_name.split(".")
    print(extension)
    valid_extension_list = ["anf","edb","aedt"]
    if extension in valid_extension_list:
        return 'File upload is successfull'
    else:
        return 'Error in uploading this file.'


@callback(
    Output("example-output2", "children"), # children
    [Input("Validate_id2","n_clicks")])
def on_button_click(n_clicks):
    n = n_clicks
    print(n)
    if n is None:
        return "Not clicked."
    else:
        return html.Img(src='assets/pic1.png', alt='image')

