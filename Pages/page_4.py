import dash
from dash import dcc, html, callback, Output, Input, State
import dash_bootstrap_components as dbc
from dash import no_update
from dash_canvas import DashCanvas
from dash_iconify import DashIconify
import pandas as pd
import plotly.express as px
import csv
import datetime

df2 = pd.read_csv('EXP_1.csv')

image_paths3 = [
    "/assets/Main/Main_20.png",
    "/assets/Main/Main_79.png",
    "/assets/Main/Main_24.png",
    "/assets/Main/Main_44.png",
    "/assets/Main/Main_54.png",
    "/assets/Main/Main_82.png",
    "/assets/Main/Main_22.png",
    "/assets/Main/Main_69.png",
    "/assets/Main/Main_18.png",
    "/assets/Main/Main_74.png",
]

result_paths3 = [
    "/assets/Result/result_20.png",
    "/assets/Result/result_79.png",
    "/assets/Result/result_24.png",
    "/assets/Result/result_44.png",
    "/assets/Result/result_54.png",
    "/assets/Result/result_82.png",
    "/assets/Result/result_22.png",
    "/assets/Result/result_69.png",
    "/assets/Result/result_18.png",
    "/assets/Result/result_74.png",
]

# dash.register_page(__name__, name='3rd Condition')

#
icon = DashIconify(icon="system-uicons:checkbox-checked", style={"color": '#F7ce00', 'width': 50, 'height': 50})
AI_icon = DashIconify(icon="carbon:machine-learning-model", className='text-primary',style={"color": '#9511af', 'width': 40, 'height': 40})
Warning_icon = DashIconify(icon="fluent-emoji:warning" ,style={ 'width': 30, 'height': 30})

