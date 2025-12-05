import os
import dash
from dash import dcc, html, dash_table, Input, Output, State
import pandas as pd

# Initial empty DataFrame
columns = ['Manufacturer', 'Library Name', 'Subfolders/Directories']
df = pd.DataFrame(columns=columns)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Sample Library Assistant'),
    html.Div([
        html.Label('Manufacturer'),
        dcc.Input(id='manufacturer', type='text'),
        html.Label('Library Name'),
        dcc.Input(id='library_name', type='text'),
        html.Label('Root Directory (optional, to scan)'),
        dcc.Input(id='root_dir', type='text'),
        html.Button('Add Entry', id='add_btn', n_clicks=0),
        html.Button('Scan Directory', id='scan_btn', n_clicks=0),
    ], style={'display': 'flex', 'gap': '10px', 'margin-bottom': '20px'}),
    dash_table.DataTable(
        id='library_table',
        columns=[{"name": i, "id": i} for i in columns],
        data=df.to_dict('records'),
        filter_action='native',
        sort_action='native',
        page_size=10
    )
])

# Store data in memory for this session
app._data = df.copy()

@app.callback(
    Output('library_table', 'data'),
    [Input('add_btn', 'n_clicks'), Input('scan_btn', 'n_clicks')],
    [State('manufacturer', 'value'), State('library_name', 'value'), State('root_dir', 'value')]
)
def update_table(add_clicks, scan_clicks, manufacturer, library_name, root_dir):
    ctx = dash.callback_context
    if not ctx.triggered:
        return app._data.to_dict('records')
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if button_id == 'add_btn' and manufacturer and library_name:
        new_row = {'Manufacturer': manufacturer, 'Library Name': library_name, 'Subfolders/Directories': ''}
        app._data = pd.concat([app._data, pd.DataFrame([new_row])], ignore_index=True)
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
    return app._data.to_dict('records')

if __name__ == '__main__':
    app.run(debug=True)
