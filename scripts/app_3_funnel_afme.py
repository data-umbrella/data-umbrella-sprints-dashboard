import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

from plotly import graph_objects as go

data_url = "https://raw.githubusercontent.com/data-umbrella/data-umbrella-sprints-dashboard/main/data/data_derived/afme2_derived.csv"
df = pd.read_csv(data_url)


# Reference
# https://stackoverflow.com/questions/59069101/how-to-convert-a-plotly-funnel-dashboard-to-dash-dashboard
    
app = dash.Dash(__name__)

from plotly import graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"],
    x = [39, 27.4, 20.6, 11, 2]))

fig = go.Figure()
fig.add_trace(go.Funnel(
    name = 'Women',
    y = ["Applied", "RSVPd", "Attended"],
    x = [25, 20, 14],
    textinfo = "value+percent initial"))

fig.add_trace(go.Funnel(
    name = 'Men',
    y = ["Applied", "RSVPd", "Attended"],
    x = [49, 35, 26],
    textinfo = "value+percent previous",      
))

app.layout=html.Div([
                    dcc.Graph(
                    id='chart1',
                    figure=fig
                )
        ])


# @app.callback(
#     Output("FunnelDashboard", "figure"), 
#     [Input("names", "value"), 
#      Input("values", "value")])

app.run_server(debug=True)
    
