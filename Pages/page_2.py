import dash
import pandas as pd
from dash import dcc, html, callback, Output, Input, State
import dash_bootstrap_components as dbc
from dash import no_update
from dash_canvas import DashCanvas
from dash_iconify import DashIconify
import csv
import datetime

df = pd.read_csv('EXP_1.csv')

image_paths1 = [
    "/assets/Main/Main_9.png",
    "/assets/Main/Main_11.png",
    "/assets/Main/Main_12.png",
    "/assets/Main/Main_13.png",
    "/assets/Main/Main_14.png",
    "/assets/Main/Main_18.png",
    "/assets/Main/Main_19.png",
    "/assets/Main/Main_21.png",
    "/assets/Main/Main_23.png",
    "/assets/Main/Main_29.png",
]

file_path1 = '1st_Condition.csv'

column_names1 = ['Agreement','modal', 'trust', 'q1','q2','q3','q4','q5','q6','q7']

required_fields1 = ['Agreement', 'trust', 'q1','q2','q3','q4','q5','q6','q7']


# dash.register_page(__name__, name='1st Condition')

icon = DashIconify(icon="system-uicons:checkbox-checked", style={"color": '#F7ce00', 'width': 50, 'height': 50})
AI_icon = DashIconify(icon="carbon:machine-learning-model", className='text-primary' ,style={ 'width': 40, 'height': 40})
Warning_icon = DashIconify(icon="fluent-emoji:warning" ,style={ 'width': 30, 'height': 30})

