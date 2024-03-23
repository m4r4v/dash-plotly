import dash
from dash import html, dcc, Input, Output, callback
from ntplib import NTPClient
from datetime import datetime, timezone
import pytz


# definimos algunas variables
ntp_shoa = NTPClient()
default_timezone = pytz.timezone('America/Santiago')

external_stylesheets = [
    "https://fonts.googleapis.com/css2?family=Dosis:wght@200..800&family=Inconsolata:wght@200..900&display=swap"
]

# paso 1: se nombra la app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# paso 2: se genera el layout (canvas)
app.layout = html.Div(
    [
        html.H1(
            "Hora NTP Shoa", 
            style={
                'text-align': 'center',
                'color': '#ffffff',
                'padding': '1rem 1rem 1rem 2rem',
                'font-family': '"Inconsolata',
                'font-weight': 300,
                'font-style': 'normal',
                'text-transform': 'uppercase'
            },
        ),
        html.Div(
            id='reloj-ntp',
            style={
                'font-size': '5rem',
                'text-align': 'center',
                'color': '#00BFFF',
                'font-family': 'Inconsolata',
                'font-weight': 'bold',
                'font-style': 'normal',
            }
        ),
        html.Div(
            id='hidden-div',
            style={
                'display': 'none'
            }
        ),
        dcc.Interval(
            id='interval-component',
            interval=1000,
            n_intervals=0
        )
    ],
    style={
        'border': '1px solid #6495ED',
        'border-radius': '0.2rem',
        'margin': '0',
        'background-color': '#222222',
        'padding-bottom': '3rem'
    }
)



@app.callback(
    Output('reloj-ntp', 'children', allow_duplicate=True),
    Input('interval-component', 'n_intervals'),
    prevent_initial_call=True
)

def update_clock(n):
    response = ntp_shoa.request('ntp.shoa.cl')
    utc_time = datetime.fromtimestamp(response.tx_time, pytz.utc)
    local_time = utc_time.astimezone(default_timezone)
    formatted_time = local_time.strftime("%H:%M:%S")
    return formatted_time


# correr el servidor web
if __name__ == '__main__':
    app.run(debug=True)
