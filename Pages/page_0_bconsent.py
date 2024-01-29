import dash
from dash import dcc, html, callback, Output, Input, State
import dash_bootstrap_components as dbc
from dash import no_update
from dash_canvas import DashCanvas
from dash_iconify import DashIconify
import csv
import random
import os

# dash.register_page(__name__,path='/', name='Consent Form')


layout = dbc.Row(
    dbc.Col(

        dbc.Card(
            [
                dbc.CardHeader([html.H4("Consent Form", className="card-title text-info",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '40px'}),
                               html.H4("*Please read the following form carefully. If you agree with all the terms and conditions, please check the box at the end of the page.",
                                      className="card-title text-danger",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '14px'})]),
                dbc.CardBody(
                    dbc.Container(
                        [
                            html.H1("Trust in Diagnosis Support Systems", className="text-secondary text-center",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '30px'}),
                            html.P("Alparslan Emrah Bayrak, Ph.D., and associates from the School of Systems and Enterprises at the Trustees of the Stevens Institute (SIT) are conducting a research study.You were selected as a possible participant in this study because you meet the research criteria.  Your participation in this research study is voluntary.",
                                   className="text-body text-justify text-left",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '16px'}),
                            html.H3("WHY IS THIS STUDY BEING DONE ?", className="text-secondary text-left",
                                    style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '20px'}),
                            html.P("The primary objective of this research is to fundamentally understand how users’ trust is formed in an Artificial Intelligence (AI) based diagnosis decision support system (DSS) and how trust impacts the users’ decision-making performance based on the system.",
                                   className="text-body text-justify text-left",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '16px'}),
                            html.H3("WHAT WILL HAPPEN IF YOU TAKE PART IN THIS RESEARCH STUDY ?", className="text-secondary text-left",
                                    style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '20px'}),
                            html.P("If you volunteer to participate in this study, the researcher will ask you to do the following:",
                                   className="text-body text-justify text-left",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '16px'}),
                            html.Ul([
                                    html.Li("Complete a brief demographics survey online"),
                                    html.Li("Diagnose a series of breast tissue images with cancer if any supported by an AI"),
                                    html.Li("Rate your trust and agreement with the AI suggestions"),
                                    html.Li("Complete a post-experiment survey to rate the workload and usefulness of the AI")
                                ],className="text-body text-justify text-left",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '16px'}),
                            html.H3("ANTICIPATED LENGTH OF PARTICIPATION:", className="text-secondary text-left",
                                    style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '20px'}),
                            html.P(
                                "Participation will take a total of about 1 hour.",
                                className="text-body text-justify text-left",
                                style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '16px'}),
                            html.P("If you would like to participate in future related research, please let us know. If you would like to learn the results of the study, please contact us.",
                                className="text-body text-justify text-left", style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '16px'}),

                            html.H3("RISKS OR DISCOMFORTS:", className="text-secondary text-left",
                                    style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '20px'}),
                            html.P(
                                "There are no anticipated risks or discomfort.",
                                className="text-body text-justify text-left",
                                style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '16px'}),
                            html.H3("POTENTIAL BENEFITS:", className="text-secondary text-left",
                                    style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '20px'}),
                            html.P(
                                "You may benefit from the study in the following way(s):",
                                className="text-body text-justify text-left",
                                style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '16px'}),

                            html.Ul([
                                html.Li("You will not directly benefit from your participation in the research."),
                                html.Li(
                                    "The results of the research may help researchers learn more about parameters that impact human interaction with intelligent systems. This information will help designers to develop such systems that interact with people better."),
                            ], className="text-body text-justify text-left",
                                style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '16px'}),
                            html.H3("WHAT OTHER CHOICES DO YOU HAVE IF YOU CHOOSE NOT TO PARTICIPATE ?", className="text-secondary text-left",
                                    style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '20px'}),
                            html.P("Your participation is completely voluntary. The alternative is not to participate in the study.",
                                className="text-body text-justify text-left",style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '16px'}),

                            html.H3("SUBJECT COMPENSATION:", className="text-secondary text-left",
                                    style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '20px'}),
                            html.P("You will receive $80 compensation after you finish all the steps in this study. If you decide to opt out before completing the session, you will not receive compensation.",
                                className="text-body text-justify text-left",style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '16px'}),
                            html.H3("INFORMATION SECURITY:", className="text-secondary text-left",
                                    style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '20px'}),
                            html.P("Data collected from this study will be done so in a way to ensure your anonymity. You will be given a code name for the experiment. Data analysis and presentation/dissemination will only use your code and will not include any identifiers. We will not collect or store any information that links your identity to your code name during the study. Your email address will be used to send you the gift card and that information will not be linked to your data in any of the records we keep.",
                                className="text-body text-justify text-left",style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '16px'}),
                            html.H3("PARTICIPANT RIGHTS:",
                                    className="text-secondary text-left",
                                    style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '20px'}),
                            html.Ul([
                                html.Li("You can choose whether or not you want to be in this study, and you may withdraw your consent and discontinue participation at any time."),
                                html.Li("Whatever decision you make, there will be no penalty to you, and no loss of benefits to which you were otherwise entitled."),
                                html.Li("You may refuse to answer any questions that you do not want to answer and still remain in the study."),
                            ], className="text-body text-justify text-left",
                                style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '16px'}),
                            html.H3("WHO TO CONTACT IF YOU HAVE QUESTIONS ABOUT THIS STUDY:", className="text-secondary text-left",
                                    style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '20px'}),
                            html.Ul(html.Li(["The Research Team"]),className="text-body text-justify text-left",
                                style={'fontFamily': 'optima', 'fontWeight': 700, 'fontSize': '18px'}),
                                html.P("If you have any questions, comments, or concerns about the research, you can contact one of the researchers:",className="text-body text-justify text-left",
                                style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '16px',"margin-left": "20px"}),
                                html.Ul([
                                    html.Li([
                                        html.Strong("Dr. Alparslan Emrah Bayrak"),
                                        html.Br(),
                                        "Email: ",
                                        html.A("Emrah.Bayrak@stevens.edu", href="mailto:Emrah.Bayrak@stevens.edu")
                                    ],className="text-body text-justify text-left",
                                style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '16px', "margin-left": "20px"}),
                                    html.Li([
                                        html.Strong("Elia Rezaeian"),
                                        html.Br(),
                                        "Email: ",
                                        html.A("orezaeia@stevens.edu", href="mailto:orezaeia@stevens.edu")
                                    ],className="text-body text-justify text-left",
                                style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '16px',"margin-left": "20px"})
                                ]),
                            html.Ul(html.Li(["SIT Institutional Review Board (IRB)"]),className="text-body text-justify text-left",
                                style={'fontFamily': 'optima', 'fontWeight': 700, 'fontSize': '18px'}),
                            html.P("If you have questions about your rights as a research subject, or you have concerns or suggestions and you want to talk to someone other than the researchers, you may contact the Stevens IRB:",
                                   className="text-body text-justify text-left",style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '16px',"margin-left": "20px"}),
                                html.P([
                                    "Phone: ",
                                    html.A("201-216-3742", href="tel:+12012163742"),
                                    html.Br(),
                                    "Email: ",
                                    html.A("irb@stevens.edu", href="mailto:irb@stevens.edu")
                                ],className="text-body text-justify text-left",
                                style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '16px',"margin-left": "20px"})


                        ],
                        className="d-flex flex-column",
                    )
                ),

                        dbc.CardFooter([
                            dcc.Checklist(
                                id='my-checkbox',
                                options=['   I agree'],

                            ),
                            dbc.Row(
                                [
                                    # Empty column to push the button to the right
                                    dbc.Col(
                                        html.Div(id = 'unique-code')
                                        ,width=10),
                                    # Column for the button
                                    dbc.Col(
                                        dbc.Button("Start", href="/page_0_code", id="proceed-button", disabled=True,
                                                   className="btn btn-warning",
                                                   style={'fontFamily': 'optima', 'fontWeight': 600,
                                                          'fontSize': '20px'}),
                                        width=2 # Adjust the width as needed
                                    ),
                                ],
                                justify="end",  # Align items to the end (right)
                            )
                        ],className="text-body text-justify text-left",
                                style={'fontFamily': 'optima', 'fontWeight': 600, 'fontSize': '16px',"margin-left": "25px"})
            ],
