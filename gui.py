import dash
from dash import dcc
from dash import html

from dash.dependencies import Input, Output

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    children=[
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ]
)

# Callback to update page based on URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return html.Div(
            children=[
                html.H1("🎉 Dinner Party Games 🎉", style={"textAlign": "center"}),  # Centering the main title
                html.Div(
                    children=[
                        html.H3("🎲 Choose Your Game 🎲"),
                        html.Div(
                            children=[
                                dcc.Link("Three Things Game", href='/three-things-game', style={"marginRight": "10px"}),
                                dcc.Link("Ratings Game", href='/ratings-game', style={"marginRight": "10px"})
                            ],
                            style={"textAlign": "center", "marginTop": "20px"}
                        )
                    ],
                    style={"maxWidth": "600px", "margin": "auto", "textAlign": "center"}
                ),
            ]
        )
    elif pathname == '/three-things-game':
        return html.Div([
            html.H1('🤔 Three Things Game 🤔', style={"textAlign": "center"}),
            html.Div([
                html.Button("👥 Team 1", id="btn-team-1", n_clicks=0, style={"marginRight": "10px"}),
                html.Button("👥 Team 2", id="btn-team-2", n_clicks=0, style={"marginRight": "10px"}),
                html.Button("👥 Team 3", id="btn-team-3", n_clicks=0)
            ], style={"textAlign": "center", "marginTop": "20px"}),
            html.Div([
                dcc.Link('🔙 Back', href='/')
            ], style={"textAlign": "center", "marginTop": "20px"})
        ])
    elif pathname == '/ratings-game':
        return html.Div([
            html.H1('📊 Ratings Game 📊', style={"textAlign": "center"}),
            html.Div([
                dcc.Link('🔙 Back', href='/')
            ], style={"textAlign": "center", "marginTop": "20px"})
        ])
    else:
        return '🚫 404 Page Not Found 🚫'


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)


