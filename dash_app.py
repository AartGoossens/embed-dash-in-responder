import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(
    name=__name__,
    external_stylesheets=external_stylesheets,
    requests_pathname_prefix='/dash/'
)


app.layout = html.Div(children=[
    html.H1(children='Simple Dash app'),
    html.P('Chart title:'),
    dcc.Input(id='input-field', value='This is the title of my pie chart', type='text'),
    dcc.Graph(id='pie-chart')
])


@app.callback(
    Output(component_id='pie-chart', component_property='figure'),
    [Input(component_id='input-field', component_property='value')]
)
def update_output_div(input_value):
    return {
        'data': [
            {
                'values': [10, 90],
                'labels': ['tiny part', 'big part'],
                'type': 'pie'
            }
        ],
        'layout': {'title': input_value}
    }


if __name__ == '__main__':
    app.run_server(debug=True)
