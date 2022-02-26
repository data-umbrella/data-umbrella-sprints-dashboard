import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# https://dash-bootstrap-components.opensource.faculty.ai/docs/components/tabs
# check version of library
# https://dash.gallery/Portal/
# https://plotly.com/python/templates/
# https://github.com/plotly/dash-sample-apps/tree/main/apps/dash-opioid-epidemic
# Bootstrap themes: https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/explorer/
# Layout:  https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/

# to do:  play with layout
# bar: give a default value
# add a title at the top
# id once per sheet
# do one copy/ paste at a time
# stylesheets:  https://bootswatch.com/
# ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]

template = "seaborn"
external_stylesheets = [dbc.themes.BOOTSTRAP, dbc.themes.SOLAR]

data_url = "https://raw.githubusercontent.com/data-umbrella/data-umbrella-sprints-dashboard/main/data/data_derived/afme2_derived.csv"
df = pd.read_csv(data_url)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


pie_div = dbc.Row([
    dbc.Row([dbc.Col(html.H4("Dimensions:"), width=3), 
             dbc.Col(dcc.Dropdown(
        id='names', 
        value='status_c', 
        options=[{'value': x, 'label': x} 
                 for x in ['gender', 'contributor_status', 'status_c','continent_o', 'python_experience', 'country']],
        clearable=False
    )),
         dbc.Col(html.H4("Count:"), width=3),
             dbc.Col(dcc.Dropdown(
        id='values', 
        value='count_rows', 
        options=[{'value': x, 'label': x} 
                 for x in ['count_rows']],
        clearable=False), width=3
                    )    
    ])
    ,html.P(html.Br()), 
    dcc.Graph(id="pie-chart"),
])

bar_div = dbc.Row([
    html.P("Names:"),
    dcc.Dropdown(
        id='names_bar', 
        value='gender', 
        options=[{'value': x, 'label': x} 
                 for x in ['gender', 'contributor_status', 'continent_o', 'country',  'python_experience', 'primary_spoken_language', 'attendance_status','role']],
        clearable=False
    ),
    html.P("Values:"),
    dcc.Dropdown(
        id='values_bar', 
        value='count_rows', 
        options=[{'value': x, 'label': x} 
                 for x in ['count_rows']],
        clearable=False
    ),
    dcc.Graph(id="bar-chart"),
])

# row = html.Div(
# [
# dbc.Row(dbc.Col(html.Div("A single column"))),
# dbc.Row(
# [
# dbc.Col(html.Div("One of three columns")),
# dbc.Col(html.Div("One of three columns")),
# dbc.Col(html.Div("One of three columns")),
# ]
# ),
# ]
# )

app.layout = html.Div([ 
    dbc.Row([
        dbc.Col(html.H1("Pie Chart"), width=6), 
        dbc.Col(html.H1("Bar Chart"), width=6)
        ]), 
    dbc.Row([
        dbc.Col(pie_div, width=6), 
        dbc.Col(bar_div, width=6)
        ]),
    dbc.Row([
        dbc.Col(html.H1("Funnel Chart"), width=6),
        dbc.Col(html.H1("Map"), width=6)
        ])
    ])


@app.callback(
    Output("pie-chart", "figure"), 
    [Input("names", "value"), 
     Input("values", "value")])
def generate_chart(names, values):
    fig = px.pie(df, values=values, names=names, template=template)
    fig.update_traces(textposition='inside', textinfo='value+percent+label')
    return fig

@app.callback(
    Output("bar-chart", "figure"), 
    [Input("names_bar", "value"), 
     Input("values_bar", "value")])
def generate_chart(names, values):
    # Try 4: try to remove warning
    grouped_yr_status = df.groupby([names, 'status_c']).count().reset_index()
    df2 = grouped_yr_status[[names, 'status_c', values]] 
    fig = px.bar(df2, x=values, y=names, color="status_c", barmode="stack", orientation="h", text=values) 
    
    fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
    return fig

app.run_server(debug=True)