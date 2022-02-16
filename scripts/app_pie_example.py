import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# This dataframe has 244 lines, but 4 distinct values for `day`
df = px.data.tips()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("Names:"),
    dcc.Dropdown(
        id='names', 
        value='day', 
        options=[{'value': x, 'label': x} 
                 for x in ['smoker', 'day', 'time', 'sex']],
        clearable=False
    ),
    html.P("Values:"),
    dcc.Dropdown(
        id='values', 
        value='total_bill', 
        options=[{'value': x, 'label': x} 
                 for x in ['total_bill', 'tip', 'size']],
        clearable=False
    ),
    dcc.Graph(id="pie-chart"),
])

@app.callback(
    Output("pie-chart", "figure"), 
    [Input("names", "value"), 
     Input("values", "value")])
def generate_chart(names, values):
    fig = px.pie(df, values=values, names=names)
    return fig

app.run_server(debug=True)