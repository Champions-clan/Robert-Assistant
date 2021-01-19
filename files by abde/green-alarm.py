from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QPushButton,QMainWindow, QTextEdit


class Ui_MainWindow(object):
    def __init__(self, MainWindow, files):
        self.files = files
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 500)
        #MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MainWindow.setMinimumSize(QtCore.QSize(430, 500))
        MainWindow.setMaximumSize(QtCore.QSize(430, 500))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        QtGui.QFontDatabase.addApplicationFont("fonts\\RobotoMono-Regular.ttf")
        QtGui.QFontDatabase.addApplicationFont("fonts\\TitilliumWeb-Bold.ttf")
        QtGui.QFontDatabase.addApplicationFont("fonts\\Cabin-Medium.ttf")
        QtGui.QFontDatabase.addApplicationFont("fonts\\Goldman-Bold.ttf")  
        QtGui.QFontDatabase.addApplicationFont("fonts\\PirataOne-Regular.ttf") 

        self.green_alarm_centralwidget = QtWidgets.QWidget(MainWindow)
        self.green_alarm_verticalLayout = QtWidgets.QVBoxLayout(self.green_alarm_centralwidget)

        self.green_alarm_home_btn = QtWidgets.QPushButton()
        self.green_alarm_home_btn.setIcon(QtGui.QIcon("pic\\home"))
        self.green_alarm_home_btn.setIconSize(QtCore.QSize(25, 25))
        self.green_alarm_home_btn.setFixedSize(40,40)
        self.green_alarm_home_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #24E29D;
}
QPushButton:pressed {
    background-color: #1A4E3B;
}
''')

        self.green_alarm_title_label = QtWidgets.QLabel(" Robert Alarm")
        self.green_alarm_title_label.setStyleSheet(
'''
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
''')
        self.green_alarm_title_layout = QtWidgets.QHBoxLayout()
        self.green_alarm_title_layout.addWidget(self.green_alarm_home_btn)
        self.green_alarm_title_layout.addWidget(self.green_alarm_title_label)
        

        self.green_alarm_addcode_btn = QtWidgets.QPushButton()
        self.green_alarm_addcode_btn.setIcon(QtGui.QIcon("icons\\add_btn.png"))
        self.green_alarm_addcode_btn.setIconSize(QtCore.QSize(40, 40))
        self.green_alarm_addcode_btn.setFixedSize(70,50)
        self.green_alarm_addcode_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-radius: 12px;
}
QPushButton:hover {
    background-color: #24E29D;
}
QPushButton:pressed {
    background-color: #1A4E3B;
}
''')
        self.green_alarm_title_layout.addWidget(self.green_alarm_addcode_btn)
        self.green_alarm_verticalLayout.addLayout(self.green_alarm_title_layout)