layout = dbc.Row(
    dbc.Col(
        dbc.Card(
            [
                dbc.CardHeader(html.H4("First Condition", className="card-title text-info",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '30px'})),
                dbc.CardBody(
                    dbc.Container(
                        [
                            dbc.Row(
                                dbc.Col(
                                    dbc.Card(
                                        [
                                            dbc.CardHeader([AI_icon,'   AI\'s Suggestion:'],className="card-title text-primary",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '20px'}),
                                            dbc.CardBody(
                                                [
                                                    # html.P('This image shows ', id='ai-statement',className='text-primary',
                                                    #        style={'font-style': 'italic', 'text-align': 'center','fontFamily': 'optima','fontWeight': 500, 'fontSize': '30px'},),
                                                    html.P('This image shows Benign Tumor!',id= 'AI-tumor-suggestion',className='text-info',
                                                           style={'font-style': 'italic', 'text-align': 'center','fontFamily': 'optima','fontWeight': 600, 'fontSize': '20px'})
                                                    ]
                                            ),
                                        ],
                                        #color="info",
                                        style={'width': '100%', 'margin': '0 auto', 'background-color':'#f8ffff'}

                                    ),
                                    style={"width": "50rem"},
                                    className="d-flex justify-content-center",

                                )
                            ),

                            html.Br(),
                            html.Label('How much do you agree with the AI suggestion?',
                                       style={'margin-top': '0px','font-style': 'italic', 'text-align': 'center','fontFamily': 'optima','fontWeight': 500, 'fontSize': '18px'},
                                       className= 'text-primary'),
                            html.Div(
                                dcc.Slider(
                                    id='agreement-slider1',
                                    min=0,
                                    max=4,
                                    step=1,
                                    value=0,
                                    marks={
                                        0: 'Totally Disagree',
                                        1: 'Disagree',
                                        2: 'Neutral',
                                        3: 'Agree',
                                        4: 'Totally Agree'
                                    }
                                ),style={'width': '60%','margin-top': '5px'}
                            ),

                            dbc.Modal(
                                        id='modal1',
                                        backdrop="static",
                                        is_open=False,
                                        centered=True,
                                        fade=True,
                                        size='md',
                                        children=[
                                            dbc.ModalHeader( dbc.ModalTitle("We'd like to hear your opinion"),close_button=True),
                                            dbc.ModalBody([
                                                html.P("What do you think about the tumor?",
                                                       className='text-primary-emphasis',
                                                       style={'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '20px','margin-top': '20px'}),
                                                dbc.RadioItems(
                                                    id='user-opinion1',
                                                    options=[
                                                        {'label': 'Healthy', 'value': 'healthy'},
                                                        {'label': 'Benign', 'value': 'benign'},
                                                        {'label': 'Malignant', 'value': 'malignant'},
                                                    ],
                                                    value=''
                                                )
                                            ]),
                                            dbc.ModalFooter(
                                                dbc.Button("Submit", id="close-modal1", className="btn btn-info",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '20px'})
                                            )
                                        ],
                                    ),

                            html.Label('How much do you trust the AI suggestion?',
                                       style={'margin-top': '20px','font-style': 'italic', 'text-align': 'center','fontFamily': 'optima','fontWeight': 500, 'fontSize': '18px'},
                                       className= 'text-primary'),
                            html.Div(
                                dcc.Slider(
                                    id='trust-slider1',
                                    min=0,
                                    max=4,
                                    step=1,
                                    value=0,
                                    marks={
                                        0: 'Not at all',
                                        1: 'Slightly',
                                        2: 'Moderately',
                                        3: 'Quite a bit',
                                        4: 'Completely'
                                    }
                                ),style={'width': '60%','margin-top': '0px'}
                            ),

                            html.Hr(style={'borderWidth': "0.01vh", "width": "100%", "borderColor": "#35397E", "borderStyle": "solid",'margin-top': '30px' }),
                            dbc.Label([icon, "  If you see cancer tissues in this image, would you please draw a boundary around the cancerous area?"],
                                      style={'margin-top': '10px','fontFamily': 'optima','fontWeight': 500, 'fontSize': '18px'},
                                      className='text-md-center text-primary me-2'),
                            DashCanvas(
                                id='canvas2',
                                tool='line',
                                lineWidth=4,
                                lineColor='red',
                                image_content=image_paths1[0],
                                width=350,
                                hide_buttons=['line', 'pan', 'rectangle', 'circle', 'polygon', 'text',
                                              'download',
                                              'polygon', 'select']
                            ),

                            dbc.Label([Warning_icon, "   Don't forget to save!"],
                                      style={'margin-top': '30px',
                                             'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '18px', 'align-items': 'baseline'},
                                      className='text-danger'),




                            html.Button("Next Image", id="next-button1", n_clicks=0,
                                        className="btn btn-outline-warning align-items-center",
                                        style={'fontFamily': 'optima', 'fontWeight': 600, 'fontSize': '16px',
                                                       'width': '11%', "marginLeft": "90%", "margin-top": "10px"}),

                            html.Button("Submit", id="submit-button2", n_clicks=0,
                                        className="btn btn-info", style={'display': 'none','fontFamily': 'optima',
                                                                         'fontWeight': 800, 'fontSize': '22px','width': '80%',
                                                                         "marginLeft": "10%", "margin-top": "10px"}),
                            html.Div(id = 'output1', className="text-danger", style={ 'fontFamily': 'optima',
                                                                         'fontWeight': 600, 'fontSize': '18px',
                                                                         'width': '80%',
                                                                         "marginLeft": "0%", "margin-top": "10px"}),

                            dbc.Modal(
                                        id='modal1_1',
                                        backdrop="static",
                                        is_open=False,
                                        centered=True,
                                        fade=True,
                                        size='lg',
                                        children=[
                                            dbc.ModalHeader( dbc.ModalTitle("Post Experiment Survey"),close_button=True),
                                            dbc.ModalBody([
                                                html.H6("1. I believe that the AI answers were accurate.",
                                                        className='text-primary-emphasis',
                                                        style={'fontFamily': 'optima', 'fontWeight': 400,
                                                               'fontSize': '20px', 'margin-top': '20px'}),
                                                dcc.RadioItems(id='q1-1', options=['Not accurate', 'Somewhat accurate',
                                                                                 'Accurate half the time',
                                                                                 'Mostly Accurate',
                                                                                 'Completely accurate'], inline=True,
                                                               labelClassName="mt-1 m-3",
                                                               style={'fontFamily': 'optima', 'fontWeight': 400,
                                                                      'fontSize': '16px'}),

                                                html.H6("2. How mentally demanding was the task?",
                                                        className='text-primary-emphasis',
                                                        style={'fontFamily': 'optima', 'fontWeight': 400,
                                                               'fontSize': '20px','margin-top': '20px'}),
                                                html.Div(
                                                    dcc.Slider(id='q1-2', min=0, max=4, step=1,
                                                               marks={
                                                                   0: 'Very Low',
                                                                   1: 'Below Average',
                                                                   2: 'Average',
                                                                   3: 'Above Average',
                                                                   4: 'Very High'
                                                               }),
                                                    style={'width': '80%', 'margin-top': '20px', 'margin': '0 auto'}
                                                ),

                                                html.H6(
                                                    "3. How insecure, discouraged, irritated, stressed, and annoyed were you?",
                                                    className='text-primary-emphasis',
                                                    style={'fontFamily': 'optima', 'fontWeight': 400,
                                                           'fontSize': '20px','margin-top': '20px'}),

                                                html.Div(
                                                    dcc.Slider(id='q1-3', min=0, max=4, step=1,
                                                               marks={
                                                                   0: 'Very Low',
                                                                   1: 'Below Average',
                                                                   2: 'Average',
                                                                   3: 'Above Average',
                                                                   4: 'Very High'
                                                               }),
                                                    style={'width': '80%', 'margin-top': '20px', 'margin': '0 auto'}
                                                ),

                                                html.H6("4. I found the AI's suggested breast cancer classification(Healthy, Benign, or Malignant) to be intuitively understandable.",
                                                        className='text-primary-emphasis',
                                                        style={'fontFamily': 'optima', 'fontWeight': 400,
                                                               'fontSize': '20px', 'margin-top': '20px'}),
                                                dcc.RadioItems(id='q1-4', options=['Strongly disagree', 'Disagree',
                                                                                 'Neither agree nor disagree', 'Agree',
                                                                                 'Strongly agree'], inline=True,
                                                               labelClassName="mt-3 m-3",
                                                               style={'fontFamily': 'optima', 'fontWeight': 400,
                                                                      'fontSize': '16px'}),

                                                html.H6(
                                                    "5.    I could access a great deal of information which explained how the AI system worked.",
                                                    className='text-primary-emphasis',
                                                    style={'fontFamily': 'optima', 'fontWeight': 400,
                                                           'fontSize': '20px', 'margin-top': '20px'}),
                                                dcc.RadioItems(id='q1-5', options=['Strongly disagree', 'Disagree',
                                                                                  'Neither agree nor disagree', 'Agree',
                                                                                  'Strongly agree'], inline=True,
                                                               labelClassName="mt-3 m-3",
                                                               style={'fontFamily': 'optima', 'fontWeight': 400,
                                                                      'fontSize': '16px'}),

                                                html.H6(
                                                    "6. The AI suggestions helped me to decide whether I can trust the generated suggestions.",
                                                    className='text-primary-emphasis',
                                                    style={'fontFamily': 'optima', 'fontWeight': 400,
                                                           'fontSize': '20px', 'margin-top': '20px'}),
                                                dcc.RadioItems(id='q1-6', options=['Strongly disagree', 'Disagree',
                                                                                 'Neither agree nor disagree', 'Agree',
                                                                                 'Strongly agree'], inline=True,
                                                               labelClassName="mt-3 m-3",
                                                               style={'fontFamily': 'optima', 'fontWeight': 400,
                                                                      'fontSize': '16px'}),

                                                html.H6(
                                                    "7.    I trusted the AI suggestions in the diagnosis of breast cancer.",
                                                    className='text-primary-emphasis',
                                                    style={'fontFamily': 'optima', 'fontWeight': 400,
                                                           'fontSize': '20px', 'margin-top': '20px'}),
                                                dcc.RadioItems(id='q1-7',
                                                               options=['Never', 'Often', 'Half of the time', 'Usually',
                                                                        'All the time'], inline=True,
                                                               labelClassName="mt-3 m-3",
                                                               style={'fontFamily': 'optima', 'fontWeight': 400,
                                                                      'fontSize': '16px'}),

                                            ]),
                                            dbc.ModalFooter(
                                                dbc.Button("Submit", id="close-modal1_1", href="/page_3",disabled= True, className="btn btn-info",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '20px'})

                                            )
                                        ],
                                    ),
                        ],
                        className="d-flex flex-column align-items-center justify-content-center",
                    )
                ),
            ],
#B0BDD6
            style={'width': '100%', 'margin': '0 auto', "background-color": "#FDFDFF"},inverse=True, outline=True, color= 'light'
        ),
        width={'size': 10},
    ),
    justify='center',
    style={'margin-top': '30px'}
)



