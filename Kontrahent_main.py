import time
import Gui
import Time_counter
from threading import Thread

Thread(target=Gui.Turn_Gui_on).start()
time.sleep(1)
Thread(target=Time_counter.timecounting).start()

