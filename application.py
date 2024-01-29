from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from Pages import page_0_bconsent, page_2, page_5, page_0_Survey, page_3, page_4, page_1, page_6, page_0_code

app = Dash(__name__, suppress_callback_exceptions=True,external_stylesheets=[dbc.themes.LITERA, dbc.icons.FONT_AWESOME] )
application = app.server



app.layout = html.Div([
    dcc.Store(id='participant-store', storage_type= 'session'),
    html.Div([
        html.Img(src="/assets/logo.png", height='100px')  # Adjust the size as required
    ], style={'position': 'absolute', 'top': '20px', 'right': '30px'}),

    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')

])


@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/page_0_bconsent':
        return page_0_bconsent.layout
    elif pathname == '/page_0_code':
        return page_0_code.layout
    elif pathname == '/page_0_Survey':
        return page_0_Survey.layout
    elif pathname == '/page_1':
        return page_1.layout
    elif pathname == '/page_2':
        return page_2.layout
    elif pathname == '/page_3':
        return page_3.layout
    elif pathname == '/page_4':
        return page_4.layout
    elif pathname == '/page_5':
        return page_5.layout
    elif pathname == '/page_6':
        return page_6.layout
    else:
        return page_0_bconsent.layout

def get_participant_code(data):
    if data and 'code' in data:
        return data['code']
    else:
        return None

if __name__ == '__main__':
    application.run(debug=True, port= 5080)