@callback(
    Output('modal1', 'is_open'),
    [Input('agreement-slider1', 'value'), Input('close-modal1', 'n_clicks')],
    [State('modal1', 'is_open')]
)
def toggle_modal(agreement_value, close_clicks, is_open):
    ctx = dash.callback_context
    if not ctx.triggered:
        return no_update
    else:
        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if trigger_id == 'agreement-slider1' and agreement_value is not None and agreement_value < 3:
            return True
        elif trigger_id == 'close-modal1':
            return not is_open
    return False


@callback(
    Output("modal1_1", "is_open"),
    [Input("submit-button2", "n_clicks"),
     Input("close-modal1_1", "n_clicks")],
    [State("modal1_1", "is_open")],
)
def toggle_modal(n_open, n_close, is_open):
    if n_open or n_close:
        return not is_open
    return is_open

current_image_index1 = 0
data_list1 = []
survey1 = []

# Callback to update images and save data
@callback(
    Output('canvas2', 'image_content'),
    Output('agreement-slider1', 'value'),
    Output('user-opinion1', 'value'),
    Output('trust-slider1', 'value'),
    Output('next-button1', 'style'),
    Output('submit-button2', 'style'),
    Output('AI-tumor-suggestion', 'children'),
    Input('canvas2', 'json_data'),
    Input('next-button1', 'n_clicks'),
    State('agreement-slider1', 'value'),
    State('user-opinion1', 'value'),
    State('trust-slider1','value'),
    State('canvas2', 'image_content'),
    prevent_initial_call=True
)
def update_canvas_image(json_data1, next_clicks1, agreement1, opinion1,trust1, current_image1):
    global current_image_index1
    global data_list1

    # Check which button was clicked
    ctx = dash.callback_context
    triggered_component_id = ctx.triggered[0]['prop_id'].split('.')[0]
    time_current = datetime.datetime.now()
    # If "Save Data" button was clicked, save the data for the current image to the list

    data_list1.append([current_image1,time_current.strftime('%Y-%m-%d '), time_current.strftime('%I:%M:%S %p'), agreement1, opinion1,trust1, json_data1])

    # If "Next" button was clicked, calculate the index of the next image
    if triggered_component_id == 'next-button1':
        current_image_index1 = (current_image_index1 + 1) % len(image_paths1)
    # Get the content of the next image
    next_image_content1 = image_paths1[current_image_index1]

    # Reset the selected item for the next image
    agreement1 = None
    opinion1 = None
    trust1 = None
    # Show or hide buttons based on the current image index
    submit_button_style = {'display': 'none'}
    next_button_style = {'display': 'block','fontFamily': 'optima', 'fontWeight': 600, 'fontSize': '16px','width': '11%', "marginLeft": "90%", "margin-top": "10px"}
    if current_image_index1 == len(image_paths1) - 1:
        submit_button_style = {'display': 'block','fontFamily': 'optima', 'fontWeight': 600, 'fontSize': '18px','width': '80%', "marginLeft": "0%", "margin-top": "10px"}
        next_button_style = {'display': 'none'}

    label = df.loc[current_image_index1 + 10, 'label']

    if label == 0:
        x = 'This image shows Benign Tumor!'
    elif label == 1:
        x = 'This image shows Malignant Tumor!'
    else:
        x = 'This image shows Healthy Tissue!'

    return next_image_content1, agreement1, opinion1, trust1,  next_button_style, submit_button_style,x

