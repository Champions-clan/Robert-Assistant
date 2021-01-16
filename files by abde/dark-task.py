from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton,QMainWindow, QTextEdit


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

        self.robert_label = QtWidgets.QLabel("      Robert Task")
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
#-----------------code adding window------------------------------------------------
        def code_text(txt):
            print(type(txt))
            self.files_set_DialogWindow = QtWidgets.QDialog()
            self.files_set_DialogWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.files_set_DialogWindow.resize(380, 300)
            self.files_set_DialogWindow.setMinimumSize(QtCore.QSize(380, 300))
            self.files_set_DialogWindow.setMaximumSize(QtCore.QSize(380, 300))
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
""")
            self.dialog_ok_btn = QtWidgets.QPushButton(self.files_set_DialogWindow)
            self.dialog_ok_btn.setGeometry(QtCore.QRect(15, 235, 151, 51))
            if txt == "Name":
                self.dialog_ok_btn.setText("Add")
            else:
                self.dialog_ok_btn.setText("Save")
            self.dialog_cancel_btn = QtWidgets.QPushButton(self.files_set_DialogWindow)
            self.dialog_cancel_btn.setGeometry(QtCore.QRect(175, 235, 151, 51))
            self.dialog_cancel_btn.setText("Cancel")
            self.dialog_cancel_btn.clicked.connect(self.files_set_DialogWindow.accept)
            self.dialog_textEdit = QtWidgets.QTextEdit(self.files_set_DialogWindow)
            self.dialog_textEdit.setGeometry(QtCore.QRect(20, 80, 291, 41))
            self.dialog_textEdit.setPlaceholderText("Name")
            self.dialoggg_textEdit = QtWidgets.QTextEdit(self.files_set_DialogWindow)
            self.dialoggg_textEdit.setGeometry(QtCore.QRect(20, 140, 350, 71))
            self.dialoggg_textEdit.setPlaceholderText("Description")
            self.dialog_label = QtWidgets.QLabel(self.files_set_DialogWindow)
            self.dialog_label.setGeometry(QtCore.QRect(60, 20, 231, 41))
            self.dialog_label.setText(f"{txt} your Task")

            self.files_set_DialogWindow.exec_()

#-----------------end of code adding--------------------------------------

        self.addcode_btn.clicked.connect(lambda checked, t="Name":code_text(t))
        self.top_horizontalLayout = QtWidgets.QHBoxLayout()
        self.verticalLayout.addLayout(self.horizontalLayout)

        combobox_list = ["Newest", "Alphabet"]

        self.choice_group = QtWidgets.QComboBox()
        self.choice_group.setFixedSize(200,30)
        self.choice_group.addItems(combobox_list)
        self.choice_group.setStyleSheet(
'''
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
'''
)
        self.sort_label = QtWidgets.QLabel("Sort by")
        self.sort_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.sort_layout = QtWidgets.QVBoxLayout()
        self.sort_layout.addWidget(self.sort_label)
        self.sort_layout.addWidget(self.choice_group)
        self.top_horizontalLayout.addLayout(self.sort_layout)
        self.top_horizontalLayout.addStretch(20)
        self.top_horizontalLayout.addWidget(self.addcode_btn)
        

        self.verticalLayout.addLayout(self.top_horizontalLayout)


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
        def show_des(btn_info):
            print(btn_info)
            self.task_show_widget = QtWidgets.QDialog()
            self.task_show_widget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.task_show_widget.resize(350, 220)
            self.task_show_widget.setMinimumSize(QtCore.QSize(350, 220))
            self.task_show_widget.setMaximumSize(QtCore.QSize(350, 220))
            self.task_show_widget.setStyleSheet("""
