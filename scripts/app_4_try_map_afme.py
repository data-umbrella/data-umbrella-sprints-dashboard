import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go # or plotly.express as px
import pandas as pd

data_url = "https://raw.githubusercontent.com/data-umbrella/data-umbrella-sprints-dashboard/main/data/data_derived/afme2_derived.csv"
df_location = pd.read_csv(data_url)


#fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )


variable = "attendance_status"

df_location['text'] = df_location['city'] + ', ' 
+ df_location['state-province'] + ', ' 
+ df_location['country'] + ', '
+ df_location['continent_o'] 

fig = px.scatter_geo(df_location, 
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

fig.update_geos(
    visible=True, resolution=50,
    showcountries=True, countrycolor="LightYellow"
)
fig.update_layout(height=600, margin={"r":10,"t":0,"l":10,"b":0})
fig.update_traces(marker_symbol=["circle-x","circle-open-dot","circle-dot"]
                  , selector=dict(type='scattergeo'))


app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True)  # Turn off reloader if inside Jupyter




# df = px.data.election()
# geojson = px.data.election_geojson()
# candidates = df.winner.unique()

# app = dash.Dash(__name__)

# app.layout = html.Div([
#     html.P("Candidate:"),
#     dcc.RadioItems(
#         id='candidate', 
#         options=[{'value': x, 'label': x} 
#                  for x in candidates],
#         value=candidates[0],
#         labelStyle={'display': 'inline-block'}
#     ),
#     dcc.Graph(id="choropleth"),
# ])

# @app.callback(
#     Output("choropleth", "figure"), 
#     [Input("candidate", "value")])
# def display_choropleth(candidate):
#     fig = px.choropleth(
#         df, geojson=geojson, color=candidate,
#         locations="district", featureidkey="properties.district",
#         projection="mercator", range_color=[0, 6500])
#     fig.update_geos(fitbounds="locations", visible=False)
#     fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#     return fig

# app.run_server(debug=True)