column_names1 = ['q1-1','q1-2','q1-3','q1-4','q1-5','q1-6','q1-7']
required_fields1 = ['q1-1','q1-2','q1-3','q1-4','q1-5','q1-6','q1-7']
@callback(
    Output("close-modal1_1", "disabled"),
    [
        Input("q1-1", "value"),
        Input("q1-2", "value"),
        Input("q1-3", "value"),
        Input("q1-4", "value"),
        Input("q1-5", "value"),
        Input("q1-6", "value"),
        Input("q1-7", "value")
    ]
)

def toggle_button_state(q1,q2,q3,q4,q5,q6,q7):
    inputs = [q1,q2,q3,q4,q5,q6,q7]

    if any(input_value is None or str(input_value).strip() == '' for input_value, field in zip(inputs, column_names1) if
           field in required_fields1):
        return True  # If any required field is empty, the button will remain disabled
    else:
        return False


# Callback to save data to a CSV file when the "Submit" button is clicked
@callback(
    Output('close-modal1_1', 'n_clicks'),
    Output('output1', 'children'),
    Input('close-modal1_1', 'n_clicks'),
    Input('participant-store', 'data'),
    State('q1-1', 'value'),
    State('q1-2', 'value'),
    State('q1-3', 'value'),
    State('q1-4', 'value'),
    State('q1-5', 'value'),
    State('q1-6', 'value'),
    State('q1-7', 'value'),

    prevent_initial_call=True
)
def save_data_to_csv(submit_clicks,code,q1,q2,q3,q4,q5,q6,q7):
    if submit_clicks > 0:
        print("Data from store:", code)
        participant_code = code.get('code') if code else None
        filename = f'1st_condition_{participant_code}.csv'
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Image Path','date','time', 'agreement', 'opinion','trust', 'JSON Data'])
            writer.writerows(data_list1)


        filename1 = f'1st_survey_{participant_code}.csv'
        with open(filename1, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            survey1.append([q1,q2,q3,q4,q5,q6,q7])
            writer.writerow(['q1','q2','q3','q4','q5','q6','q7'])
            writer.writerows(survey1)

    global current_image_index
    current_image_index = 0
    # Reset the submit button click count to 0
    return 0, "* Thanks! Please go to the second condition of the experiment from the top of the page! "

