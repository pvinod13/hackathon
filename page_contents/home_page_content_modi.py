import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dcc, html, callback, State
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
# def uploadButton():
#     return html.Div([
#         # dbc.Card(
#         #     dbc.CardBody([
#                 html.Div([
#                     dcc.Upload(id="upload_id", children=html.Button('Upload File')),
#                     dbc.Alert(
#                         "Click button to upload the file.",
#                         color="warning",
#                     )
#                 ]),
#                 html.Div([
#                 html.Div(id="txt_id")])
#         #     ])
#         # )
#     ])


def uploadButton():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H4("Upload ECAD File"),
                    dcc.Upload(
                    id='upload-file',
                    children=html.Div([
                        'Drag and Drop or ',
                        html.A('Select Files')
                    ]),
                    style={
                        'width': '100%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin-top': '30px'
                    },
                    multiple=False
                ),
                html.Div(id='output-file')
                ], style={'textAlign': 'center'}),

                html.Div([html.Button(id='submit-button', n_clicks=0, children='Submit', style={'margin-top': '30px'}),                ], style={'textAlign': 'center'})
            ])
        ),
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
def addAccordion(title_Accordion,validation_button,text_data = {}):
    return html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    uploadButton()
                    # html.P(text_data),
                    # cardbody_one(),
                    # validation_button,
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

def cardbody_one():
    return dbc.CardBody([
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
                        className="btn btn-primary",
                        id="Validate_id",
                        style={
                            "margin-right": "10px",
                            "margin-bottom": '10px',
                        },
                        n_clicks=0,
                    )

accordion2_homepage = html.Div([dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                html.Img(id = "pcb_figure")
                                ],
                                title=str(),
                            )]
                    )
    ])


def page_layout():
    return html.Div([
    addAccordion("Upload EDB file", text_data = "introduction to the project"),
    accordion2_homepage,
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    drawText()
                ], width=1),
                dbc.Col([
                    drawText()
                ], width=1),
                dbc.Col([
                    drawText()
                ], width=1),
                dbc.Col([
                    drawText()
                ], width=1),
            ], align='center'),
            html.Br(),
        ]), color = 'dark'
    ),
])

def parse_file(contents, filename):
    if '.def' in filename:
        # do something
        return f'You uploaded a .def file: {filename} and File has been uploaded !!'
    elif '.anf' in filename:
        # do something
        return f'You uploaded a .anf file: {filename} and File has been uploaded !!'
    else:

        return f'Unsupported file format: {filename}'

# @callback(
#     Output('output-file', 'children'),
#     [Input('upload-file', 'contents')],
#     [State('upload-file', 'filename')]
# )
# def update_output(contents, filename):
#     print('checking update')
#     if contents is not None:
#         return parse_file(contents, filename)
#     else:
#         return 'No file uploaded'
# @callback(
#     dash.dependencies.Output("txt_id", 'children'),
#     dash.dependencies.Input("upload_id","filename"),
#     # dash.dependencies.State("upload_id","filename")
#     #Input("Validate", 'children') # Input("upload_id","filename")
# )
# def update_file_validation(validate_filename): # only_uploaded_filename
#     file_name = []
#     file_name = validate_filename
#     [name,extension] = file_name.split(".")
#     print(extension)
#     valid_extension_list = ["anf","edb","aedt"]
#     if extension in valid_extension_list:
#         return 'File validation is successfull'
#     else:
#         return 'There is an error processing this file.'


# @app.callback(
#     Output('pcb_figure', 'figure'),
#     [Input("Validate_id","n_clicks")])
# def on_button_click(n):
#     print('clicked button')
#     if n is None:
#         return "Not clicked."
#     else:
#         return f"Clicked {n} times."
# @app.callback(
#     Output("example-output", "children"), [Input("example-button", "n_clicks")]
# )
# def on_button_click(n):
#     if n is None:
#         return print("Not clicked.")
#     else:
#         return print(f"Clicked {n} times.")
#     [dash.dependencies.State('upload_id', 'filename')])
# def update_fig(validate_file):
#     return print("validate_button_pressed")
