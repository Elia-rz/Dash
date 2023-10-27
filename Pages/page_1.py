import dash
from dash import dcc, html, callback, Output, Input, State, MATCH
import dash_bootstrap_components as dbc
from dash_canvas import DashCanvas
from dash_iconify import DashIconify
import datetime
import json
import pandas as pd
import csv
from dash.exceptions import PreventUpdate



# dash.register_page(__name__, name='Baseline')

icon = DashIconify(icon="system-uicons:checkbox-checked", style={"color": '#F7ce00', 'width': 50, 'height': 50})
Warning_icon = DashIconify(icon="fluent-emoji:warning" ,style={ 'width': 30, 'height': 30})

# Define the image paths
image_paths= [
    "/assets/Main/Main_0.png",
    "/assets/Main/Main_1.png",
    "/assets/Main/Main_2.png",
    "/assets/Main/Main_3.png",
    "/assets/Main/Main_4.png",
    "/assets/Main/Main_5.png",
    "/assets/Main/Main_6.png",
    "/assets/Main/Main_7.png",
    "/assets/Main/Main_8.png",
    "/assets/Main/Main_10.png"
]

# Define the layout
layout = dbc.Row(
    dbc.Col(
        dbc.Card(
            [
                dbc.CardHeader(html.H4("Baseline", className="card-title text-info",style={'fontFamily': 'optima','fontWeight': 400, 'fontSize': '30px'})),
                dbc.CardBody(
                    dbc.Container(
                        [
                            dbc.Row(
                                dbc.Col(
                                    dbc.Card(
                                        [

                                            dbc.CardBody(
                                                [
                                                    html.P("What is your diagnosis about the below breast image?", style={'fontFamily': 'optima','fontWeight': 600, 'fontSize': '18px'}, className='text-md-center text-primary'),
                                                    dcc.RadioItems(id='radio-item',
                                                                   options=[' Healthy', ' Benign', ' Malignant'],
                                                                   inline=True, labelClassName="mt-2 m-3",className='text-info  px-sm-5',
                                                                   style={'fontFamily': 'optima', 'fontWeight': 500,
                                                                          'fontSize': '18px','margin-left': '15px'}),

                                                    ]
                                            ),
                                        ],
                                        style={'width': '100%', 'margin': '0 auto', 'background-color':'#f8ffff'}
                                    ),
                                    width={'size': 12},
                                    className="d-flex justify-content-center",
                                )
                            ),

                            dbc.Label([icon, "  If you see cancer tissues in this image, would you please draw a boundary around the cancerous area?"],
                                      style={'margin-top': '15px','fontFamily': 'optima','fontWeight': 500, 'fontSize': '18px'},
                                      className='text-md-center text-primary me-2'),

                            DashCanvas(
                                                    id='canvas',
                                                    tool='line',
                                                    lineWidth=4,
                                                    lineColor='red',
                                                    image_content=image_paths[0],
                                                    width=350,
                                                    hide_buttons=['line', 'pan', 'rectangle', 'circle', 'polygon', 'text', 'download',
                                                                  'polygon', 'select']
                                                ),
                            dbc.Label([Warning_icon, "   Don't forget to save!"],
                                      style={'margin-top': '30px',
                                             'fontFamily': 'optima', 'fontWeight': 400, 'fontSize': '18px', 'align-items': 'baseline'},
                                      className='text-danger'),
                            #
                            # html.Button('Save Data', id='save-button', n_clicks=0,className="btn btn-outline-danger d-flex flex-column align-items-center",
                            #             style={'fontFamily': 'optima', 'fontWeight': 600, 'fontSize': '16px',
                            #                    'width': '11%', "marginLeft": "90%", "margin-top": "10px"}),
                            html.Button( "Next Image", id="next-button", n_clicks=0,
                                        className="btn btn-outline-warning",
                                        style={'fontFamily': 'optima', 'fontWeight': 600, 'fontSize': '16px',
                                               'width': '11%', "marginLeft": "90%", "margin-top": "10px"}),

                            # html.Button("Submit", id="submit-button1", n_clicks=0,
                            #             className="btn btn-info", style={'display': 'none', 'fontFamily': 'optima',
                            #                                              'fontWeight': 600, 'fontSize': '18px',
                            #                                              'width': '80%',
                            #                                              "marginLeft": "0%", "margin-top": "10px"}),
                            dbc.Button("Submit", id="submit-button1", href="/page_2", n_clicks=0,
                                       className="btn btn-info",
                                       style={'display': 'none', 'fontFamily': 'optima',
                                                                         'fontWeight': 600, 'fontSize': '18px',
                                                                         'width': '80%',
                                                                         "marginLeft": "0%", "margin-top": "10px"}),

                            html.Div(id = 'output', className="text-danger", style={ 'fontFamily': 'optima',
                                                                         'fontWeight': 600, 'fontSize': '18px',
                                                                         'width': '80%',
                                                                         "marginLeft": "0%", "margin-top": "10px"}),
                            html.Div(id='current-image-index', style={'display': 'none'}, children='0'),


                        ],
                        className="d-flex flex-column align-items-center justify-content-center",
                    )
                ),
            ],
            style={'width': '100%', 'margin': '0 auto', "background-color": "#FDFDFF"},inverse=True, outline=True, color= 'light'
        ),
        width={'size': 10},
    ),
    justify='center',
    style={'margin-top': '30px'}
)


