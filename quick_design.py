from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px

# Iris bar figure
def drawFigure():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df, x="sepal_width", y="sepal_length", color="species"
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    ),
                    config={
                        'displayModeBar': False
                    }
                )
            ])
        ),
    ])

# upload button
def uploadButton():
    return html.Div([
        # dbc.Card(
        #     dbc.CardBody([
                html.Div([
                    dcc.Upload(id="upload_id",children=html.Button('Upload File')),
                    dbc.Alert(
                        "Click button to upload the file.",
                        color="warning",
                    )
                ])
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
df = px.data.iris()

# Defining an Accordion
def addAccordion(title_Accordion,key,text_data,add_ons):
    return html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    html.P(text_data),
                    add_ons,
                    dbc.Button(
                        str(key),
                        className="btn btn-primary",
                        id=str(key),
                        style={
                            "margin-right": "10px",
                            "margin-bottom": '10px',
                        },
                        n_clicks=0,
                    ),
                ],
                title=str(title_Accordion),
            )]
    )
    )

# Build App
app = Dash(external_stylesheets=[dbc.themes.SLATE])
# app = Dash(__name__)
Accordion_add_ons = dbc.CardBody([
            dbc.Row([
                dbc.Col(html.Div("Upload Ansys .anf file")),
                dbc.Col([
                    uploadButton()
                ])
            ])
    ])

app.layout = html.Div([
    addAccordion("Upload EDB file","Validate", 'Adding the data', Accordion_add_ons),
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
            dbc.Row([
                dbc.Col([
                    drawFigure()
                ], width=3),
                dbc.Col([
                    drawFigure()
                ], width=3),
                dbc.Col([
                    drawFigure()
                ], width=6),
            ], align='center'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawFigure()
                ], width=9),
                dbc.Col([
                    drawFigure()
                ], width=3),
            ], align='center'),
        ]), color = 'dark'
    ),
])


# @app.callback(
#     # Output('graph-with-slider', 'figure'),
#     Input("Validate", 'value'))
# def update_status:

# Run app and display result inline in the notebook
if __name__ == '__main__':
    app.run_server(debug=True)