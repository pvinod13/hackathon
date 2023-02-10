import dash
from dash import  html,dcc
# import dash_html_components as html
# import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Input(id='demo-input', value='Type here'),
    dcc.Dropdown(
        id='demo-dropdown',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'}
        ]
    )
])

@app.callback(
    Output('demo-dropdown', 'placeholder'), # <- dropdown placeholder gets updated
    Input('demo-input', 'value'))
def update_placeholder(value):
    return value

if __name__ == '__main__':
    app.run_server(debug=True)