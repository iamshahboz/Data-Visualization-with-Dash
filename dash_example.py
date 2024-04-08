from dash import Dash, html, dcc
from dash.dependencies import Input, Output


app = Dash()

app.layout = html.Div(children=[html.H1('Dash tutorial'),
                    dcc.Input(id='input', 
                              value='Enter something', type='text'),
                    html.Div(id='output')
                    ])

@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
)

def update_value(input_data):
    return "Input: {}".format(input_data)



if __name__ == '__main__':
    app.run_server(debug=True)



