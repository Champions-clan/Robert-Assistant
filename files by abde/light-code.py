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

        self.light_code_centralwidget = QtWidgets.QWidget(MainWindow)
        self.light_code_main_layout = QtWidgets.QVBoxLayout(self.light_code_centralwidget)
        self.light_code_search_layout = QtWidgets.QHBoxLayout()

        self.light_code_title_label = QtWidgets.QLabel("    Robert codes")
        self.light_code_title_label.setStyleSheet(
'''
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
''')
        self.light_code_title_layout = QtWidgets.QHBoxLayout()
        self.light_code_home_btn = QtWidgets.QPushButton()
        self.light_code_home_btn.setIcon(QtGui.QIcon("pic\\home"))
        self.light_code_home_btn.setIconSize(QtCore.QSize(25, 25))
        self.light_code_home_btn.setFixedSize(40,40)
        self.light_code_home_btn.setStyleSheet(
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
        self.light_code_title_layout.addWidget(self.light_code_home_btn)
        self.light_code_title_layout.addWidget(self.light_code_title_label)
        self.light_code_main_layout.addLayout(self.light_code_title_layout)

        self.light_code_search_textarea = QtWidgets.QTextEdit()
        self.light_code_search_textarea.setFixedSize(340,50)
        self.light_code_search_textarea.setPlaceholderText("Search for snippets")
        self.light_code_search_textarea.setStyleSheet(
'''
QTextEdit {
    font-family: 'Cabin', sans-serif;
    font-size: 22px;
    background: #ebedef;
    border-radius: 5px;
}
'''
)

        self.light_code_search_btn = QtWidgets.QPushButton()
        self.light_code_search_btn.setIcon(QtGui.QIcon("icons\\search_icon"))
        self.light_code_search_btn.setIconSize(QtCore.QSize(30, 30))
        self.light_code_search_btn.setFixedSize(70,50)
        self.light_code_search_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #ebedef;
}
QPushButton:pressed {
    background-color: #e3e5e8;
}
''')
        self.light_code_addcode_btn = QtWidgets.QPushButton()
        self.light_code_addcode_btn.setIcon(QtGui.QIcon("icons\\add_btn.png"))
        self.light_code_addcode_btn.setIconSize(QtCore.QSize(40, 40))
        self.light_code_addcode_btn.setFixedSize(70,50)
        self.light_code_addcode_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #ebedef;
}
QPushButton:pressed {
    background-color: #e3e5e8;
}
''')
#-----------------code adding window------------------------------------------------
        def light_code_dialog_popup_func():
            import os.path
            user = os.path.expanduser('~')
            files_list = ['py', 'c++']
            files_list_updated = [f"*.{i}" for i in files_list]
            code_file = " ;; ".join(files_list_updated)

            self.code_widget = QtWidgets.QWidget()
            self.file_get = QtWidgets.QFileDialog.getOpenFileName(self.code_widget, 'Open File', user , code_file)
            
            self.file_selected = self.file_get[0]
            if self.file_selected == '':
                pass
            else:
                self.files_set_DialogWindow = QtWidgets.QDialog()
                self.files_set_DialogWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
                self.files_set_DialogWindow.resize(330, 200)
                self.files_set_DialogWindow.setMinimumSize(QtCore.QSize(330, 200))
                self.files_set_DialogWindow.setMaximumSize(QtCore.QSize(350, 200))
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
""")
                self.dialog_ok_btn = QtWidgets.QPushButton(self.files_set_DialogWindow)
                self.dialog_ok_btn.setGeometry(QtCore.QRect(10, 140, 151, 51))
                self.dialog_ok_btn.setText("Add")
                self.dialog_cancel_btn = QtWidgets.QPushButton(self.files_set_DialogWindow)
                self.dialog_cancel_btn.setGeometry(QtCore.QRect(170, 140, 151, 51))
                self.dialog_cancel_btn.setText("Cancel")
                self.dialog_textEdit = QtWidgets.QTextEdit(self.files_set_DialogWindow)
                self.dialog_textEdit.setGeometry(QtCore.QRect(20, 80, 291, 41))
                self.dialog_textEdit.setPlaceholderText("Type Name of your Code")
                self.dialog_label = QtWidgets.QLabel(self.files_set_DialogWindow)
                self.dialog_label.setGeometry(QtCore.QRect(60, 20, 231, 41))
                self.dialog_label.setText("Name your Code")

                import sys
                sys.exit(self.files_set_DialogWindow.exec_())

#-----------------end of code adding--------------------------------------

        self.light_code_addcode_btn.clicked.connect(light_code_dialog_popup_func)

        self.light_code_search_layout.addWidget(self.light_code_search_textarea)
        self.light_code_search_layout.addWidget(self.light_code_search_btn)
        self.light_code_main_layout.addLayout(self.light_code_search_layout)

        combobox_list = ["Most Used","Alphabet","Newest"]

        self.light_code_choice_group = QtWidgets.QComboBox()
        #self.light_code_choice_group.setFixedSize(200,35)
        self.light_code_choice_group.addItems(combobox_list)
        self.light_code_choice_group.setStyleSheet(
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
        lang_lst = ["All Languages","Python", "Java", "C++", "C#", "Golang", "Javascript", "Typescript",
                    "Html", "CSS", "PHP","Dart", "Scala", "Ruby", "R", "kotlin", "rust", "Lua",
                    "Haskel"]
        self.light_code_lang_choice = QtWidgets.QComboBox()
        #self.light_code_lang_choice.setFixedSize(200,35)
        self.light_code_lang_choice.addItems(lang_lst)
        self.light_code_lang_choice.setStyleSheet(
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
        self.light_code_sort_label = QtWidgets.QLabel("Sort by")
        self.light_code_sort_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.light_code_sort_layout = QtWidgets.QVBoxLayout()
        self.light_code_sort_layout.addWidget(self.light_code_sort_label)
        self.light_code_sort_layout.addWidget(self.light_code_choice_group)

        self.light_code_lang_label = QtWidgets.QLabel("Choose Language")
        self.light_code_lang_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.light_code_lang_layout = QtWidgets.QVBoxLayout()
        self.light_code_lang_layout.addWidget(self.light_code_lang_label)
        self.light_code_lang_layout.addWidget(self.light_code_lang_choice)
        self.light_code_choice_layout = QtWidgets.QHBoxLayout()
        self.light_code_choice_layout.addLayout(self.light_code_lang_layout)
        self.light_code_choice_layout.addLayout(self.light_code_sort_layout)
        self.light_code_choice_layout.addWidget(self.light_code_addcode_btn)
        

        self.light_code_main_layout.addLayout(self.light_code_choice_layout)


        self.light_code_scrollArea = QtWidgets.QScrollArea(self.light_code_centralwidget)
        self.light_code_scrollArea.setWidgetResizable(True)
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
        self.light_code_scrollArea.setStyleSheet("background: #f2f3f5; border-radius: 7px;")
        self.light_code_scrollAreaWidgetContents = QtWidgets.QWidget(self.light_code_scrollArea)
        self.light_code_scrollArea.setWidget(self.light_code_scrollAreaWidgetContents)

        self.light_code_main_layout.addWidget(self.light_code_scrollArea)

        MainWindow.setCentralWidget(self.light_code_centralwidget)

        self.light_code_form_layout = QtWidgets.QFormLayout(self.light_code_scrollAreaWidgetContents)


        def copyed(txt):
            import clipboard
            file = open(f".\\codes\\{txt}.txt", 'r')
            file = file.read()
            clipboard.copy(file)


        for i,s in enumerate(files):
            light_code_scroll_btns_layout = QtWidgets.QHBoxLayout()
            light_code_scroll_main_btn = QPushButton(files[i])
            light_code_scroll_main_btn.setFixedSize(300,60)
            light_code_scroll_main_btn.setStyleSheet(
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
            light_code_scroll_edit_btn = QPushButton()   #39DFA2
            light_code_scroll_edit_btn.setIcon(QtGui.QIcon("icons\\edit_icon.png"))
            light_code_scroll_edit_btn.setIconSize(QtCore.QSize(28, 28))
            light_code_scroll_edit_btn.setFixedSize(30,60)  
            light_code_scroll_edit_btn.setStyleSheet(
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
            light_code_scroll_del_btn = QPushButton()
            light_code_scroll_del_btn.setIcon(QtGui.QIcon("icons/del_icon.png"))
            light_code_scroll_del_btn.setIconSize(QtCore.QSize(28, 28))
            light_code_scroll_del_btn.setFixedSize(30,60)   #39DFA2
            light_code_scroll_del_btn.setStyleSheet(
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
            light_code_scroll_btns_layout.addWidget(light_code_scroll_main_btn)
            light_code_scroll_btns_layout.addWidget(light_code_scroll_edit_btn)
            light_code_scroll_btns_layout.addWidget(light_code_scroll_del_btn)
            self.light_code_form_layout.addRow(light_code_scroll_btns_layout)

        def combo(index):
            global files
            print(self.light_code_choice_group.itemText(index))
            #i = self.light_code_choice_group.itemText(index)
            if index == 0:
                files = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
            if index == 1:
                files = ["Alphabet","Alphabet","Alphabet","Alphabet","Alphabet"]
            elif index == 2:
                files = ["Newest","Newest","Newest","Newest","Newest"]

            self.light_code_scrollAreaWidgetContents.deleteLater()
            self.light_code_scrollAreaWidgetContents = QtWidgets.QWidget(self.light_code_scrollArea)
            self.light_code_scrollArea.setWidget(self.light_code_scrollAreaWidgetContents)
            self.light_code_form_layout = QtWidgets.QFormLayout(self.light_code_scrollAreaWidgetContents)

            for i,s in enumerate(files):
                light_code_scroll_btns_layout = QtWidgets.QHBoxLayout()
                light_code_scroll_main_btn = QPushButton(files[i])
                light_code_scroll_main_btn.setFixedSize(300,60)
                light_code_scroll_main_btn.setStyleSheet(
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
                light_code_scroll_edit_btn = QPushButton()   #39DFA2
                light_code_scroll_edit_btn.setIcon(QtGui.QIcon("icons\\edit_icon.png"))
                light_code_scroll_edit_btn.setIconSize(QtCore.QSize(28, 28))
                light_code_scroll_edit_btn.setFixedSize(30,60)  
                light_code_scroll_edit_btn.setStyleSheet(
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
                light_code_scroll_del_btn = QPushButton()
                light_code_scroll_del_btn.setIcon(QtGui.QIcon("icons/del_icon.png"))
                light_code_scroll_del_btn.setIconSize(QtCore.QSize(28, 28))
                light_code_scroll_del_btn.setFixedSize(30,60)   #39DFA2
                light_code_scroll_del_btn.setStyleSheet(
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
                light_code_scroll_btns_layout.addWidget(light_code_scroll_main_btn)
                light_code_scroll_btns_layout.addWidget(light_code_scroll_edit_btn)
                light_code_scroll_btns_layout.addWidget(light_code_scroll_del_btn)
                self.light_code_form_layout.addRow(light_code_scroll_btns_layout)
        self.light_code_choice_group.activated.connect(combo)
        

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
