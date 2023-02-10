import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dcc, html, callback
import base64
import io
import os
# from dash_extensions.enrich import Input, Output, State, callback, dcc, html

def drawFigure():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Img(src='assets/pic1.png'),
                print("image updated")
            ])
        ),
    ])

# upload button
def uploadButton():
    return html.Div([
                html.Div([
                    dcc.Upload(id="upload_id", children=html.Button('Upload File')),
                ]),
                html.Div([
                html.Div(id="txt_id")])
        #     ])
        # )
    ])



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

# Data
# df = px.data.iris()

# Defining an Accordion
def addAccordion(title_Accordion,cardbody_one,validation_button,text_data = {}):
    return html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    # html.P(text_data),
                    cardbody_one,
                    validation_button,
                ],
                title=str(title_Accordion),
            )]
    )
    )

# Build App
# app = Dash(external_stylesheets=[dbc.themes.SLATE])
# app = Dash(__name__)
Accordion_add_ons = dbc.CardBody([
            dbc.Row([
                dbc.Col(html.Div("Upload Ansys .anf file")),
                dbc.Col([
                    uploadButton()
                ])
            ])
    ])

cardbody_one = dbc.CardBody([
                dbc.Row([
                    dbc.Col(html.Div("Upload Ansys .anf file")),
                    dbc.Col([
                        uploadButton()
                    ]),
                ]),
                html.Div(id='output-file'),
            ])

validation_button = dbc.Button(
        "Validate",
        className="me-2", #"btn btn-primary",
        id="Validate_id",
        style={
            "margin-right": "10px",
            "margin-bottom": '10px',
        },
        n_clicks=0,
    )


accordion2_homepage = html.Div([
    dbc.Accordion([
        dbc.AccordionItem([
            html.Div(id = "example-output")
            # dcc.Graph(id = "example-output"),
            # html.Div(html.Img(id="example-output"))
        ])
    ])
])

def page_layout():
    return html.Div([
    html.P([
        "This is a project for democratizing the SYZ for a PCB and give access to many people through web interface"],
        # justify="center", align="center"
    ),
    addAccordion("Upload EDB file",cardbody_one, validation_button, text_data = "introduction to the project"),
    accordion2_homepage,
])

@callback(
    dash.dependencies.Output("txt_id", 'children'),
    dash.dependencies.Input("upload_id","filename"),
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
    Output("example-output", "children"), # children
    [Input("Validate_id","n_clicks")])
def on_button_click(n_clicks):
    n = n_clicks
    print(n)
    if n == 0:
        return "Validate the file to show the image."
    else:
        return html.Img(src='assets/pic1.png', alt='image')