QDialog {
background-color: #36393f;
}
QLabel {
font-family: 'Titillium Web', sans-serif;
font-size: 30px;
}
QPushButton {
background-color: transparent;
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
""")
            self.exit_btn = QtWidgets.QPushButton(self.task_show_widget)
            self.exit_btn.setIcon(QtGui.QIcon("icons\\exit_icon"))
            self.exit_btn.setIconSize(QtCore.QSize(20, 20))
            self.exit_btn.setGeometry(QtCore.QRect(315, 5, 25, 25))
            self.exit_btn.clicked.connect(self.task_show_widget.accept)
                

            self.des_label = QtWidgets.QLabel(self.task_show_widget)
            self.des_label.setText(f"Description:\n  You clicked {btn_info}")
            self.des_label.setGeometry(QtCore.QRect(10, 10, 300, 180))

            self.task_show_widget.exec_()

        self.scrollArea.setStyleSheet("background-color: #2f3136; border-radius: 7px;")
        self.scrollAreaWidgetContents = QtWidgets.QWidget(self.scrollArea)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)

        for i,s in enumerate(files):
            btn_horizontal = QtWidgets.QHBoxLayout()
            finished_btn = QtWidgets.QCheckBox()
            finished_btn.setFixedSize(50,50)
            #finished_btn.setChecked(True)
            finished_btn.setStyleSheet("""

QCheckBox::indicator {
    border-radius: 5px;
    width: 15px;
    height: 15px;
}
QCheckBox::indicator:unchecked {
    background-color: #CC0000;
    color: #000000;
}
QCheckBox::indicator:checked {
    background-color: #00CC00;
}
""")
            btn_horizontal.addWidget(finished_btn)


            main_btn = QtWidgets.QPushButton(files[i])
            main_btn.setFixedSize(250,60)
            main_btn.setStyleSheet(
'''
QPushButton {
    color: #FFFFFF;
    background-color: #202225;
    font-family: 'Roboto Mono', monospace;
    font-size: 20px;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    border-top-right-radius: 0px;
    border-bottom-right-radius: 0px;
}
QPushButton:hover {
    background-color: #40444b;
}
QPushButton:pressed {
    background-color: #18191c;
}
''')
            main_btn.clicked.connect(lambda checked, btn_text=s:show_des(btn_text))
    
            edit_btn = QPushButton()   #39DFA2
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
            edit_btn.clicked.connect(lambda checked, t="Edit":code_text(t))
            del_btn = QPushButton()
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
            btn_horizontal.addWidget(main_btn)
            btn_horizontal.addWidget(edit_btn)
            btn_horizontal.addWidget(del_btn)
            self.formLayout.addRow(btn_horizontal)

        def combo(index):
            global files
            print(self.choice_group.itemText(index))
            #i = self.choice_group.itemText(index)
            if index == 0:
                files = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
            if index == 1:
                files = ["Alphabet","Alphabet","Alphabet","Alphabet","Alphabet"]
            elif index == 2:
                files = ["Newest","Newest","Newest","Newest","Newest"]

            self.scrollAreaWidgetContents.deleteLater()
            self.scrollAreaWidgetContents = QtWidgets.QWidget(self.scrollArea)
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)
            self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)

            for i,s in enumerate(files):
                btn_horizontal = QtWidgets.QHBoxLayout()
                finished_btn = QtWidgets.QCheckBox()
                finished_btn.setFixedSize(50,50)
                #finished_btn.setChecked(True)
                finished_btn.setStyleSheet("""
QCheckBox::indicator {
    border-radius: 5px;
    width: 15px;
    height: 15px;
}
QCheckBox::indicator:unchecked {
    background-color: #CC0000;
    color: #000000;
}
QCheckBox::indicator:checked {
    background-color: #00CC00;
}
""")
                btn_horizontal.addWidget(finished_btn)
                main_btn = QPushButton(files[i])
                main_btn.setFixedSize(250,60)
                main_btn.setStyleSheet(
'''
QPushButton {
    color: #FFFFFF;
    background-color: #202225;
    font-family: 'Roboto Mono', monospace;
    font-size: 20px;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    border-top-right-radius: 0px;
    border-bottom-right-radius: 0px;
}
QPushButton:hover {
    background-color: #40444b;
}
QPushButton:pressed {
    background-color: #18191c;
}
''')
                main_btn.clicked.connect(lambda checked, btn_text=s:show_des(btn_text))
                edit_btn = QPushButton()   #39DFA2
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
                del_btn = QPushButton()
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
                btn_horizontal.addWidget(main_btn)
                btn_horizontal.addWidget(edit_btn)
                btn_horizontal.addWidget(del_btn)
                self.formLayout.addRow(btn_horizontal)
        self.choice_group.activated.connect(combo)
        

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
