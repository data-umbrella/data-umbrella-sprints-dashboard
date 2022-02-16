
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


def group_data(df_use, byvar):
    byvar_list = byvar 
    byvar_list.append("status_c")
    df_grouped = df_use.groupby(byvar_list).count()
    df_grouped = df_grouped.reset_index()

    byvar_list.append("count_rows")
    df_use = df_grouped[byvar_list]

    return df_use


def graph_region(region_df, graph_type: str, dimension1: str, dimension2: str, dimension3: str) -> None:
    """
    Parameters
    ----------
        region_df: (dataframe object) reshaped data frame object with mortage, delinquency and population data
        graph_type: (string) "box", "violin", "scatter", "line", "pie", "bar", "funnel", "scatter_geo"
        dimension1: (str) one of 'Time' or 'Geography'
        dimension2: (str) one of 'AverageMortgageAmount', 'AverageMortgageAmount' or 'PopulationSize'
        
    Returns:
    --------
        None
    """
    
    # Dictionary of plots
    plot_dict = {'box': px.box, 
                 'violin': px.violin,
                 'scatter': px.scatter,
                 'line': px.line,
                 'pie': px.pie,
                 'bar': px.bar,
                 'funnel': px.funnel,
                 'scatter_geo': px.scatter_geo,
                 }
        
    try:
        fig = plot_dict[graph_type](region_df, 
                                     x=dimension1, 
                                     y=dimension2, 
                                     color = dimension3,
                                     hover_name = dimension3,
                                     text=dimension1,
                                     #extposition='inside',
                                     orientation='h',
                                   )
            
        # Format figure 
        title_string = f'Chart: {graph_type} plot of {dimension1} and {dimension2} by {dimension3}'
        fig.update_layout(title = title_string)
        #fig.update_xaxes(tickangle=-45)
        #fig.update_layout(yaxis_categoryorder='category ascending')
        fig.update_layout(barmode='stack', 
                  yaxis={'categoryorder':'total ascending'})
        fig.show()
    
    except KeyError:
        print("Key not found. Make sure that 'graph_type' is in ['box','violin', 'scatter', 'line', 'pie', 'bar','funnel', 'scatter_geo']")
    except ValueError:
        print("Dimension is not valid. dimension1 is one of 'Time' or 'Geography'")
        print("dimension2 is one of 'AverageMortgageAmount', 'DelinquencyRate', 'PopulationSize'")
        

# ----------------------------------------------------------------------------------#

# Read the data into a dataframe 
url = 'https://raw.githubusercontent.com/data-umbrella/data-umbrella-sprints-dashboard/main/data/afme2_final.csv'
data_afme2 = pd.read_csv(url, index_col=0)

    
# ----------------------------------------------------------------------------------#
# App section        
        

# Stylesheets
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Intialize app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server


# ----------------------------------------------------------------------------------#
# A dropdown menu and a chart

app.layout = html.Div([
             # This div contains a header H1, a dropdown to select the kind of plot and the plot
            html.H1("Different kinds of plots"),
            dcc.Dropdown(
                        id='graph-type',
                        options=[{'label': 'Violin plot', 'value': 'violin'},
                                 {'label': 'Box plot', 'value': 'box'},
                                 {'label': 'Bar plot', 'value': 'bar'}
                                ],
                        value= 'bar'),
            dcc.Graph(id='graph-render')

        
])

@app.callback(
    Output('graph-render', 'figure'),
    Input('graph-type', 'value'))

def update_figure0(selected_graph):
#    filtered_df = data_pop_del_mort_df
#    fig0 = graph_region(filtered_df, selected_graph, "Geography", "AverageMortgageAmount")
#    return fig0

    df_use = group_data(data_afme2, ['country'])
    graph_region(df_use, 'bar', "count_rows", "country",  "status_c")
    

    # See the first few rows
    #display(data_afme2.head(1))
    
#     # Plot:
#     df_use = group_data(data_afme2, ['country'])
#     graph_region(df_use, 'bar', "count_rows", "country",  "status_c")
    
#     # Plot:
#     df_use = group_data(data_afme2, ['gender'])
#     graph_region(df_use, 'bar', "count_rows", "gender",  "status_c")

#     # Plot
#     df_use = group_data(data_afme2, ['contributor_status'])
#     graph_region(df_use, 'bar', "count_rows", "contributor_status",  "status_c")

#     # Plot:
#     df_use = group_data(data_afme2, ['learn_of_sprint'])
#     graph_region(df_use, 'bar', "learn_of_sprint", "count_rows", "status_c")
    
