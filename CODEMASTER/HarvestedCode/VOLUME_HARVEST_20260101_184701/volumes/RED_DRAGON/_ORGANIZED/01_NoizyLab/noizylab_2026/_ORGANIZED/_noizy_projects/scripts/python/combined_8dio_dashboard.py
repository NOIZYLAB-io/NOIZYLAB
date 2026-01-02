import os
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table, Input, Output, State
import pandas as pd
import webbrowser
import threading


# File to autosave/keep data
SAVE_PATH = os.path.expanduser('~/Desktop/perfectionist_libraries.csv')
columns = ['Manufacturer', 'Library Name', 'Subfolders/Directories']
if os.path.exists(SAVE_PATH):
    df = pd.read_csv(SAVE_PATH)
else:
    df = pd.DataFrame(columns=columns)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

app.layout = dbc.Container([
    html.H1('Perfectionist Library Assistant', className='text-center my-4', style={'fontWeight': 'bold', 'color': '#00ffe7'}),
    dbc.Row([
        dbc.Col([
            dbc.Label('Manufacturer'),
            dbc.Input(id='manufacturer', type='text', placeholder='e.g. 8Dio', className='mb-2'),
        ], width=3),
        dbc.Col([
            dbc.Label('Library Name'),
            dbc.Input(id='library_name', type='text', placeholder='e.g. Majestica', className='mb-2'),
        ], width=3),
        dbc.Col([
            dbc.Label('Root Directory (optional, to scan)'),
            dbc.Input(id='root_dir', type='text', placeholder='/Volumes/6TB/_8Dio_2026/', className='mb-2'),
        ], width=4),
        dbc.Col([
            dbc.Button('Add Entry', id='add_btn', color='success', className='me-2 mt-4'),
            dbc.Button('Scan Directory', id='scan_btn', color='info', className='mt-4'),
        ], width=2),
    ], className='mb-4'),
    dash_table.DataTable(
        id='library_table',
        columns=[{"name": i, "id": i} for i in columns],
        data=df.to_dict('records'),
        filter_action='native',
        sort_action='native',
        page_size=12,
        style_header={'backgroundColor': '#222', 'color': '#00ffe7', 'fontWeight': 'bold'},
        style_cell={'backgroundColor': '#111', 'color': '#fff', 'fontSize': 16},
        style_table={'overflowX': 'auto'},
    ),
    html.Div('Made with ❤️ for Perfectionists', className='text-center mt-4', style={'color': '#00ffe7', 'fontSize': 18})
], fluid=True)

# Store data in memory for this session
app._data = df.copy()

@app.callback(
    Output('library_table', 'data'),
    [Input('add_btn', 'n_clicks'), Input('scan_btn', 'n_clicks')],
    [State('manufacturer', 'value'), State('library_name', 'value'), State('root_dir', 'value')]
)
def update_table(add_clicks, scan_clicks, manufacturer, library_name, root_dir):
    ctx = dash.callback_context
    changed = False
    if not ctx.triggered:
        return app._data.to_dict('records')
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if button_id == 'add_btn' and manufacturer and library_name:
        new_row = {'Manufacturer': manufacturer, 'Library Name': library_name, 'Subfolders/Directories': ''}
        app._data = pd.concat([app._data, pd.DataFrame([new_row])], ignore_index=True)
        changed = True
    elif button_id == 'scan_btn' and root_dir and os.path.isdir(root_dir):
        for dirpath, dirnames, _ in os.walk(root_dir):
            rel_path = os.path.relpath(dirpath, root_dir)
            if rel_path == '.':
                continue
            manufacturer_name = os.path.basename(os.path.dirname(dirpath))
            library = os.path.basename(root_dir)
            new_row = {
                'Manufacturer': manufacturer_name,
                'Library Name': library,
                'Subfolders/Directories': rel_path
            }
            app._data = pd.concat([app._data, pd.DataFrame([new_row])], ignore_index=True)
        changed = True
    # AutoSave
    if changed:
        app._data.to_csv(SAVE_PATH, index=False)
    return app._data.to_dict('records')

if __name__ == '__main__':
    # AutoRun: open browser automatically
    def open_browser():
        webbrowser.open_new('http://127.0.0.1:8050/')
    threading.Timer(1, open_browser).start()
    app.run(debug=True)
