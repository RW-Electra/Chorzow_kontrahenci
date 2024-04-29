import time
import Gui
from threading import Thread
import Control_saving_txt as Cs


def timecounting():
    start_time = time.time()
    Interval = Gui.get_Interval_value()
    previous_interval = Interval
    next_timestamp = start_time + Interval * 3600
    while True:
        time.sleep(0.5)
        Interval = Gui.get_Interval_value()
        break_signal = Gui.get_break_signal()
        if Gui.get_start_stop_downloading():
            if previous_interval != Interval:
                previous_interval = Interval
                next_timestamp = start_time + Interval * 3600
            if time.time() > next_timestamp:
                start_time = next_timestamp
                next_timestamp += Interval * 3600
                path, filename, library, tablename = Gui.get_names_data()
                Dictionary_thread = Thread(target=Cs.File_to_database,
                                           args=[path, filename, library, tablename])
                Dictionary_thread.start()
        else:
            if next_timestamp - time.time() < Interval * (-3600):
                next_timestamp += Interval * 3600
        if break_signal:
            break