#     # Plot:
#     df_use = group_data(data_afme2, ['role'])
#     graph_region(df_use, 'bar', "role", "count_rows", "status_c")


# ----------------------------------------------------------------------------------#

    
# ----------------------------------------------------------------------------------#
# Improving aesthetics, dropdown that changes three graphs

# app.layout = html.Div([
#     html.Div(
#         className="six columns",
#         children = [
#             html.H1("Housing graphs"),
#                 dcc.Dropdown(
#                     id='province',
#                     options=[{'label': i, 'value': i} for i in data_pop_del_mort_df['Geography'].unique()],
#                     value= 'Newfoundland'
#                 ),
            
#             html.Div([
#                    dcc.Graph(id='graph-time-mortgage')
#                     ], className="six columns"),
            
#             html.Div([
#                 dcc.Graph(id='graph-time-del')
#                 ], className="six columns"),
            
#             ]),
    
#     html.Div(
#         className="six columns",
#         children = [
#             html.Div([
#             dcc.Graph(id='scatter-mortgage-del')
#             ]),
#         ])
# ])


    
# @app.callback(
#     Output('graph-time-mortgage', 'figure'),
#     Input('province', 'value'))
# def update_figure1(selected_province):
#     df = data_pop_del_mort_df
#     filtered_df = df[df['Geography'] == selected_province]
#     fig1 = graph_region(filtered_df, 'line', "Time", "AverageMortgageAmount")
#     return fig1

# @app.callback(
#     Output('graph-time-del', 'figure'),
#     Input('province', 'value'))
# def update_figure2(selected_province):
#     df = data_pop_del_mort_df
#     filtered_df = df[df['Geography'] == selected_province]  
#     fig2 = graph_region(filtered_df, 'line', "Time", "DelinquencyRate")
#     return fig2

# @app.callback(
#     Output('scatter-mortgage-del', 'figure'),
#     Input('province', 'value'))
# def update_figure3(selected_province):
#     df = data_pop_del_mort_df
#     filtered_df = df[df['Geography'] == selected_province]  
#     fig3 = graph_region(filtered_df, 'scatter', "AverageMortgageAmount", "DelinquencyRate")
#     return fig3

# ----------------------------------------------------------------------------------#
# text_style = {
#     'textAlign' : 'center',
#     'color' : "black"
# }

# card_text_style = {
#     'textAlign' : 'center',
#     'color' : 'black'
# }
    
# app.layout = html.Div([
#     html.Div([
#         html.H2("Housing Market Trends in Vancouver (quarterly, 2012 - 2020)", style=card_text_style),
#         html.Div([
            
#             dcc.Dropdown(
#                 id='xaxis-column',
#                 options=[{'label': 'Geography', 'value': 'Geography'},
#                          {'label': 'Time', 'value': 'Time'},
#                         {'label': 'Population Size', 'value': 'PopulationSize'},
#                          {'label': 'Delinquency Rate', 'value': 'DelinquencyRate'},
#                         {'label': 'Average Mortgage Amount', 'value': 'AverageMortgageAmount'}],
#                 value='Geography'
#             ),
#             dcc.Dropdown(
#                 id='yaxis-column',
#                 options=[{'label': 'Population Size', 'value': 'PopulationSize'},
#                          {'label': 'Delinquency Rate', 'value': 'DelinquencyRate'},
#                         {'label': 'Average Mortgage Amount', 'value': 'AverageMortgageAmount'}],
#                 value='PopulationSize'
#             ),
            
#         ]),
        
#         html.Div([
#             dcc.Checklist(
#                 id='graph-type',
#                 options=[{'label': 'Violin plot', 'value': 'violin'},
#                          {'label': 'Box plot', 'value': 'box'},
#                         {'label': 'Scatter plot', 'value': 'scatter'},
#                         {'label': 'Line plot', 'value': 'line'}],
#                 value=['violin']
#             )
#         ])
#     ]),

#     dcc.Graph(id='indicator-graphic'),

    
# ])

# @app.callback(
#     Output('indicator-graphic', 'figure'),
#     Input('graph-type', 'value'),
#     Input('xaxis-column', 'value'),
#     Input('yaxis-column', 'value'))
# def update_figure3(selected_graph, xaxis, yaxis):
#     filtered_df = data_pop_del_mort_df
#     fig3 = graph_region(filtered_df, selected_graph[0], xaxis, yaxis)
#     return fig3

# ----------------------------------------------------------------------------------#

if __name__ == '__main__':  
    
    app.run_server(debug=True) 