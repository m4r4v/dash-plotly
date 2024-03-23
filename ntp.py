import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from ntplib import NTPClient
from datetime import datetime, timezone

import dash
from dash import html
from dash.dependencies import Input, Output
from ntplib import NTPClient
from datetime import datetime
import pytz

app = dash.Dash(__name__)

ntp_client = NTPClient()
desired_timezone = pytz.timezone('America/Santiago')  # Choose your desired timezone

app.layout = html.Div([
    html.H1("NTP Digital LED Clock", style={'textAlign': 'center'}),
    html.Div(id='live-clock', style={'fontSize': 48, 'textAlign': 'center'}),
    html.Div(id='hidden-div', style={'display': 'block'}),
    dcc.Interval(
        id='interval-component',
        interval=1000,  # in milliseconds
        n_intervals=0
    )
])

@app.callback(
    Output('live-clock', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_clock(n):
    response = ntp_client.request('ntp.shoa.cl', version=3)
    utc_time = datetime.fromtimestamp(response.tx_time, pytz.utc)
    local_time = utc_time.astimezone(desired_timezone)
    formatted_time = local_time.strftime("%H:%M:%S")
    return formatted_time

if __name__ == '__main__':
    app.run_server(debug=True)

