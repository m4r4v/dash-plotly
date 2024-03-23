import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from datetime import datetime
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Interactive Clock"),
    html.Div(id='live-clock'),
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
    if n == 0:
        raise PreventUpdate
    else:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"Current Time: {current_time}"

if __name__ == '__main__':
    app.run_server(debug=True)