current_image_index = 0
data_list = []

# Callback to update images and save data
@callback(
    Output('canvas', 'image_content'),
    Output('radio-item', 'value'),
    # Output('save-button', 'style'),
    Output('next-button', 'style'),
    Output('submit-button1', 'style'),
    Input('canvas', 'json_data'),
    # Input('save-button', 'n_clicks'),
    Input('next-button', 'n_clicks'),
    State('radio-item', 'value'),
    State('canvas', 'image_content'),
    prevent_initial_call=True
)
def update_canvas_image(json_data, next_clicks,selected_item, current_image):
    global current_image_index
    global data_list

    # Check which button was clicked
    ctx = dash.callback_context
    triggered_component_id = ctx.triggered[0]['prop_id'].split('.')[0]
    time_current = datetime.datetime.now()
    # If "Save Data" button was clicked, save the data for the current image to the list

    data_list.append([current_image, time_current.strftime('%Y-%m-%d '), time_current.strftime('%I:%M:%S %p'), selected_item, json_data])

    # If "Next" button was clicked, calculate the index of the next image
    if triggered_component_id == 'next-button':
        current_image_index = (current_image_index + 1) % len(image_paths)
        selected_item = None
    # Get the content of the next image
    next_image_content = image_paths[current_image_index]

    # Show or hide buttons based on the current image index
    submit_button_style = {'display': 'none'}
    # save_button_style = {'display': 'block','fontFamily': 'optima', 'fontWeight': 600, 'fontSize': '16px',
    #                                            'width': '11%', "marginLeft": "90%", "margin-top": "10px"}
    next_button_style = {'display': 'block','fontFamily': 'optima', 'fontWeight': 600, 'fontSize': '16px',
                                               'width': '11%', "marginLeft": "90%", "margin-top": "10px"}
    if current_image_index == len(image_paths) - 1:
        submit_button_style = {'display': 'block','fontFamily': 'optima', 'fontWeight': 600, 'fontSize': '18px','width': '80%', "marginLeft": "0%", "margin-top": "10px"}
        # save_button_style = {'display': 'block','fontFamily': 'optima', 'fontWeight': 600, 'fontSize': '16px',
        #                                        'width': '11%', "marginLeft": "90%", "margin-top": "10px"}
        next_button_style = {'display': 'none'}


    return next_image_content, selected_item, next_button_style, submit_button_style



# Callback to save data to a CSV file when the "Submit" button is clicked
@callback(
    Output('submit-button1', 'n_clicks'),
    Input('submit-button1', 'n_clicks'),
    Input('participant-store', 'data'),

    prevent_initial_call=True
)
def save_data_to_csv(submit_clicks, code):

    if submit_clicks > 0:
        print("Data from store:", code)
        participant_code = code.get('code') if code else None
        filename = f'baseline_{participant_code}.csv'
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Image Path', 'Selected Item', 'JSON Data'])
            writer.writerows(data_list)

        global current_image_index
        current_image_index = 0
        data_list.clear()

    # Reset the submit button click count to 0
    return 0