#-----------------alarm adding window------------------------------------------------
        def green_alarm_add_window(txt):
            self.files_set_DialogWindow = QtWidgets.QDialog()
            self.files_set_DialogWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.files_set_DialogWindow.resize(400, 300)
            #self.files_set_DialogWindow.setMinimumSize(QtCore.QSize(480, 300))
            #self.files_set_DialogWindow.setMaximumSize(QtCore.QSize(480, 300))
            self.files_set_DialogWindow.setStyleSheet("""
QDialog {
    background-color: #14B57A;
}
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 30px;
}
QPushButton {
    background-color: #39DFA2;
    border-radius: 5px;
    font-family: 'Roboto Mono', monospace;
    font-size: 20px;
}
QPushButton:hover {
    background-color: #27A97A;
}
QPushButton:pressed {
    background-color: #1A4E3B;
}
QTextEdit{
    background-color: #24E29D;
    font-family: 'Cabin', sans-serif;
    font-size: 20px;
    border-radius: 5px;
}
QSpinBox {
    background-color: #39DFA2;
    font-size: 15px;
	border-radius: 5px;
	padding: 5px;
	padding-left: 10px;
}
QSpinBox QAbstractItemView {
	color: #000000;	
	background-color: #2ABF88;
	padding: 10px;
	selection-background-color: #2ABF88;
}
QComboBox{
	background-color: #39DFA2;
    font-size: 15px;
	border-radius: 5px;
	padding: 5px;
	padding-left: 10px;
}
QComboBox QAbstractItemView {
	color: #000000;	
	background-color: #2ABF88;
	padding: 10px;
	selection-background-color: #2ABF88;
}
""")
            self.alarm_add_layout = QtWidgets.QVBoxLayout(self.files_set_DialogWindow)
            self.alarm_ok_layout = QtWidgets.QHBoxLayout()
            self.dialog_ok_btn = QtWidgets.QPushButton(s)
            if txt == "Add":
                self.dialog_ok_btn.setText("Add")
            else:
                self.dialog_ok_btn.setText("Save")
            self.dialog_cancel_btn = QtWidgets.QPushButton()
            self.dialog_cancel_btn.setText("Cancel")
            self.dialog_cancel_btn.clicked.connect(lambda: self.files_set_DialogWindow.reject())
            self.alarm_ok_layout.addWidget(self.dialog_ok_btn)
            self.alarm_ok_layout.addWidget(self.dialog_cancel_btn)

            self.dialog_textEdit = QtWidgets.QTextEdit()
            self.dialog_textEdit.setPlaceholderText("Name")
            self.dialog_textEdit.setFixedHeight(50)
            self.dialog_label = QtWidgets.QLabel()
            self.dialog_label.setText(f"{txt} your Alarm")

            self.alarm_hour_add = QtWidgets.QSpinBox()
            self.alarm_hour_add.setRange(1,12)
            self.alarm_minute_add = QtWidgets.QSpinBox()
            self.alarm_minute_add.setRange(0,59)

            self.alarm_time_add_layout = QtWidgets.QHBoxLayout()
            self.alarm_hour_layout = QtWidgets.QVBoxLayout()
            self.alarm_minute_layout = QtWidgets.QVBoxLayout()

            self.alarm_hour_label = QtWidgets.QLabel()
            self.alarm_hour_label.setText("Hour")
            self.alarm_hour_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
            self.alarm_minute_label = QtWidgets.QLabel()
            self.alarm_minute_label.setText("Minute")
            self.alarm_minute_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
            
            self.alarm_hour_layout.addWidget(self.alarm_hour_label)
            self.alarm_hour_layout.addWidget(self.alarm_hour_add)
            self.alarm_minute_layout.addWidget(self.alarm_minute_label)
            self.alarm_minute_layout.addWidget(self.alarm_minute_add)

            self.alarm_mid_group = QtWidgets.QComboBox()
            self.alarm_mid_group.addItems(["AM", "PM"])
            

            self.alarm_time_add_layout.addLayout(self.alarm_hour_layout)
            self.alarm_time_add_layout.addLayout(self.alarm_minute_layout)
            self.alarm_mid_group_layout = QtWidgets.QVBoxLayout()
            self.alarm_mid_group_layout.addStretch(2)
            self.alarm_mid_group_layout.addWidget(self.alarm_mid_group)
            self.alarm_time_add_layout.addLayout(self.alarm_mid_group_layout)

            self.alarm_other_layout = QtWidgets.QHBoxLayout()
            self.alarm_repeats_label = QtWidgets.QLabel("Repeats")
            self.alarm_repeats_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
            self.alarm_sound_label = QtWidgets.QLabel("Sound")
            self.alarm_sound_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
            self.alarm_repeats_add = QtWidgets.QComboBox()
            self.alarm_repeats_add.addItems(["Only Once", "Every day", "Every week", "Every Month"])
            self.alarm_sound_add = QtWidgets.QComboBox()
            self.alarm_sound_add.addItems(["sound A", "sound B", "sound C", "sound D", "sound E"])

            self.alarm_repeats_layout = QtWidgets.QVBoxLayout()
            self.alarm_repeats_layout.addWidget(self.alarm_repeats_label)
            self.alarm_repeats_layout.addWidget(self.alarm_repeats_add)
            self.alarm_sound_layout = QtWidgets.QVBoxLayout()
            self.alarm_sound_layout.addWidget(self.alarm_sound_label)
            self.alarm_sound_layout.addWidget(self.alarm_sound_add)

            self.alarm_other_layout.addLayout(self.alarm_repeats_layout)
            self.alarm_other_layout.addLayout(self.alarm_sound_layout)


            self.alarm_add_layout.addWidget(self.dialog_label)
            self.alarm_add_layout.addWidget(self.dialog_textEdit)
            self.alarm_add_layout.addLayout(self.alarm_time_add_layout)
            self.alarm_add_layout.addLayout(self.alarm_other_layout)
            self.alarm_add_layout.addLayout(self.alarm_ok_layout)

            self.files_set_DialogWindow.exec_()

