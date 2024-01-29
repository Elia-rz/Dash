import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Output, Input
import csv
# Define the "Thank You" page layout
layout = dbc.Row(
    dbc.Col(
        dbc.Card(
            [
                dbc.CardHeader(html.H4("Thank you!", className="card-title text-info", style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '30px'})),
                dbc.CardBody(
                    [
                        html.P("If you'd like to receive 80$ Amazon gift card, please enter your email address. ", className="text-dark", style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '18px'}),
                        dbc.Input(type="email", id="email-input", placeholder="Enter your email", style={'fontFamily': 'optima', 'fontSize': '16px'}),
                        html.Br(),
                        dbc.Button("Submit", id="email-submit-button",disabled=True, className="btn btn-info", style={'fontFamily': 'optima', 'fontWeight': 600, 'fontSize': '18px'}),
                        html.Div(id="email-submit-output", className="text-center text-danger", style={'fontFamily': 'optima', 'fontWeight': 500, 'fontSize': '18px'})
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
    Output('email-submit-button', 'disabled'),
    Input('email-input', 'value')
)
def enable_submit_button(email):
    if email and '@' in email and '.' in email:
        return False  # Enable the button
    return True  # Disable the button


@callback(
    Output('email-submit-output', 'children'),
    Input('email-submit-button', 'n_clicks'),
    Input('email-input', 'value'),
    Input('participant-store', 'data'),
)
def save_email(n_clicks, email,code):
    if n_clicks:
        participant_code = code.get('code') if code else None
        filename = f'email_{participant_code}.csv'
        # If email is valid (you can add more validation checks if necessary)
        if '@' in email and '.' in email:
            with open(filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([email])
                return "Thank you! Your email has been saved."
        else:
            return "Please enter a valid email."
    return ""