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

        self.light_task_centralwidget = QtWidgets.QWidget(MainWindow)
        self.light_task_verticalLayout = QtWidgets.QVBoxLayout(self.light_task_centralwidget)
        self.light_task_title_layout = QtWidgets.QHBoxLayout()

        self.light_task_home_btn = QtWidgets.QPushButton()
        self.light_task_home_btn.setIcon(QtGui.QIcon("pic\\home"))
        self.light_task_home_btn.setIconSize(QtCore.QSize(25, 25))
        self.light_task_home_btn.setFixedSize(40,40)
        self.light_task_home_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-radius: 5px;
}
QPushButton:hover {
    background-color: #e3e5e8;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
''')

        self.light_task_title_label = QtWidgets.QLabel("      Robert Task")
        self.light_task_title_label.setStyleSheet(
'''
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
''')
        self.light_task_title_layout = QtWidgets.QHBoxLayout()
        self.light_task_title_layout.addWidget(self.light_task_home_btn)
        self.light_task_title_layout.addWidget(self.light_task_title_label)

        self.light_task_task_addcode_btn = QtWidgets.QPushButton()
        self.light_task_task_addcode_btn.setIcon(QtGui.QIcon("icons\\add_btn.png"))
        self.light_task_task_addcode_btn.setIconSize(QtCore.QSize(40, 40))
        self.light_task_task_addcode_btn.setFixedSize(70,50)
        self.light_task_task_addcode_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-radius: 12px;
}
QPushButton:hover {
    background-color: #e3e5e8;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
''')
        self.light_task_verticalLayout.addLayout(self.light_task_title_layout)
#-----------------code adding window------------------------------------------------
        def light_task_task_add_func(txt):
            self.files_set_DialogWindow = QtWidgets.QDialog()
            self.files_set_DialogWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.files_set_DialogWindow.resize(380, 350)
            self.files_set_DialogWindow.setStyleSheet("""
QDialog {
    background-color: #ffffff;
}
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 30px;
}
QPushButton {
    background-color: #e3e5e8;
    border-radius: 5px;
    font-family: 'Roboto Mono', monospace;
    font-size: 20px;
}
QPushButton:hover {
    background-color: #C9C9C9;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
QTextEdit{
    background-color: #ebedef;
    font-family: 'Cabin', sans-serif;
    font-size: 20px;
    border-radius: 5px;
}
QComboBox{
	background-color: #e3e5e8;
    font-size: 15px;
	border-radius: 5px;
	padding: 5px;
	padding-left: 10px;
}
QComboBox QAbstractItemView {
	color: #000000;	
	background-color: #e3e5e8;
	padding: 10px;
	selection-background-color: #e3e5e8;
}
""")
            self.task_add_layout = QtWidgets.QVBoxLayout(self.files_set_DialogWindow)
            self.task_ok_layout = QtWidgets.QHBoxLayout()
            self.dialog_ok_btn = QtWidgets.QPushButton(s)
            if txt == "Add":
                self.dialog_ok_btn.setText("Add")
            else:
                self.dialog_ok_btn.setText("Save")
            self.dialog_cancel_btn = QtWidgets.QPushButton()
            self.dialog_cancel_btn.setText("Cancel")
            self.dialog_cancel_btn.clicked.connect(lambda: self.files_set_DialogWindow.reject())
            self.task_ok_layout.addWidget(self.dialog_ok_btn)
            self.task_ok_layout.addWidget(self.dialog_cancel_btn)

            self.dialog_label = QtWidgets.QLabel()
            self.dialog_label.setText(f"{txt} your Alarm")
            self.dialog_textEdit = QtWidgets.QTextEdit()
            self.dialog_textEdit.setPlaceholderText("Name")
            self.dialog_textEdit.setFixedHeight(40)

            self.task_desc_add = QtWidgets.QTextEdit()
            self.task_desc_add.setPlaceholderText("Description")
            self.task_desc_add.setFixedHeight(75)


            self.task_other_layout = QtWidgets.QHBoxLayout()
            self.task_priority_label = QtWidgets.QLabel("Priority")
            self.task_priority_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 20px;")
            self.task_priority_add = QtWidgets.QComboBox()
            self.task_priority_add.setFixedHeight(40)
            self.task_priority_add.addItems(["1", "2", "3", "4", "5"])

            self.task_priority_layout = QtWidgets.QVBoxLayout()
            self.task_priority_layout.addWidget(self.task_priority_label)
            self.task_priority_layout.addWidget(self.task_priority_add)

            self.task_other_layout.addLayout(self.task_priority_layout)


            self.task_add_layout.addWidget(self.dialog_label)
            self.task_add_layout.addWidget(self.dialog_textEdit)
            self.task_add_layout.addWidget(self.task_desc_add)
            self.task_add_layout.addLayout(self.task_other_layout)
            self.task_add_layout.addLayout(self.task_ok_layout)

            self.files_set_DialogWindow.exec_()

