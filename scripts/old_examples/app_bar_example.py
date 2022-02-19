import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

df = px.data.tips()
days = df.day.unique()

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} for x in days],
        value=days[0],
        clearable=False,
    ),
    dcc.Graph(id="bar-chart"),
])

@app.callback(
    Output("bar-chart", "figure"), 
    [Input("dropdown", "value")])
def update_bar_chart(day):
    mask = df["day"] == day
    fig = px.bar(df[mask], x="total_bill", y="sex", 
                 color="smoker", barmode="group",
                orientation='h',)
    #title_string = f'Chart: {graph_type} plot of {dimension1} and {dimension2} by {dimension3}'
    #fig.update_layout(title = title_string)
    fig.update_layout(barmode='stack', 
    yaxis={'categoryorder':'total ascending'})
    
    return fig

app.run_server(debug=True)