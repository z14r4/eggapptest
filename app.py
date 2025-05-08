from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Load data
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2],
    "City": ["SF", "SF", "SF"]
})
fig = px.bar(df, x="Fruit", y="Amount", color="City")

# Initialize Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Hello Dash!"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)