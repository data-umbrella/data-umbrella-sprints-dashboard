import dash
#import dash_core_components as dcc
from dash import dcc
from dash import html
#import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
from plotly import graph_objects as go
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
    dbc.Row([dbc.Col(html.H4("Dimensions:"), width=3),
             dbc.Col(dcc.Dropdown(
        id='names_bar',
        value='gender',
        options=[{'value': x, 'label': x} 
                 for x in ['gender', 'contributor_status', 'continent_o', 'country',  'python_experience', 'primary_spoken_language', 'attendance_status','role']],
        clearable=False
             )),
        dbc.Col(html.H4("Count:"), width=3),
        dbc.Col(dcc.Dropdown(
            id='values_bar',
            value='count_rows',
            options=[{'value': x, 'label': x} 
                 for x in ['count_rows']],
            clearable=False), width=3
            )
    ])
    ,html.P(html.Br()),
    dcc.Graph(id="bar-chart"),
])

# funnel_div = dbc.Row([  
#     dcc.Graph(id='FunnelDashboard',
#                     figure = {'data':[
#                             go.Funnel(
#                             name = "xxx",
#                             y = ["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"],
#                             x = [39, 27.4, 20.6, 11, 2],
#                             textinfo = "value+percent previous"
#                             )],
                    
#                             }
#                             )])
# ])
# app.layout=html.Div([
#                     dcc.Graph(
#                     id='chart1',
#                     figure=fig
#                 )
#         ])

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
    textinfo = "value+percent previous",))

funnel_div = dbc.Row([
    dbc.Row([dbc.Col(html.H4("Dimensions:"), width=3),
             dcc.Graph(figure=fig)
             ])
])

variable = "attendance_status"

df['text'] = df['city'] + ', ' 
+ df['state-province'] + ', ' 
+ df['country'] + ', '
+ df['continent_o'] 

fig2 = px.scatter_geo(df, 
                     #locations="iso_alpha", 
                     lat = "lat",
                     lon = "lng",
                     color=variable,
                     hover_name="location", 
                     #hover_name="country", 
                     hover_data=["country","state-province"],
                     #text="text",
                     #size="members_followers",
                     #mode = "markers",
                     #marker = dict(
                     #           size = 8,
                     #           opacity = 0.8,
                     #           reversescale = True,
                     #           autocolorscale = False,
                     #           symbol = 'square',
                     #),
                     projection="natural earth",
                     title=f"Chart: Geomap of {variable}",
                    )

fig2.update_geos(
    visible=True, resolution=50,
    showcountries=True, countrycolor="LightYellow"
)
fig2.update_layout(height=600, margin={"r":10,"t":0,"l":10,"b":0})
fig2.update_traces(marker_symbol=["circle-x","circle-open-dot","circle-dot"]
                  , selector=dict(type='scattergeo'))


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
        ]),
    dbc.Row([
        dcc.Graph(figure=fig),
        #dcc.Col(funnel_div, width=6)
        ]),
    dbc.Row([
        dcc.Graph(figure=fig2),
        #dcc.Col(funnel_div, width=6)
        ]),
    ])


# PIE CHART
@app.callback(
    Output("pie-chart", "figure"), 
    [Input("names", "value"), 
     Input("values", "value")])
def generate_chart(names, values):
    fig = px.pie(df, values=values, names=names, template=template)
    fig.update_traces(textposition='inside', textinfo='value+percent+label')
    return fig

# BAR CHART
@app.callback(
    Output("bar-chart", "figure"), 
    [Input("names_bar", "value"), 
     Input("values_bar", "value")])
def generate_chart(names, values):
    # Try 4: try to remove warning
    grouped_yr_status = df.groupby([names, 'status_c']).count().reset_index()
    df2 = grouped_yr_status[[names, 'status_c', values]] 
    fig = px.bar(df2, x=values, y=names, color="status_c", 
                barmode="stack", orientation="h", text=values, template=template) 
    
    fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
    return fig

app.run_server(debug=True)

# app.layout=html.Div([
#                     dcc.Graph(
#                     id='chart1',
#                     figure=fig
#                 )
#         ])
# FUNNEL CHART
# @app.callback(
#     Output("chart1", "figure"), 
#     [Input("y", "value"), 
#      Input("x", "value"),
#      Input("name", "value"),
#      Input("textinfo", "value")
#      ])
# def generate_chart(names, values):
#     # Try 4: try to remove warning
#     #grouped_yr_status = df.groupby([names, 'status_c']).count().reset_index()
#     #df2 = grouped_yr_status[[names, 'status_c', values]] 
#     #fig = px.bar(df2, x=values, y=names, color="status_c", barmode="stack", orientation="h", text=values) 
    
#     #fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})

#     fig = go.Figure(go.Funnel(
#         y = ["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"],
#         x = [39, 27.4, 20.6, 11, 2]))

#     fig = go.Figure()
#     fig.add_trace(go.Funnel(
#         name = 'Women',
#         y = ["Applied", "RSVPd", "Attended"],
#         x = [25, 20, 14],
#         textinfo = "value+percent initial"))

#     fig.add_trace(go.Funnel(
#         name = 'Men',
#         y = ["Applied", "RSVPd", "Attended"],
#         x = [49, 35, 26],
#         textinfo = "value+percent previous",))
#     return fig

