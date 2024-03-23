import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1(id="date-time-title"),
        dcc.Interval(id="clock", interval=1000)
    ]
)


app.clientside_callback(
    """
    function(n) {          
        const local_time_str = new Date().toLocaleTimeString();                   
        return "The current time is: " + local_time_str
    }
    """,
    Output('date-time-title', 'children'),
    Input('clock', 'n_intervals'),
)



if __name__ == "__main__":
    app.run_server(debug=True)