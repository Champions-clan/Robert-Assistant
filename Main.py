from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
import keyboard
from App.db_worker import Alarms
import schedule
from notifypy import Notify

os.system('python ./App/GUI.py')


app = QApplication([])
app.setQuitOnLastWindowClosed(False)

icon = QIcon("./Assets/Robert logo.png")


tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

menu = QMenu()
btn = QAction("Home Page")
btn2 = QAction("Robert Listner")
btn.triggered.connect(lambda: os.system('python ./App/GUI.py'))
btn2.triggered.connect(lambda: os.system('python ./App/Robert.pyw'))

menu.addAction(btn)
menu.addAction(btn2)

quit = QAction("Quit")
quit.triggered.connect(lambda: exit())
menu.addAction(quit)

keyboard.add_hotkey('shift+6', lambda: os.system('python ./App/GUI.py'))
keyboard.add_hotkey('shift+7', lambda: os.system('python ./App/Robert.pyw'))

tray.setContextMenu(menu)

def this_will_run_when_alarm_rings(alarm):
    if alarm[2] == 0:
        pass
    else:
        alarm_ = Alarms()
        time = alarm_.convert_to_12_hour_clock(minutes_from_minight=alarm[4])
        notification = Notify()
        notification.title = alarm[1]
        notification.message = f"The time is {time[0]}:{time[1]} {time[2]}"
        notification.icon = "./Assets/Robert Logo.png"
        notification.audio = "./Assets/beep.wav"
        notification.send()
    alarm_.delete_alarm(alarm[0])

alarm_manager = Alarms()
def listen():
    alarm_manager.listen_for_alarms(this_will_run_when_alarm_rings)

schedule.every().minute.at(':00').do(listen)

while True:
    schedule.run_pending()

app.exec_()
