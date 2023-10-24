import dash
from dash import html, dcc, Output, Input, State, callback
from dash import dcc, callback
from dash import html
import csv
import dash_bootstrap_components as dbc
import pandas as pd
import json


column_names = [ 'Age',
                 'Gender', 'race', 'job', 'other_job', 'experience',
                'AI-familiarity', 'AI-recommendation', 'AI-trust', 'AI-role', 'complexity', 'AI-usefulness'
                 ]

required_fields = ['Age',
                   'Gender', 'race', 'job', 'experience',
                'AI-familiarity', 'AI-recommendation', 'AI-trust', 'AI-role', 'complexity', 'AI-usefulness'
                   ]


# dash.register_page(__name__,name='Pre-Survey')

layout = dbc.Container([
    dbc.Row(

        dbc.Col([
            html.H1("Pre-experiment Survey",
                    className='text-center text-info font-weight-bold mb-2',style={'fontFamily': 'optima','fontWeight': 600, 'fontSize': '40px', 'margin-top': '20px'}),
            html.Hr(style={'borderWidth': "0.01vh", "width": "100%", "borderColor": "#35397E", "borderStyle":"solid"})

        ],width=11),

        justify= 'around'),

    dbc.Row([
        dbc.Col([

            # html.H6("Participant Code",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '20px'}),
            # dbc.Input(id="code-input", type="text", placeholder="Enter your code",required= True, autoFocus= True,style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '16px'}),
            html.H6("Age",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '20px','margin-top': '20px'}),
            dbc.Input(id="age-input", type="text", placeholder="Enter your age e.g. 29",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '16px'}),

            html.H6("Gender:",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '20px','margin-top': '20px'}),
            dcc.RadioItems(id='gender',
                          options=['Male','Female', 'Not declared/assigned sex not listed'],
                          labelClassName="mr-3",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '16px'}),

            html.H6('What is your race/ethnicity? ',style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '20px','margin-top': '20px'}),
            dcc.Dropdown(id="Race-dropdown",
                         options=[
                             {"label": "Not Selected", "value": "Not Selected"},
                             {"label": "American Indian or Alaska Native","value" :"American Indian or Alaska Native"},
                             {"label": "Asian", "value": "Asian"},
                             {"label": "Black or African American", "value": "Black or African American"},
                             {"label": "Hispanic, Latino, or Spanish Origin", "value": "Hispanic, Latino, or Spanish Origin"},
                             {"label": "Middle Eastern or North African", "value": "Middle Eastern or North African"},
                             {"label": "Native Hawaiian or Other Pacific Islander", "value": "Native Hawaiian or Other Pacific Islander"},
                             {"label": "White", "value": "White"},
                             {"label": "other", "value": "other"},
                         ], value="Not Selected",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '16px'})

        ],width=3 ),





        dbc.Col([
            html.H6("1. Which one of the following job titles best describes your current position?   ", className= 'text-primary-emphasis',style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '20px','margin-top': '20px'}),
            dcc.RadioItems(id = 'job',options=['Radiologist', 'Oncologist', 'Other'], inline = True,labelClassName="mt-1 m-3" ,style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '16px'} ),
            dbc.Input(id="Job-input", type="text", placeholder="If other:", size = 'sm',style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '16px'}),

            html.H6("2. How many years of experience do you have in your current job position?", className= 'text-primary-emphasis',style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '20px','margin-top': '20px'}),
            dbc.Input(id="experience-input", type="number", placeholder="Select a year",size = 'sm',min = 0, max= 20, minLength= 1, maxLength =3, style = {'width':"20%",'fontFamily': 'optima','fontWeight': 400, 'fontSize': '16px'}),

            html.H6("3. How familiar are you with Artificial Intelligence systems?", className= 'text-primary-emphasis',style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '20px','margin-top': '20px'}),
            dcc.RadioItems(id = 'AI-familiarity',options = ['Not at all','A little bit','Somewhat', 'Familiar','Completely familiar'], inline = True,labelClassName="mt-1 m-3",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '16px'}),

            html.H6("4. Have you had any experiences where an AI system provided information or recommendations in oncology or radiology?", className= 'text-primary-emphasis',style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '20px','margin-top': '20px'}),
            dcc.RadioItems(id= 'AI-recommendation',options=['Yes','No'], inline = True,labelClassName="mt-1 m-3",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '16px'}),

            html.H6("5. To what extent do you trust AI systems to provide accurate and reliable information in oncology/radiology?", className= 'text-primary-emphasis',style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '20px','margin-top': '20px'}),
            dcc.RadioItems(id = 'AI-trust' ,options =['Not at all','A little bit','Somewhat', 'Familiar','Completely familiar'], inline = True,labelClassName="mt-1 m-3",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '16px'}),

            html.H6("6. Please indicate your level of agreement with the following statements:", className= 'text-primary-emphasis',style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '20px','margin-top': '20px'}),
            dcc.Markdown(''' * Artificial Intelligence will play an important role in the future of medicine. ''',style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '18px'}),
            html.Div(
                dcc.Slider(id='AI-role', min=0, max=4, step=1,
                           marks={
                               0: 'Totally Disagree',
                               1: 'Disagree',
                               2: 'Neutral',
                               3: 'Agree',
                               4: 'Totally Agree'
                           }), style={'width': '80%','margin-top': '50px', 'margin': '0 auto'}),

            dcc.Markdown(''' * There are too many complexities and barriers in medicine for AI to help in clinical settings. ''',style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '18px','margin-top': '20px'}),
            html.Div(
                dcc.Slider(id='complexity', min=0, max=4, step=1,
                           marks={
                               0: 'Totally Disagree',
                               1: 'Disagree',
                               2: 'Neutral',
                               3: 'Agree',
                               4: 'Totally Agree'
                           }), style={'width': '80%','margin-top': '50px', 'margin': '0 auto'}),

            dcc.Markdown(''' * AI would be useful in my job. ''',style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '18px','margin-top': '20px'}),
            html.Div(
                    dcc.Slider(id='AI-usefulness', min=0,max=4,step=1,
                       marks={
                            0: 'Totally Disagree',
                            1: 'Disagree',
                            2: 'Neutral',
                            3: 'Agree',
                            4: 'Totally Agree'
                       }),style={'width': '80%','margin-top': '50px', 'margin': '0 auto'}),

        ], width= 7)
    ], justify= 'around' ),

    dbc.Row([
            dbc.Button("Submit", id="submit-button", href = "/page_1",n_clicks=0,disabled= True, className="btn btn-info",style={'fontFamily': 'optima','fontWeight': 600, 'fontSize': '24px','margin-top': '40px'}),
            html.Div(id='output-1',style={'fontFamily': 'optima','fontWeight': 600, 'fontSize': '20px', 'margin-top': '20px'},
                     className='text-center text-danger font-weight-bold mb-2' )
    ], justify= 'around'),

])


