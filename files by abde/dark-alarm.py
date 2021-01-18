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

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.trans_home_btn = QtWidgets.QPushButton()
        self.trans_home_btn.setIcon(QtGui.QIcon("pic\\home"))
        self.trans_home_btn.setIconSize(QtCore.QSize(25, 25))
        self.trans_home_btn.setFixedSize(40,40)
        self.trans_home_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #40444b;
}
QPushButton:pressed {
    background-color: #202225;
}
''')

        self.robert_label = QtWidgets.QLabel(" Robert Alarm")
        self.robert_label.setStyleSheet(
'''
QLabel {
    color: #FFFFFF;
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
''')
        self.title_layout = QtWidgets.QHBoxLayout()
        self.title_layout.addWidget(self.trans_home_btn)
        self.title_layout.addWidget(self.robert_label)
        

        
        self.addcode_btn = QtWidgets.QPushButton()
        self.addcode_btn.setIcon(QtGui.QIcon("icons\\add_btn.png"))
        self.addcode_btn.setIconSize(QtCore.QSize(40, 40))
        self.addcode_btn.setFixedSize(70,50)
        self.addcode_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-radius: 12px;
}
QPushButton:hover {
    background-color: #40444b;
}
QPushButton:pressed {
    background-color: #202225;
}
''')
        self.title_layout.addWidget(self.addcode_btn)
        self.verticalLayout.addLayout(self.title_layout)