#-----------------end of code adding--------------------------------------

        self.light_task_task_addcode_btn.clicked.connect(lambda checked, t="Add":light_task_task_add_func(t))
        self.light_task_second_layout = QtWidgets.QHBoxLayout()

        task_sort_combo_lst = ["Newest", "Priority", "Alphabet"]

        self.light_task_sort_combo = QtWidgets.QComboBox()
        self.light_task_sort_combo.setFixedSize(200,30)
        self.light_task_sort_combo.addItems(task_sort_combo_lst)
        self.light_task_sort_combo.setStyleSheet(
'''
QComboBox{
	background-color: #e3e5e8;
    font-size: 15px;
	border-radius: 5px;
	padding: 5px;
	padding-left: 10px;
}
QComboBox QAbstractItemView {
	color: #000000;	
	background-color: #e3e5e8;
	padding: 10px;
	selection-background-color: #e3e5e8;
}
'''
)
        self.light_task_sort_label = QtWidgets.QLabel("Sort by")
        self.light_task_sort_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.light_task_sort_layout = QtWidgets.QVBoxLayout()
        self.light_task_sort_layout.addWidget(self.light_task_sort_label)
        self.light_task_sort_layout.addWidget(self.light_task_sort_combo)
        self.light_task_second_layout.addLayout(self.light_task_sort_layout)
        self.light_task_second_layout.addStretch(20)
        self.light_task_second_layout.addWidget(self.light_task_task_addcode_btn)
        

        self.light_task_verticalLayout.addLayout(self.light_task_second_layout)


        self.light_task_scrollArea = QtWidgets.QScrollArea(self.light_task_centralwidget)
        self.light_task_scrollArea.setWidgetResizable(True)
        MainWindow.setStyleSheet(
"QMainWindow {"
"   background: #ffffff;"
"}"
"QScrollArea {"
"background-color: #f2f3f5"
"}"        
"/* VERTICAL SCROLLBAR */"
" QScrollBar:vertical {"
"    border: none;"
"    background: #e3e5e8;"
"    width: 14px;"
"    margin: 15px 0 15px 0;"
"    "
" }"
""
"/*  HANDLE BAR VERTICAL */"
"QScrollBar::handle:vertical {    "
"    background-color: #D0D0D0;"
"    min-height: 30px;"
"    "
"}"
"QScrollBar::handle:vertical:hover{    "
"    background-color: #B7B7B7;"
"}"
"QScrollBar::handle:vertical:pressed {    "
"    background-color: #A9A9A9;"
"}"
""
"/* BTN TOP - SCROLLBAR */"
"QScrollBar::sub-line:vertical {"
"    border: none;"
"    background-color: #D0D0D0;"
"    height: 15px;"
"    border-top-left-radius: 7px;"
"    border-top-right-radius: 7px;"
"    subcontrol-position: top;"
"    subcontrol-origin: margin;"
"}"
"QScrollBar::sub-line:vertical:hover {    "
"    background-color: #B7B7B7;"
"}"
"QScrollBar::sub-line:vertical:pressed {    "
"    background-color: #A9A9A9;"
"}"
""
"/* BTN BOTTOM - SCROLLBAR */"
"QScrollBar::add-line:vertical {"
"    border: none;"
"    background-color: #D0D0D0;"
"    height: 15px;"
"    border-bottom-left-radius: 7px;"
"    border-bottom-right-radius: 7px;"
"    subcontrol-position: bottom;"
"    subcontrol-origin: margin;"
"}"
"QScrollBar::add-line:vertical:hover {    "
"    background-color: #B7B7B7;"
"}"
"QScrollBar::add-line:vertical:pressed {    "
"    background-color: #A9A9A9;"
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
        def light_task_show_des_func(btn_info):
            self.task_show_widget = QtWidgets.QDialog()
            self.task_show_widget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.task_show_widget.resize(350, 220)
            self.task_show_widget.setMinimumSize(QtCore.QSize(350, 220))
            self.task_show_widget.setMaximumSize(QtCore.QSize(350, 220))
            self.task_show_widget.setStyleSheet("""
QDialog {
    background-color: #ffffff;
}
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 30px;
}
QPushButton {
    background-color: #e3e5e8;
    border-radius: 5px;
    font-family: 'Roboto Mono', monospace;
    font-size: 20px;
}
QPushButton:hover {
    background-color: #C9C9C9;
}
QPushButton:pressed {
    background-color: #A2A2A2;
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

        self.light_task_scrollArea.setStyleSheet("background-color: #f2f3f5; border-radius: 7px;")
        self.light_task_scrollAreaWidgetContents = QtWidgets.QWidget(self.light_task_scrollArea)
        self.light_task_scrollArea.setWidget(self.light_task_scrollAreaWidgetContents)

        self.light_task_verticalLayout.addWidget(self.light_task_scrollArea)

        MainWindow.setCentralWidget(self.light_task_centralwidget)

        self.light_task_form_layout = QtWidgets.QFormLayout(self.light_task_scrollAreaWidgetContents)
        self.light_task_cond_lst = ["icons\\unchecked.png", "icons\\checked.png"]
        self.light_task_cond = {}
        
        def light_task_create_task_btn_func(btn, i, s):
            self.light_task_cond[btn] = 0
            btn.setFixedSize(25,25)
            btn.setIcon(QtGui.QIcon(self.light_task_cond_lst[self.light_task_cond[btn]]))
            btn.setIconSize(QtCore.QSize(25,25))
            btn.setStyleSheet("""
QPushButton {
    background-color: transparent;
    font-size: 12px;
}
QPushButton:hover {
    background-color: #e3e5e8;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
""")
            def task_switch():
                self.light_task_cond[btn] = not self.light_task_cond[btn]
                btn.setIcon(QtGui.QIcon(self.light_task_cond_lst[self.light_task_cond[btn]]))
            btn.clicked.connect(lambda: task_switch())

        for i,s in enumerate(files):
            light_task_scroll_btn_layout = QtWidgets.QHBoxLayout()
            light_task_checked_btn = QtWidgets.QPushButton()
            light_task_create_task_btn_func(light_task_checked_btn, i, s)
            light_task_scroll_btn_layout.addWidget(light_task_checked_btn)


            light_task_main_btn = QtWidgets.QPushButton(files[i])
            light_task_main_btn.setFixedSize(260,60)
            light_task_main_btn.setStyleSheet(
'''
QPushButton {
    background-color: #e3e5e8;
    font-family: 'Roboto Mono', monospace;
    font-size: 20px;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    border-top-right-radius: 0px;
    border-bottom-right-radius: 0px;
}
QPushButton:hover {
    background-color: #C9C9C9;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
''')
            light_task_main_btn.clicked.connect(lambda checked, btn_text=s:light_task_show_des_func(btn_text))
    
            light_task_edit_btn = QPushButton()   #39DFA2
            light_task_edit_btn.setIcon(QtGui.QIcon("icons\\edit_icon.png"))
            light_task_edit_btn.setIconSize(QtCore.QSize(28, 28))
            light_task_edit_btn.setFixedSize(30,60)  
            light_task_edit_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-radius: 0px;
}
QPushButton:hover {
    background-color: #e3e5e8;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
''')
            light_task_edit_btn.clicked.connect(lambda checked, t="Edit":light_task_task_add_func(t))
            light_task_del_btn = QPushButton()
            light_task_del_btn.setIcon(QtGui.QIcon("icons/del_icon.png"))
            light_task_del_btn.setIconSize(QtCore.QSize(28, 28))
            light_task_del_btn.setFixedSize(30,60)   #39DFA2
            light_task_del_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-top-left-radius: 0;
    border-bottom-left-radius: 00px;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
}
QPushButton:hover {
    background-color: #e3e5e8;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
''')
            light_task_scroll_btn_layout.addWidget(light_task_main_btn)
            light_task_scroll_btn_layout.addWidget(light_task_edit_btn)
            light_task_scroll_btn_layout.addWidget(light_task_del_btn)
            self.light_task_form_layout.addRow(light_task_scroll_btn_layout)

        def combo(index):
            global files
            #i = self.light_task_sort_combo.itemText(index)
            if index == 0:
                files = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
            if index == 1:
                files = ["Alphabet","Alphabet","Alphabet","Alphabet","Alphabet"]
            elif index == 2:
                files = ["Newest","Newest","Newest","Newest","Newest"]

            self.light_task_scrollAreaWidgetContents.deleteLater()
            self.light_task_scrollAreaWidgetContents = QtWidgets.QWidget(self.light_task_scrollArea)
            self.light_task_scrollArea.setWidget(self.light_task_scrollAreaWidgetContents)
            self.light_task_form_layout = QtWidgets.QFormLayout(self.light_task_scrollAreaWidgetContents)

            for i,s in enumerate(files):
                light_task_scroll_btn_layout = QtWidgets.QHBoxLayout()
                light_task_checked_btn = QtWidgets.QPushButton()
                light_task_create_task_btn_func(light_task_checked_btn, i, s)
                light_task_scroll_btn_layout.addWidget(light_task_checked_btn)
                light_task_main_btn = QPushButton(files[i])
                light_task_main_btn.setFixedSize(250,60)
                light_task_main_btn.setStyleSheet(
'''
QPushButton {
    background-color: #e3e5e8;
    font-family: 'Roboto Mono', monospace;
    font-size: 20px;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    border-top-right-radius: 0px;
    border-bottom-right-radius: 0px;
}
QPushButton:hover {
    background-color: #C9C9C9;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
''')
                light_task_main_btn.clicked.connect(lambda checked, btn_text=s:light_task_show_des_func(btn_text))
                light_task_edit_btn = QPushButton()   #39DFA2
                light_task_edit_btn.setIcon(QtGui.QIcon("icons\\edit_icon.png"))
                light_task_edit_btn.setIconSize(QtCore.QSize(28, 28))
                light_task_edit_btn.setFixedSize(30,60)  
                light_task_edit_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-radius: 0px;
}
QPushButton:hover {
    background-color: #e3e5e8;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
''')
                light_task_del_btn = QPushButton()
                light_task_del_btn.setIcon(QtGui.QIcon("icons/del_icon.png"))
                light_task_del_btn.setIconSize(QtCore.QSize(28, 28))
                light_task_del_btn.setFixedSize(30,60)   #39DFA2
                light_task_del_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-top-left-radius: 0;
    border-bottom-left-radius: 00px;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
}
QPushButton:hover {
    background-color: #e3e5e8;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
''')
                light_task_scroll_btn_layout.addWidget(light_task_main_btn)
                light_task_scroll_btn_layout.addWidget(light_task_edit_btn)
                light_task_scroll_btn_layout.addWidget(light_task_del_btn)
                self.light_task_form_layout.addRow(light_task_scroll_btn_layout)
        self.light_task_sort_combo.activated.connect(combo)
        

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
