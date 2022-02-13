import pandas as pd
import plotly.express as px


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
        
        
if __name__ == '__main__':  
      
    # Read the data into a dataframe 
    url = 'https://raw.githubusercontent.com/data-umbrella/data-umbrella-sprints-dashboard/main/data/afme2_final.csv'
    data_afme2 = pd.read_csv(url, index_col=0)

    # See the first few rows
    #display(data_afme2.head(1))
    
    # Plot:
    df_use = group_data(data_afme2, ['country'])
    graph_region(df_use, 'bar', "count_rows", "country",  "status_c")
    
#     # Plot:
     df_use = group_data(data_afme2, ['gender'])
     graph_region(df_use, 'bar', "gender", "count_rows", "status_c")
    
#     # Plot:
#     df_use = group_data(data_afme2, ['learn_of_sprint'])
#     graph_region(df_use, 'bar', "learn_of_sprint", "count_rows", "status_c")
    
#     # Plot:
#     df_use = group_data(data_afme2, ['role'])
#     graph_region(df_use, 'bar', "role", "count_rows", "status_c")

      # Plot
#     df_use = group_data(data_afme2, ['contributor_status'])
#     graph_region(df_use, 'bar', "count_rows", "contributor_status",  "status_c")
    