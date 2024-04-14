from dash import Dash, html, dcc
import plotly.express as px 
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [9, 3, 1, 4, 4, 3],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]

})

fig = px.bar(df, x= "Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children = '''
            Dash: A web application framework for your data
             '''),
    dcc.Graph(
        id = 'example_graph',
        figure= fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)