layout = dbc.Row(
    dbc.Col(

        dbc.Card(
            [
                dbc.CardHeader(html.H4("Third Condition", className="card-title text-info",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '30px'})),
                dbc.CardBody(
                    dbc.Container(
                        [
                            dbc.Row(
                                dbc.Col(
                                    dbc.Card(
                                        [
                                            dbc.CardHeader([AI_icon,'   AI\'s Suggestion:'],className="card-title text-primary",style={'fontFamily': 'optima','fontWeight': '400', 'fontSize': '20px','color': '#9511af'}),
                                            dbc.CardBody(
                                                    dbc.Row([
                                                        dbc.Col([
                                                            html.P(id='AI-tumor-suggestion3', className='text-info',
                                                                   style={'font-style': 'italic',
                                                                          'text-align': 'center',
                                                                          'fontFamily': 'optima', 'fontWeight': 600,
                                                                          'fontSize': '20px', 'padding': '0','margin-top': '15px'}),

                                                            html.Div(
                                                                dcc.Graph(id="graph2"),
                                                                style={'display': 'flex', 'justify-content': 'center',
                                                                       'align-items': 'center','padding': '0','margin': '0'})


                                                        ]
                                                        ,width= 6
                                                        ),

                                                        dbc.Col([
                                                            html.P('The image shows the potential cancerous area.', id='ai-image_explanation', className= 'text-primary',
                                                           style={'font-style': 'italic', 'text-align': 'center','fontFamily': 'optima','fontWeight': 500, 'fontSize': '16px','margin-top': '10px'}),

                                                            html.Div(
                                                                [
                                                                    html.Img(src=result_paths3[0],
                                                                             id='image-container3',style={'width': 300, 'height': 300,})
                                                                ],
                                                                style={'margin-bottom': '20px','margin': '0 auto', },
                                                                className="d-flex justify-content-center"
                                                            )

                                                            ]
                                                        ,width= 6)
                                                    ]),

                                            ),
                                        ],
                                        #color="primary",
                                        style={'width': '100%', 'margin': '0 auto', 'background-color':'#f8ffff'},
                                    ),
                                    width={'size': 12},
                                    className="d-flex justify-content-center",

                                )
                            ),

                            html.Br(),
                            html.Label('How much do you agree with the AI suggestion?',
                                       style={'margin-top': '10px','font-style': 'italic', 'text-align': 'center','fontFamily': 'optima','fontWeight': 500, 'fontSize': '18px'},
                                       className= 'text-primary'),
                            html.Div(
                                dcc.Slider(
                                    id='agreement-slider3',
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
                                ),style={'width': '60%','margin-top': '0px'}
                            ),

                            dbc.Modal(
                                        id='modal3',
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
                                                    id='user-opinion3',
                                                    options=[
                                                        {'label': 'Healthy', 'value': 'healthy'},
                                                        {'label': 'Benign', 'value': 'benign'},
                                                        {'label': 'Malignant', 'value': 'malignant'},
                                                    ],
                                                    value=''
                                                )
                                            ]),
                                            dbc.ModalFooter(
                                                dbc.Button("Submit", id="close-modal3", className="ml-auto btn-outline-info",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '20px'})
                                            )
                                        ],
                            ),

                            html.Label('How much do you trust the AI suggestion?',
                                       style={'margin-top': '20px','font-style': 'italic', 'text-align': 'center','fontFamily': 'optima','fontWeight': 500, 'fontSize': '18px'},
                                       className= 'text-primary'),
                            html.Div(
                                dcc.Slider(
                                    id='trust-slider3',
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
                                id='canvas4',
                                tool='line',
                                lineWidth=4,
                                lineColor='red',
                                image_content=image_paths3[0],
                                width=350,
                                hide_buttons=['line', 'pan', 'rectangle', 'circle', 'polygon', 'text',
                                              'download',
                                              'polygon', 'select']
                            ),
                            dbc.Label([Warning_icon, "   Don't forget to save!"],
                                      style={'margin-top': '30px',
                                             'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '18px',
                                             'align-items': 'baseline'},
                                      className='text-danger'),
                            #
                            # html.Button('Save Data', id='save-button3', n_clicks=0,
                            #             className="btn btn-outline-danger d-flex flex-column align-items-center",
                            #             style={'fontFamily': 'optima', 'fontWeight': 600, 'fontSize': '16px',
                            #                    'width': '11%', "marginLeft": "90%", "margin-top": "10px"}),
                            html.Button("Next Image", id="next-button3", n_clicks=0,
                                        className="btn btn-outline-warning align-items-center",
                                        style={'fontFamily': 'optima', 'fontWeight': 600, 'fontSize': '16px',
                                               'width': '11%', "marginLeft": "90%", "margin-top": "10px"}),

                            html.Button("Submit", id="submit-button4", n_clicks=0,
                                        className="btn btn-info", style={'display': 'none', 'fontFamily': 'optima',
                                                                         'fontWeight': 800, 'fontSize': '22px',
                                                                         'width': '80%',
                                                                         "marginLeft": "0%", "margin-top": "10px"}),

                            html.Div(id='output3', className="text-danger", style={'fontFamily': 'optima',
                                                                                   'fontWeight': 600,
                                                                                   'fontSize': '18px',
                                                                                   'width': '80%',
                                                                                   "marginLeft": "0%",
                                                                                   "margin-top": "10px"}),



                            dbc.Modal(
                                        id='modal3_1',
                                        backdrop="static",
                                        is_open=False,
                                        centered=True,
                                        fade=True,
                                        size='lg',
                                        children=[
                                            dbc.ModalHeader( dbc.ModalTitle("Post Experiment"),close_button=True),
                                            dbc.ModalBody([
                                                html.H6("1. I believe that the AI answers were accurate.",
                                                        className='text-primary-emphasis',
                                                        style={'fontFamily': 'optima', 'fontWeight': 400,
                                                               'fontSize': '20px', 'margin-top': '20px'}),
                                                dcc.RadioItems(id='q3-1', options=['Not accurate', 'Somewhat accurate',
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
                                                    dcc.Slider(id='q3-2', min=0, max=4, step=1,
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
                                                    "3. How stressed, and annoyed were you?",
                                                    className='text-primary-emphasis',
                                                    style={'fontFamily': 'optima', 'fontWeight': 400,
                                                           'fontSize': '20px','margin-top': '20px'}),

                                                html.Div(
                                                    dcc.Slider(id='q3-3', min=0, max=4, step=1,
                                                               marks={
                                                                   0: 'Very Low',
                                                                   1: 'Below Average',
                                                                   2: 'Average',
                                                                   3: 'Above Average',
                                                                   4: 'Very High'
                                                               }),
                                                    style={'width': '80%', 'margin-top': '20px', 'margin': '0 auto'}
                                                ),

                                                html.H6("4. I found the AI's suggested breast cancer classification, along with the associated probabilities for each class, and the area of cancerous tissue, to be intuitively understandable.",
                                                        className='text-primary-emphasis',
                                                        style={'fontFamily': 'optima', 'fontWeight': 400,
                                                               'fontSize': '20px', 'margin-top': '20px'}),
                                                dcc.RadioItems(id='q3-4', options=['Strongly disagree', 'Disagree',
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
                                                dcc.RadioItems(id='q3-5', options=['Strongly disagree', 'Disagree',
                                                                                  'Neither agree nor disagree', 'Agree',
                                                                                  'Strongly agree'], inline=True,
                                                               labelClassName="mt-3 m-3",
                                                               style={'fontFamily': 'optima', 'fontWeight': 400,
                                                                      'fontSize': '16px'}),

                                                html.H6(
                                                    "6. The explanations helped me to decide whether I can trust the generated sugesstions.",
                                                    className='text-primary-emphasis',
                                                    style={'fontFamily': 'optima', 'fontWeight': 400,
                                                           'fontSize': '20px', 'margin-top': '20px'}),
                                                dcc.RadioItems(id='q3-6', options=['Strongly disagree', 'Disagree',
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
                                                dcc.RadioItems(id='q3-7',
                                                               options=['Never', 'Often', 'Half of the time', 'Usually',
                                                                        'All the time'], inline=True,
                                                               labelClassName="mt-3 m-3",
                                                               style={'fontFamily': 'optima', 'fontWeight': 400,
                                                                      'fontSize': '16px'}),

                                            ]),
                                            dbc.ModalFooter(
                                                dbc.Button("Submit", id="close-modal3_1", href="/page_5",disabled= True,className="ml-auto btn-info",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '20px'})
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
    Output('modal3', 'is_open'),
    [Input('agreement-slider3', 'value'), Input('close-modal3', 'n_clicks')],
    [State('modal3', 'is_open')]
)
def toggle_modal(agreement_value, close_clicks, is_open):
    ctx = dash.callback_context
    if not ctx.triggered:
        return no_update
    else:
        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if trigger_id == 'agreement-slider3' and agreement_value is not None and agreement_value < 3:
            return True
        elif trigger_id == 'close-modal3':
            return not is_open
    return False

@callback(
    Output("modal3_1", "is_open"),
    [Input("submit-button4", "n_clicks"), Input("close-modal3_1", "n_clicks")],
    [State("modal3_1", "is_open")],
)
def toggle_modal1(n_open, n_close, is_open):
    if n_open or n_close:
        return not is_open
    return is_open


current_image_index3 = 0
data_list3 = []
survey3 = []

@callback(
    Output('canvas4', 'image_content'),
    Output('agreement-slider3', 'value'),
    Output('user-opinion3', 'value'),
    Output('trust-slider3', 'value'),
    # Output('save-button3', 'style'),
    Output('next-button3', 'style'),
    Output('submit-button4', 'style'),
    Output('AI-tumor-suggestion3', 'children'),
    Output('image-container3','src'),
    Input('canvas4', 'json_data'),
    # Input('save-button3', 'n_clicks'),
    Input('next-button3', 'n_clicks'),
    State('agreement-slider3', 'value'),
    State('user-opinion3', 'value'),
    State('trust-slider3','value'),
    State('canvas4', 'image_content'),
    prevent_initial_call=False  # Allow the callback to run on initial loading
)
def update_canvas_image(json_data, next_clicks, agreement, opinion, trust, current_image):
    global current_image_index3
    global data_list3

    # Check which button was clicked
    ctx = dash.callback_context
    triggered_component_id = ctx.triggered[0]['prop_id'].split('.')[0]
    time_current = datetime.datetime.now()

    # If "Save Data" button was clicked, save the data for the current image to the list

    data_list3.append([current_image, time_current.strftime('%Y-%m-%d'), time_current.strftime('%I:%M:%S %p'), agreement, opinion, trust, json_data])

    # If "Next" button was clicked, calculate the index of the next image
    if triggered_component_id == 'next-button3':
        current_image_index3 = (current_image_index3 + 1) % len(image_paths3)
        # Reset the selected item for the next image


    # Get the content of the next image
    next_image_content3 = image_paths3[current_image_index3]
    next_result_content3 = result_paths3[current_image_index3]
    opinion = None
    agreement = None
    trust = None

    # Show or hide buttons based on the current image index
    submit_button_style = {'display': 'none'}
    # save_button_style = {'display': 'block', 'fontFamily': 'optima', 'fontWeight': 600, 'fontSize': '16px', 'width': '11%', "marginLeft": "90%", "margin-top": "10px"}
    next_button_style = {'display': 'block', 'fontFamily': 'optima', 'fontWeight': 600, 'fontSize': '16px', 'width': '11%', "marginLeft": "90%", "margin-top": "10px"}

    if current_image_index3 == len(image_paths3) - 1:
        submit_button_style = {'display': 'block', 'fontFamily': 'optima', 'fontWeight': 600, 'fontSize': '18px', 'width': '80%', "marginLeft": "10%", "margin-top": "10px"}
        # save_button_style = {'display': 'block', 'fontFamily': 'optima', 'fontWeight': 600, 'fontSize': '16px', 'width': '11%', "marginLeft": "90%", "margin-top": "10px"}
        next_button_style = {'display': 'none'}

    label = df2.loc[current_image_index3 + 30, 'label']

    if label == 0:
        x = 'This image shows Benign Tumor!'
    elif label == 2:
        x = 'This image shows Malignant Tumor!'
    else:
        x = 'This image shows Healthy Tissue!'

    return next_image_content3, agreement, opinion, trust, next_button_style, submit_button_style, x, next_result_content3

column_names3 = ['q3-1','q3-2','q3-3','q3-4','q3-5','q3-6','q3-7']
required_fields3 = ['q3-1','q3-2','q3-3','q3-4','q3-5','q3-6','q3-7']
@callback(
    Output("close-modal3_1", "disabled"),
    [
        Input("q3-1", "value"),
        Input("q3-2", "value"),
        Input("q3-3", "value"),
        Input("q3-4", "value"),
        Input("q3-5", "value"),
        Input("q3-6", "value"),
        Input("q3-7", "value")
    ]
)

def toggle_button_state(q1,q2,q3,q4,q5,q6,q7):
    inputs = [q1,q2,q3,q4,q5,q6,q7]

    if any(input_value is None or str(input_value).strip() == '' for input_value, field in zip(inputs, column_names3) if
           field in required_fields3):
        return True  # If any required field is empty, the button will remain disabled
    else:
        return False


@callback(
    Output('close-modal3_1', 'n_clicks'),
    Output('output3', 'children'),
    Input('close-modal3_1', 'n_clicks'),
    Input('participant-store', 'data'),
    State('q3-1', 'value'),
    State('q3-2', 'value'),
    State('q3-3', 'value'),
    State('q3-4', 'value'),
    State('q3-5', 'value'),
    State('q3-6', 'value'),
    State('q3-7', 'value'),

    prevent_initial_call=True
)
def save_data_to_csv(submit_clicks,code,q1,q2,q3,q4,q5,q6,q7):
    if submit_clicks > 0:
        print("Data from store:", code)
        participant_code = code.get('code') if code else None
        filename = f'3rd_condition_{participant_code}.csv'
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Image Path','date','time', 'agreement', 'opinion','trust', 'JSON Data'])
            writer.writerows(data_list3)

        filename1 = f'3rd_survey_{participant_code}.csv'
        with open(filename1, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            survey3.append([q1,q2,q3,q4,q5,q6,q7])
            writer.writerow(['q1','q2','q3','q4','q5','q6','q7'])
            writer.writerows(survey3)

    global current_image_index3
    current_image_index3 = 0
    # Reset the submit button click count to 0
    return 0, "* Thanks! Please go to the fourth condition of the experiment from the top of the page! "




df2 = df2.iloc[30:40,:]
@callback(
    Output('graph2', 'figure'),
    Input('next-button3', 'n_clicks')
)
def update_pie_chart(n_clicks):
    row_index = n_clicks % len(df2)  # Calculate row index based on the number of clicks
    row_data = df2.iloc[row_index]

    # Prepare data for pie chart
    labels = ['Benign', 'Malignant', 'Healthy']
    values = [row_data['Benign'], row_data['Malignant'], row_data['Healthy']]
    colors = {'Benign': '#FDF264', 'Malignant': '#F24B62', 'Healthy': '#67daa0'}

    # Create pie chart using Plotly Express
    fig = px.pie(
        values=values,
        names=labels,
        color=labels,
        color_discrete_map=colors,
        title="Likelihood",
        template='xgridoff',
        width=300,
        height=300,
        hole=0.5
    )

    # Update layout
    fig.update_layout(
        margin=dict(l=0, r=0, t=80, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family="optima",
            size=12,
            color="#3B71CA"
        )
    )

    return fig








