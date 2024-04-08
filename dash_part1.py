from dash import Dash, html, dcc

app = Dash()

app.layout = html.Div(children=[html.H1('Dash tutorial'),
             dcc.Graph(id='example',
                       figure={
                           'data' : [
                               {
                                   'x': [1,2,3,4,5], 'y': [5,6,7,2,1], 'type': 'line', 'name': 'boats'
                               },
                               {
                                   'x': [1,2,3,4,5], 'y': [8,3,2,3,5], 'type': 'bar', 'name': 'cars'
                               },
                           ],
                           'layout': {
                               'title': 'Basic Dash  Example'
                           }
                       })])

if __name__ == '__main__':
    app.run_server(debug=True)



