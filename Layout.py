import PySimpleGUI as sg


button_on_color = '#525252'
button_off_color = '#282828'
background_color = '#808080'
window_size_x = 850
window_size_y = 420

def get_names_data():
    global lib_name
    global tab_name
    global path
    global file_name
    global Interval_value
    f = open("Additional_files/Parametry_pliku_i_bazy.txt")
    lines = f.readlines()
    data = [i.split('--')[1][:-1] for i in lines]
    f.close()
    print(data)
    return data


load_last_names = get_names_data()


layout_location = [
    [sg.Text('Lokalizacja pliku:', justification='right', font=('', 15), pad=(20, 23), background_color=background_color,
             text_color='black')],
    [sg.Text('Ścieżka:', justification='right', font=10, background_color=background_color,
             text_color='black', pad=(20, 0))],
    [sg.Input(justification='left', size=(22, 2), font=('', 15), pad=(20, 2), background_color=background_color,
              text_color='black', key='Path',default_text=load_last_names[0])],
    [sg.Text('Nazwa:', justification='right', font=10, background_color=background_color,
             text_color='black', pad=(20, 0))],
    [sg.Input(justification='left', size=(22, 2), font=('', 15), pad=(20, 2), background_color=background_color,
              text_color='black', key='File_name',default_text=load_last_names[1])],
    [sg.Text('Interwał pobierania:', justification='left', pad=(20, 0),font=10,
                 background_color=background_color, text_color='black')],
    [sg.Input(justification='left', size=(22, 2), font=('', 15), pad=(20, 2), background_color=background_color,
              text_color='black', key='Interval',default_text=load_last_names[2])],
    [sg.Text('',key='Error_interval', justification='left', pad=(20, 0), font=10,
             background_color=background_color, text_color='#b31028')],

]


layout_directory = [
    [sg.Text('Ustawienia bazy:', justification='right', font=('', 15), pad=(20, 23), background_color=background_color,
             text_color='black')],
    [sg.Text('Nazwa biblioteki:', justification='right', font=10, background_color=background_color,
             text_color='black', pad=(20, 0))],
    [sg.Input(justification='left', size=(22, 2), font=('', 15), pad=(20, 2), background_color=background_color,
              text_color='black', key='Library',default_text=load_last_names[3])],
    [sg.Text('Nazwa tabeli:', justification='right', font=10, background_color=background_color,
             text_color='black', pad=(20, 0))],
    [sg.Input(justification='left', size=(22, 2), font=('', 15), pad=(20, 2), background_color=background_color,
              text_color='black', key='Table',default_text=load_last_names[4])],

]

layout_errors = [
    [sg.Text('Błędy i pobieranie danych:', justification='right', font=('', 15), pad=(10, 20),
             background_color=background_color,
             text_color='black')],
    [sg.Listbox(
        values=['' for i in range(12)],
                size=(30, 13), pad=(5, 0), key='Text_Listbox', highlight_background_color=background_color,
                highlight_text_color='black',
                background_color=background_color,
                no_scrollbar= True
        )]
]

layout = [[sg.HSep()],

          [[sg.Column(
              [[
                  sg.Col(layout_location, pad=(0, 0), key='COL1', size=(278, 300), background_color=background_color),
                  sg.VerticalSeparator(key='Vertical_1', pad=(0, 0)),
                  sg.Col(layout_directory, pad=(0, 0), key='COL1', size=(290, 300), background_color=background_color),
                  sg.VerticalSeparator(key='Vertical_1', pad=(0, 0)),
                  sg.Col(layout_errors, pad=(0, 0), key='COL3', size=(250, 300), background_color=background_color),
              ]],
              key='Watch_panel', visible=True)]],

          [sg.HSep()],

          [sg.Button('Stop', key='Start_stop_button', button_color=button_on_color, size=(30, 2), pad=(30, 0),
                     font=('', 15), visible=True),
           sg.Button('Zatwierdź dane', key='Apply_all', button_color=button_on_color, size=(30, 2), pad=(20, 0),
                     font=('', 15), visible=True)],
          [sg.HSep()],
          ]


def make_window(theme=None):
    sg.theme('DarkGrey4')
    window = sg.Window('Aktualizacja Baz Orlen - RW Electra', layout, finalize=True,
                       keep_on_top=False, size=(window_size_x, window_size_y), icon='Additional_files/logo.ico',
                       background_color=background_color)

    return window