#B0BDD6
            style={'width': '80%', 'margin': '0 auto', "background-color": "#FDFDFF"},inverse=True, outline=True, color= 'light'
        ),
        width={'size': 10},
    ),
    justify='center',
    style={'margin-top': '30px'}
)



def generate_unique_code():
    while True:
        new_code = random.randint(1000, 9999)
        if not is_code_used(new_code):
            save_code(new_code)
            return new_code

# Check if the code has already been used
def is_code_used(code):
    if not os.path.exists('generated_codes.txt'):
        return False
    with open('generated_codes.txt', 'r') as file:
        used_codes = file.read().splitlines()
    return str(code) in used_codes

# Save the new unique code to the file
def save_code(code):
    with open('generated_codes.txt', 'a') as file:
        file.write(f"{code}\n")




@callback(
    [Output('proceed-button', 'disabled'),
     Output('unique-code', 'children')],
    [Input('my-checkbox', 'value')]
)

def enable_proceed_button_and_generate_code(checked_values):
    if checked_values == ["   I agree"]:
        unique_code = generate_unique_code()
        return False, [
            "Remember your unique participant ID:  ",
            html.Span(unique_code, style={'color': 'red', 'fontWeight': 'bold'})  # Highlight the unique code
        ]
    return True, ""


# def enable_proceed_button_and_generate_code(checked_values):
#     if checked_values == ["   I agree"]:
#         unique_code = generate_unique_code()
#         return False, f"Your unique participant ID: {unique_code}"  # Return the unique code
#     return True, ""  # If not checked, don't display a code


#
# @callback(
#     Output('proceed-button', 'disabled'),
#     [Input('my-checkbox', 'value')]
# )
# def enable_proceed_button(checked_values):
#     if checked_values == ["   I agree"]:
#         return False  # Enable the button
#     return True

