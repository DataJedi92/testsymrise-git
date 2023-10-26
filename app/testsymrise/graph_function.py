import plotly.graph_objects as go

def correlation_heatmap(dataframe):

    fig = go.Figure(data=[go.Scatter(
        x=[dataframe.collect()[0][1], dataframe.collect()[1][1], dataframe.collect()[2][1]],
        y=[dataframe.collect()[0][2], dataframe.collect()[1][2], dataframe.collect()[2][2] ],
        text = ['Berlin','Koln', 'Munich'],
        mode='markers',
        marker_size=[10, 10, 10])
    ])

    fig.show()
