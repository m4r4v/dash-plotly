import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from datetime import datetime
import plotly.graph_objs as go
import numpy as np

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Analog Clock", style={'textAlign': 'center'}),
    dcc.Graph(id='live-clock'),
    dcc.Interval(
        id='interval-component',
        interval=1000,  # in milliseconds
        n_intervals=0
    )
])

@app.callback(
    Output('live-clock', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_clock(n):
    current_time = datetime.now()
    hour = current_time.hour % 12
    minute = current_time.minute
    second = current_time.second

    # Calculate the angles for the clock hands
    hour_angle = 90 - 30 * hour - minute / 2
    minute_angle = 90 - 6 * minute - second / 10
    second_angle = 90 - 6 * second

    # Create clock face
    clock_face = go.Scatter(
        x=[0],
        y=[0],
        mode='markers',
        marker=dict(
            size=6,
            color='black'
        ),
        showlegend=False
    )

    # Create hour hand
    hour_hand = go.Scatter(
        x=[0, 0.3 * np.cos(np.radians(hour_angle - 90))],
        y=[0, 0.3 * np.sin(np.radians(hour_angle - 90))],
        mode='lines',
        line=dict(
            color='blue',
            width=6
        ),
        showlegend=False
    )

    # Create minute hand
    minute_hand = go.Scatter(
        x=[0, 0.5 * np.cos(np.radians(minute_angle - 90))],
        y=[0, 0.5 * np.sin(np.radians(minute_angle - 90))],
        mode='lines',
        line=dict(
            color='green',
            width=4
        ),
        showlegend=False
    )

    # Create second hand
    second_hand = go.Scatter(
        x=[0, 0.7 * np.cos(np.radians(second_angle - 90))],
        y=[0, 0.7 * np.sin(np.radians(second_angle - 90))],
        mode='lines',
        line=dict(
            color='red',
            width=2
        ),
        showlegend=False
    )

    # Create layout
    layout = go.Layout(
        xaxis=dict(
            visible=False,
            range=[-1, 1]
        ),
        yaxis=dict(
            visible=False,
            range=[-1, 1]
        ),
        shapes=[
            dict(
                type='circle',
                xref='x',
                yref='y',
                x0=-1,
                y0=-1,
                x1=1,
                y1=1,
                line=dict(
                    color='black',
                    width=2
                )
            )
        ],
        margin=dict(l=20, r=20, t=20, b=20),
        hovermode=False,
        title=f"Current Time: {current_time.strftime('%H:%M:%S')}",
        title_x=0.5,  # Set the title position
        title_y=0.9
    )

    return {
        'data': [clock_face, hour_hand, minute_hand, second_hand],
        'layout': layout
    }

if __name__ == '__main__':
    app.run_server(debug=True)