#-----------------end of code adding--------------------------------------
        self.green_alarm_addcode_btn.clicked.connect(lambda : green_alarm_add_window("Add"))
        self.green_alarm_scroll_Area = QtWidgets.QScrollArea(self.green_alarm_centralwidget)
        self.green_alarm_scroll_Area.setWidgetResizable(True)
        MainWindow.setStyleSheet(
"QMainWindow {"
"   background: #14B57A;"
"}"
"QScrollArea {"
"background-color: #2ABF88"
"}"        
"/* VERTICAL SCROLLBAR */"
" QScrollBar:vertical {"
"    border: none;"
"    background: #40A681;"
"    width: 14px;"
"    margin: 15px 0 15px 0;"
"    "
" }"
""
"/*  HANDLE BAR VERTICAL */"
"QScrollBar::handle:vertical {    "
"    background-color: #3ABA8B;"
"    min-height: 30px;"
"    "
"}"
"QScrollBar::handle:vertical:hover{    "
"    background-color: #0BE494;"
"}"
"QScrollBar::handle:vertical:pressed {    "
"    background-color: #05D085;"
"}"
""
"/* BTN TOP - SCROLLBAR */"
"QScrollBar::sub-line:vertical {"
"    border: none;"
"    background-color: #1F986C;"
"    height: 15px;"
"    border-top-left-radius: 7px;"
"    border-top-right-radius: 7px;"
"    subcontrol-position: top;"
"    subcontrol-origin: margin;"
"}"
"QScrollBar::sub-line:vertical:hover {    "
"    background-color: #40A681;"
"}"
"QScrollBar::sub-line:vertical:pressed {    "
"    background-color: #1A6C4E;"
"}"
""
"/* BTN BOTTOM - SCROLLBAR */"
"QScrollBar::add-line:vertical {"
"    border: none;"
"    background-color: #1F986C;"
"    height: 15px;"
"    border-bottom-left-radius: 7px;"
"    border-bottom-right-radius: 7px;"
"    subcontrol-position: bottom;"
"    subcontrol-origin: margin;"
"}"
"QScrollBar::add-line:vertical:hover {    "
"    background-color: #40A681;"
"}"
"QScrollBar::add-line:vertical:pressed {    "
"    background-color: #1A6C4E;"
"}"
""
"/* RESET ARROW */"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {"
"    background: none;"
"}"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {"
"    background: none;"
"}"
)
        self.green_alarm_scroll_Area.setStyleSheet("background: #2ABF88; border-radius: 7px;")
        self.green_alarm_scroll_AreaWidgetContents = QtWidgets.QWidget(self.green_alarm_scroll_Area)
        self.green_alarm_scroll_Area.setWidget(self.green_alarm_scroll_AreaWidgetContents)

        self.green_alarm_verticalLayout.addWidget(self.green_alarm_scroll_Area)

        MainWindow.setCentralWidget(self.green_alarm_centralwidget)

        self.green_alarm_scrollArea_formLayout = QtWidgets.QFormLayout(self.green_alarm_scroll_AreaWidgetContents)
        self.cond_lst = ["icons\\off.png", "icons\\on.png"]
        self.cond_text = ["Off", "On"]
        self.cond = {}
        def green_alarm_create_alarm_btn(btn, i, s):
            self.cond[btn] = 0
            btn.setFixedSize(60,35)
            btn.setIcon(QtGui.QIcon(self.cond_lst[self.cond[btn]]))
            btn.setIconSize(QtCore.QSize(40,35))
            btn.setText(self.cond_text[self.cond[btn]])
            btn.setStyleSheet("""
QPushButton {
    background-color: transparent;
    font-size: 12px;
}
QPushButton:hover {
    background-color: #27A97A;
}
QPushButton:pressed {
    background-color: #1A4E3B;
}
""")
            def alarm_switch():
                self.cond[btn] = not self.cond[btn]
                btn.setIcon(QtGui.QIcon(self.cond_lst[self.cond[btn]]))
                btn.setText(self.cond_text[self.cond[btn]])
            btn.clicked.connect(lambda: alarm_switch())

        for i,s in enumerate(files):
            green_alarm_create_scroll_btn_layout = QtWidgets.QHBoxLayout()
            green_alarm_switch_btn = QtWidgets.QPushButton()
            green_alarm_create_alarm_btn(green_alarm_switch_btn, i, s)
            
            green_alarm_main_btn = QtWidgets.QPushButton()
            green_alarm_main_btn.setFixedSize(240,60)
            green_alarm_main_btn.setText(files[i])
            #green_alarm_main_btn.setAlignment(QtCore.Qt.AlignCenter)
            green_alarm_main_btn.setStyleSheet(
'''
QPushButton {
    background-color: #39DFA2;
    font-family: 'Roboto Mono', monospace;
    font-size: 20px;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    border-top-right-radius: 0px;
    border-bottom-right-radius: 0px;
}
QPushButton:hover {
    background-color: #27A97A;
}
QPushButton:pressed {
    background-color: #1A4E3B;
}
''')

            green_alarm_edit_btn = QtWidgets.QPushButton()   #39DFA2
            green_alarm_edit_btn.setIcon(QtGui.QIcon("icons\\edit_icon.png"))
            green_alarm_edit_btn.setIconSize(QtCore.QSize(28, 28))
            green_alarm_edit_btn.setFixedSize(30,60)  
            green_alarm_edit_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-radius: 0px;
}
QPushButton:hover {
    background-color: #27A97A;
}
QPushButton:pressed {
    background-color: #1A4E3B;
}
''')
            green_alarm_edit_btn.clicked.connect(lambda : green_alarm_add_window("Edit"))

            green_alarm_del_btn = QtWidgets.QPushButton()
            green_alarm_del_btn.setIcon(QtGui.QIcon("icons/del_icon.png"))
            green_alarm_del_btn.setIconSize(QtCore.QSize(28, 28))
            green_alarm_del_btn.setFixedSize(30,60)   #39DFA2
            green_alarm_del_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-top-left-radius: 0;
    border-bottom-left-radius: 00px;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
}
QPushButton:hover {
    background-color: #27A97A;
}
QPushButton:pressed {
    background-color: #1A4E3B;
}
''')
            green_alarm_create_scroll_btn_layout.addWidget(green_alarm_switch_btn)
            green_alarm_create_scroll_btn_layout.addWidget(green_alarm_main_btn)
            green_alarm_create_scroll_btn_layout.addWidget(green_alarm_edit_btn)
            green_alarm_create_scroll_btn_layout.addWidget(green_alarm_del_btn)
            self.green_alarm_scrollArea_formLayout.addRow(green_alarm_create_scroll_btn_layout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


#files = ['Abdella','Harish','Rajvir','Dawn','Ahmed','celen','trump','ok','bye','morning','evening','afternoon','mame','abdesol','aklon','you','me','we','are','happy','nice','cool']
import os
#files = [name.split('.')[0] for name in os.listdir('.\codes') if name.split('.')[1] == "txt"]
files = ["Study", "Lunch", f"Break fast", f"Dinner", f"Coding", f"Programming", f"Playing", f"Study"]
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow,files)
    MainWindow.show()
    sys.exit(app.exec_())