#-----------------alarm adding window------------------------------------------------
        def add_alarm_window(txt):
            self.files_set_DialogWindow = QtWidgets.QDialog()
            self.files_set_DialogWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.files_set_DialogWindow.resize(400, 300)
            #self.files_set_DialogWindow.setMinimumSize(QtCore.QSize(480, 300))
            #self.files_set_DialogWindow.setMaximumSize(QtCore.QSize(480, 300))
            self.files_set_DialogWindow.setStyleSheet("""
QDialog {
background-color: #36393f;
}
QLabel {
font-family: 'Titillium Web', sans-serif;
font-size: 30px;
}
QPushButton {
background-color: #202225;
border-radius: 5px;
font-family: 'Roboto Mono', monospace;
font-size: 20px;
}
QPushButton:hover {
background-color: #40444b;
}
QPushButton:pressed {
background-color: #18191c;
}
QTextEdit{
background-color: #40444b;
font-family: 'Cabin', sans-serif;
font-size: 20px;
border-radius: 5px;
}
QSpinBox {
    color: #FFFFFF;
	background-color: #2f3136;
    font-size: 15px;
	border-radius: 5px;
	padding: 5px;
	padding-left: 10px;
}
QSpinBox QAbstractItemView {
	color: #FFFFFF;	
	background-color: #2f3136;
	padding: 10px;
	selection-background-color: #40444b;
}
QComboBox{
    color: #FFFFFF;
	background-color: #2f3136;
    font-size: 15px;
	border-radius: 5px;
	padding: 5px;
	padding-left: 10px;
}
QComboBox QAbstractItemView {
	color: #FFFFFF;	
	background-color: #2f3136;
	padding: 10px;
	selection-background-color: #40444b;
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
        self.addcode_btn.clicked.connect(lambda : add_alarm_window("Add"))
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        MainWindow.setStyleSheet(
"QMainWindow {"
"   background-color: #36393f;"
"}"
"QScrollArea {"
"background-color: #2ABF88"
"}"        
"/* VERTICAL SCROLLBAR */"
" QScrollBar:vertical {"
"    border: none;"
"    background: #2f3136;"
"    width: 14px;"
"    margin: 15px 0 15px 0;"
"    "
" }"
""
"/*  HANDLE BAR VERTICAL */"
"QScrollBar::handle:vertical {    "
"    background-color: #202225;"
"    min-height: 30px;"
"    "
"}"
"QScrollBar::handle:vertical:hover{    "
"    background-color: #40444b;"
"}"
"QScrollBar::handle:vertical:pressed {    "
"    background-color: #18191c;"
"}"
""
"/* BTN TOP - SCROLLBAR */"
"QScrollBar::sub-line:vertical {"
"    border: none;"
"    background-color: #202225;"
"    height: 15px;"
"    border-top-left-radius: 7px;"
"    border-top-right-radius: 7px;"
"    subcontrol-position: top;"
"    subcontrol-origin: margin;"
"}"
"QScrollBar::sub-line:vertical:hover {    "
"    background-color: #40444b;"
"}"
"QScrollBar::sub-line:vertical:pressed {    "
"    background-color: #18191c;"
"}"
""
"/* BTN BOTTOM - SCROLLBAR */"
"QScrollBar::add-line:vertical {"
"    border: none;"
"    background-color: #202225;"
"    height: 15px;"
"    border-bottom-left-radius: 7px;"
"    border-bottom-right-radius: 7px;"
"    subcontrol-position: bottom;"
"    subcontrol-origin: margin;"
"}"
"QScrollBar::add-line:vertical:hover {    "
"    background-color: #40444b;"
"}"
"QScrollBar::add-line:vertical:pressed {    "
"    background-color: #18191c;"
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
        self.scrollArea.setStyleSheet("background: #2f3136; border-radius: 7px;")
        self.scrollAreaWidgetContents = QtWidgets.QWidget(self.scrollArea)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.cond_lst = ["icons\\off.png", "icons\\on.png"]
        self.cond_text = ["Off", "On"]
        self.cond = {}
        def create_alarm_btn(btn, i, s):
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
    background-color: #202225;
}
QPushButton:pressed {
    background-color: #18191c;
}
""")
            def alarm_switch():
                self.cond[btn] = not self.cond[btn]
                btn.setIcon(QtGui.QIcon(self.cond_lst[self.cond[btn]]))
                btn.setText(self.cond_text[self.cond[btn]])
            btn.clicked.connect(lambda: alarm_switch())

        for i,s in enumerate(files):
            btn_horizontal = QtWidgets.QHBoxLayout()
            self.alarm_switch_btn = QtWidgets.QPushButton()
            create_alarm_btn(self.alarm_switch_btn, i, s)
            
            main_btn = QtWidgets.QLabel()
            main_btn.setFixedSize(240,60)
            main_btn.setText(files[i])
            main_btn.setAlignment(QtCore.Qt.AlignCenter)
            main_btn.setStyleSheet(
'''
QLabel {
    color: #FFFFFF;
    background-color: #37393D;
    font-family: 'Roboto Mono', monospace;
    font-size: 20px;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    border-top-right-radius: 0px;
    border-bottom-right-radius: 0px;
}
''')

            edit_btn = QtWidgets.QPushButton()   #39DFA2
            edit_btn.setIcon(QtGui.QIcon("icons\\edit_icon.png"))
            edit_btn.setIconSize(QtCore.QSize(28, 28))
            edit_btn.setFixedSize(30,60)  
            edit_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-radius: 0px;
}
QPushButton:hover {
    background-color: #202225;
}
QPushButton:pressed {
    background-color: #18191c;
}
''')
            edit_btn.clicked.connect(lambda : add_alarm_window("Edit"))

            del_btn = QtWidgets.QPushButton()
            del_btn.setIcon(QtGui.QIcon("icons/del_icon.png"))
            del_btn.setIconSize(QtCore.QSize(28, 28))
            del_btn.setFixedSize(30,60)   #39DFA2
            del_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-top-left-radius: 0;
    border-bottom-left-radius: 00px;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
}
QPushButton:hover {
    background-color: #202225;
}
QPushButton:pressed {
    background-color: #18191c;
}
''')
            btn_horizontal.addWidget(self.alarm_switch_btn)
            btn_horizontal.addWidget(main_btn)
            btn_horizontal.addWidget(edit_btn)
            btn_horizontal.addWidget(del_btn)
            self.formLayout.addRow(btn_horizontal)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


#files = ['Abdella','Harish','Rajvir','Dawn','Ahmed','celen','trump','ok','bye','morning','evening','afternoon','mame','abdesol','aklon','you','me','we','are','happy','nice','cool']
import os
#files = [name.split('.')[0] for name in os.listdir('.\codes') if name.split('.')[1] == "txt"]

files = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow,files)
    MainWindow.show()
    sys.exit(app.exec_())