# Callback to handle the enabling/disabling of the Submit button
@callback(
    Output("submit-button", "disabled"),
    [
        # Input("code-input", "value"),
        Input("age-input", "value"),
        Input("gender", "value"),
        Input("Race-dropdown", "value"),
        Input("job", "value"),
        Input("Job-input", "value"),
        Input("experience-input", "value"),
        Input("AI-familiarity", "value"),
        Input("AI-recommendation", "value"),
        Input("AI-trust", "value"),
        Input("AI-role", "value"),
        Input("complexity", "value"),
        Input("AI-usefulness", "value")
    ]
)
def toggle_button_state( age, gender, race, job, other_job, experience, familiarity, recom, trust, role,
                        complexity, usefulness):
    inputs = [ age, gender, race, job, other_job, experience, familiarity, recom, trust, role, complexity,
              usefulness]

    if any(input_value is None or str(input_value).strip() == '' for input_value, field in zip(inputs, column_names) if
           field in required_fields):
        return True  # If any required field is empty, the button will remain disabled
    else:
        return False


@callback(
    Output('output-1', 'children'),  # You can use a dummy div to act as the output since there's no direct UI change after saving
    Input("submit-button", "n_clicks"),
    Input('participant-store', 'data'),
    [
        # State("code-input", "value"),
        State("age-input", "value"),
        State("gender", "value"),
        State("Race-dropdown", "value"),
        State("job", "value"),
        State("Job-input", "value"),
        State("experience-input", "value"),
        State("AI-familiarity", "value"),
        State("AI-recommendation", "value"),
        State("AI-trust", "value"),
        State("AI-role", "value"),
        State("complexity", "value"),
        State("AI-usefulness", "value"),

    ]
)

def submit_email(n_clicks, code, age, gender, race, job, other_job, experience, familiarity, recom, trust, role,
                        complexity, usefulness):
    inputs = [ age, gender, race, job, other_job, experience, familiarity, recom, trust, role, complexity,
              usefulness]
    if n_clicks>0 :
        print("Data from store:", code)
        participant_code = code.get('code') if code else None
        filename = f'Demographic_{participant_code}.csv'

        # Save the email to the CSV file
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(column_names)
            writer.writerow(inputs)

