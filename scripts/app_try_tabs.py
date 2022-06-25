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

# FUNNEL CHART
fig_funnel = go.Figure()
fig_funnel.add_trace(go.Funnel(
    name = 'Women',
    y = ["Applied", "RSVPd", "Attended"],
    x = [25, 20, 14],
    textinfo = "value+percent initial"))

fig_funnel.add_trace(go.Funnel(
    name = 'Men',
    y = ["Applied", "RSVPd", "Attended"],
    x = [49, 35, 26],
    textinfo = "value+percent previous",))

funnel_div = dbc.Row([
    dbc.Row([dbc.Col(html.H4("Dimensions:"), width=3),
             dcc.Graph(figure=fig_funnel)
             ])
])

# MAP
variable = "attendance_status"

df['text'] = df['city'] + ', ' + df['country'] + ', '
#+ df['state-province'] + ', ' 
#+ df['continent_o'] 

fig_map = px.scatter_geo(df, 
                     #locations="iso_alpha", 
                     lat = "lat",
                     lon = "lng",
                     color=variable,
                     hover_name="city", #"location", 
                     #hover_name="country", 
                     hover_data=["city", "country","continent_o"],
                     #hover_data=["text"],
                     #text="city",
                     #text = dict (
                     #    size=8,
                     #)
                     #size=8,
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

fig_map.update_geos(
    visible=True, resolution=50,
    showcountries=True, countrycolor="LightYellow"
)
fig_map.update_layout(height=600, margin={"r":10,"t":0,"l":10,"b":0})
fig_map.update_traces(marker_symbol=["circle-x","circle-open-dot","circle-dot"]
                  , selector=dict(type='scattergeo'))

card = dbc.Card(
    [
    dbc.CardHeader(
        dbc.Tabs(
                [
                    dbc.Tab(label="AFME2 (Oct 2021)", tab_id="AFME2", tab_style={"marginLeft": "left"}),
                    dbc.Tab(label="Tab 2", tab_id="tab-2", label_style={"color": "#00AEF9"}),
                ],
                id="card-tabs",
                active_tab="tab-1",
            ),
        ),
    html.Br(),
        #     dbc.Tabs(
        #     [
        #         dbc.Tab(label="Tab 1", activeTabClassName="fw-bold fst-italic"),
        #         dbc.Tab(label="Tab 2", activeLabelClassName="text-success"),
        #     ]
        # ),
    dbc.CardBody(html.P(id="card-content", className="card-text")
        ),
    dbc.CardBody(
        [
            html.H4("Data Umbrella", id="card-title"),
            html.H2("Africa & Middle East scikit-learn Sprint", id="card-value"),
            html.P("October 2021", id="card-description")
        ]
                )
    ],
)
app.layout = html.Div([ 
    dbc.Row([
        dbc.Col([card], width=12),
        ],
        align="center",
        justify="center"),
    dbc.Row([
        dbc.Col(html.H1("Pie Chart"), width=4), 
        dbc.Col(html.H1("Bar Chart"), width=4),
        ],
        align="center",
        justify="center"), 
    dbc.Row([
        dbc.Col(pie_div, width=4), 
        dbc.Col(bar_div, width=4)
        ],
        align="center",
        justify="center"), 
    # dbc.Row([
    #     dbc.Col(
    #             html.Div("A single, half-width column"),
    #             width={"size": 6, "offset": 3},
    #         ),
    #     dbc.Col(html.H1("Funnel Chart"), width=4),
    #     ],
    #     align="center",
    #     justify="center"),
    dbc.Row([
        dbc.Col(html.H1("Funnel Chart"), width=4), 
        dbc.Col(html.H1("Map"), width=4),
        ],
        align="center",
        justify="center"), 
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_funnel), width=4),
        dbc.Col(dcc.Graph(figure=fig_map), width=4),
        ],
        align="center",
        justify="center"),
    # dbc.Row([
    #     dbc.Col(html.H1("Map"), width={"size": 6, "offset": 3})
    #     ]),      
    # dbc.Row([
    #     dcc.Graph(figure=fig_map),
    #     ]),
    ],
    className="pad-row",
)


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

@app.callback(
    Output("card-content", "children"), [Input("card-tabs", "active_tab")]
)
def tab_content(active_tab):
    return "This is tab: {}".format(active_tab)

app.run_server(debug=True)
