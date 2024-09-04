import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go

def fibonacci(Nterms: int, N1: int, N2: int):
    fibonacci_sequence = []
    Count = 0
    # check if the number of terms is valid
    if Nterms <= 0:
        return "Please enter a positive integer"

    # if there is only one term, return n1
    elif Nterms == 1:
        fibonacci_sequence.append(N1)
    # generate fibonacci sequence
    else:
        while Count < Nterms:
            fibonacci_sequence.append(N1)
            Nth = N1 + N2
            N1 = N2
            N2 = Nth
            Count += 1

    return fibonacci_sequence

# Generate Fibonacci sequences
nterms_10 = 10
nterms_50 = 50
fibonacci_10 = fibonacci(nterms_10, 0, 1)
fibonacci_50 = fibonacci(nterms_50, 0, 1)

# Create bar charts using Plotly
fig_10 = go.Figure(data=[go.Bar(x=list(range(1, nterms_10 + 1)), y=fibonacci_10)])
fig_10.update_layout(title='Fibonacci Sequence (10 terms)', xaxis_title='Term', yaxis_title='Value')

fig_50 = go.Figure(data=[go.Bar(x=list(range(1, nterms_50 + 1)), y=fibonacci_50)])
fig_50.update_layout(title='Fibonacci Sequence (50 terms)', xaxis_title='Term', yaxis_title='Value')

# Create Dash application
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Fibonacci Sequence Bar Charts'),

    html.Div(children='''
        Bar chart for 10 terms:
    '''),

    dcc.Graph(
        id='fibonacci-10',
        figure=fig_10
    ),

    html.Div(children='''
        Bar chart for 50 terms:
    '''),

    dcc.Graph(
        id='fibonacci-50',
        figure=fig_50
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)