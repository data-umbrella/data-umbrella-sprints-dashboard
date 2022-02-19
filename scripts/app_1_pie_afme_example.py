import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# This dataframe has 244 lines, but 4 distinct values for `day`
#df = px.data.tips()

data_url = "https://raw.githubusercontent.com/data-umbrella/data-umbrella-sprints-dashboard/main/data/data_derived/afme2_derived.csv"
df = pd.read_csv(data_url)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("Names:"),
    dcc.Dropdown(
        id='names', 
        value='status_c', 
        options=[{'value': x, 'label': x} 
                 for x in ['gender', 'contributor_status', 'status_c','continent_o', 'python_experience', 'country']],
        clearable=False
    ),
    html.P("Values:"),
    dcc.Dropdown(
        id='values', 
        value='count_rows', 
        options=[{'value': x, 'label': x} 
                 for x in ['count_rows']],
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
    fig.update_traces(textposition='inside', textinfo='value+percent+label')
    return fig



app.run_server(debug=True)