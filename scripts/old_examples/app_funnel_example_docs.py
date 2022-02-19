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

# fig = go.Figure(go.Funnel(
#     y = ["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"],
#     x = [39, 27.4, 20.6, 11, 2]))

from plotly import graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"],
    x = [39, 27.4, 20.6, 11, 2]))

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
# def generate_chart(names, values):
#     fig = go.Figure(go.Funnel(
#         names = ["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"],
#         values = [39, 27.4, 20.6, 11, 2]))
#     #fig.update_traces(textposition='inside', textinfo='value+percent+label')
#     return fig

app.run_server(debug=True)
    
# app.layout = html.Div([
#     html.P("Names:"),
#     dcc.Dropdown(
#         id='names', 
#         value='status_c', 
#         options=[{'value': x, 'label': x} 
#                  for x in ['gender', 'contributor_status', 'continent_o', 'country',  'python_experience', 'primary_spoken_language', 'attendance_status','role']],
#         clearable=False
#     ),
#     html.P("Values:"),
#     dcc.Dropdown(
#         id='values', 
#         value='count_rows', 
#         options=[{'value': x, 'label': x} 
#                  for x in ['count_rows']],
#         clearable=False
#     ),
#     dcc.Graph(id="bar-chart"),
# ])

# @app.callback(
#     Output("bar-chart", "figure"), 
#     [Input("names", "value"), 
#      Input("values", "value")])
# def generate_chart(names, values):
#     #fig = px.pie(df, values=values, names=names)
#     #fig.update_traces(textposition='inside', textinfo='value+percent+label')

#     # Try 2: it works
#     #fig = px.bar(df, x=values, y=names, color="status_c", barmode="stack", orientation="h", text=values) 

#     # Try 3: it works with a warning
# #     grouped_yr_status = df.groupby([names,'status_c']).count().reset_index()
# #     df2 = grouped_yr_status[[names, 'status_c', values]] 
# #     fig = px.bar(df2, x=values, y=names, color="status_c", barmode="stack", orientation="h", text=values) 


#     fig = go.Figure()

#     fig.add_trace(go.Funnel(
#         name = 'Women',
#         y = ["Applied", "RSVPd", "Attended"],
#         x = [25, 20, 14],
#         textinfo = "value+percent initial"))

#     fig.add_trace(go.Funnel(
#         name = 'Men',
#         orientation = "h",
#         y = ["Applied", "RSVPd", "Attended"],
#         x = [49, 35, 26],
#         textposition = "inside",
#         textinfo = "value+percent previous",      
#         ))


# app.run_server(debug=True)