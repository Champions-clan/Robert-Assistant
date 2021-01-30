from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
import keyboard 

os.system('python ./App/GUI.py')

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

icon = QIcon("./Assets/Robert logo.png")

tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

menu = QMenu()
btn = QAction("Robert")
btn.triggered.connect(lambda: os.system('python ./App/GUI.py'))

menu.addAction(btn)

quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

keyboard.add_hotkey('shift+6', lambda: os.system('python ./App/GUI.py')) 
keyboard.add_hotkey('shift+7', lambda: os.system('python ./App/GUI.py')) 

tray.setContextMenu(menu)
app.exec_()