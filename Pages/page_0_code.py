import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Output, Input, State

# Define the "Thank You" page layout
layout = dbc.Row(
    dbc.Col(
        dbc.Card(
            [
                dbc.CardHeader(html.H4("Welcome to our experiment!", className="card-title text-info", style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '30px'})),
                dbc.CardBody(
                    [
                        html.P("Please enter the unique participant code provided to you in the email.", className="text-dark", style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '18px'}),
                        dbc.Input(type="code", id="participant_code", placeholder="Enter Your Participant Code", style={'fontFamily': 'optima', 'fontSize': '16px'}),
                        html.Br(),
                        dbc.Button("Submit", id="code-submit-button",href = "/page_0_consent",n_clicks=0,disabled= True, className="btn btn-info", style={'fontFamily': 'optima', 'fontWeight': 600, 'fontSize': '18px'}),
                        html.Div(id="code-submit-output", className="text-center text-info", style={'fontFamily': 'optima', 'fontWeight': 500, 'fontSize': '18px'})
                    ]
                ),
            ],
            className="card border-info mb-3",style={'width': '100%', 'margin-top': '200px'}
        ),
        width={'size': 6},
    ),
    justify='center',
    style={'margin-top': '10px'}
)

@callback(
    Output('code-submit-button', 'disabled'),
    Input('participant_code', 'value')
)
def enable_submit_button(input_value):
    return not bool(input_value)


# Callback to save the participant code to the dcc.Store
@callback(
    Output('participant-store', 'data'),
    Input('participant_code', 'value'),
)
def save_code(code_value):
    return {'code': code_value}
