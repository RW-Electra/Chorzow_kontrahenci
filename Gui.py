import PySimpleGUI as sg
import Layout
# import time
import datetime
import Control_saving_txt as Cs

start_stop_downloading = True
break_signal = False
button_on_color = '#525252'
button_off_color = '#282828'
background_color = '#808080'
window_size_x = 1030
window_size_y = 420

global lib_name
global tab_name
global path
global file_name
Interval_value = 1


def save_names_data(new_path, new_filename, new_interval, new_lib, new_tab):
    f = open("Additional_files/Parametry_pliku_i_bazy.txt", 'w')
    f.write(f'Ścieżka--{new_path.strip()}\n')
    f.write(f'Nazwa pliku--{new_filename.strip()}\n')
    f.write(f'Interwał--{new_interval}\n')
    f.write(f'Nazwa biblioteki--{new_lib.strip()}\n')
    f.write(f'Nazwa tabeli--{new_tab.strip()}\n')
    return


def Stringcheck(x):
    try:
        x = int(x)
        if 1 <= x <= 24:
            return True, ''
        else:
            return False, 'Wartość poza zakresem'
    except:
        return False, 'Wartość nie jest liczbą'


def Update_Listbox(errors, Listbox):
    Last_data = Listbox.get_list_values()
    Last_data[2:] = Last_data[0:11]
    Last_data[0] = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    Last_data[-1] = ''
    if not errors[2]:
        Last_data[1] = 'Błędna nazwa pliku lub ścieżka'
    else:
        if errors[0]:
            if errors[1][0]:
                Last_data[1] = 'Brak połączenia z bazą'
            elif errors[1][1]:
                Last_data[1] = 'Błąd nazwy tabeli lub biblioteki'
        else:
            Last_data[1] = 'Zapis poprawny'

    Listbox.update(values=Last_data)

    return


def get_break_signal():
    return break_signal


def get_start_stop_downloading():
    return start_stop_downloading


def get_Interval_value():
    return Interval_value


def get_names_data():
    return path, file_name, lib_name, tab_name


def Turn_Gui_on():
    global Interval_value
    global start_stop_downloading
    global break_signal
    global lib_name
    global tab_name
    global path
    global file_name
    path, file_name, Interval_string, lib_name, tab_name = Layout.get_names_data()
    Interval_value = int(Interval_string)
    start_stop_downloading = True
    window = Layout.make_window()

    while True:
        event, values = window.read(timeout=50)
        if event == sg.WIN_CLOSED:
            break
        if event == 'Apply_all':
            Check_value = Stringcheck(values['Interval'])
            window['Error_interval'].update(Check_value[1])
            if Check_value[0]:
                Interval_value = int(values['Interval'])
            lib_name = values['Library']
            tab_name = values['Table']
            path = values['Path']
            file_name = values['File_name']
            save_names_data(path, file_name, Interval_value, lib_name, tab_name)

        if Cs.ready_to_update():
            Cs.reset_proccess()
            Update_Listbox(Cs.get_error(), window['Text_Listbox'])

        if event == 'Start_stop_button':
            start_stop_downloading = not start_stop_downloading
            if start_stop_downloading:
                window['Start_stop_button'].update("Stop")
                window['Start_stop_button'].update(button_color=button_on_color)
            else:
                window['Start_stop_button'].update("Start")
                window['Start_stop_button'].update(button_color=button_off_color)
    window.close()
    break_signal = True
