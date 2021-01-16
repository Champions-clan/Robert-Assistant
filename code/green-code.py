from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton


class Ui_MainWindow(object):
    def __init__(self, MainWindow, files):
        self.files = files
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 500)
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

        self.robert_label = QtWidgets.QLabel("             Robert")
        self.robert_label.setStyleSheet(
'''
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
''')
        self.title_layout = QtWidgets.QHBoxLayout()
        self.title_layout.addWidget(self.robert_label)
        self.verticalLayout.addLayout(self.title_layout)

        self.search_text = QtWidgets.QTextEdit()
        self.search_text.setFixedSize(340,50)
        self.search_text.setPlaceholderText("Search for snippets")
        self.search_text.setStyleSheet(
'''
QTextEdit {
    font-family: 'Cabin', sans-serif;
    font-size: 22px;
    background: #24E29D;
    border-radius: 5px;
}
'''
)

        self.search_btn = QtWidgets.QPushButton()
        self.search_btn.setIcon(QtGui.QIcon("icons\\search_icon"))
        self.search_btn.setIconSize(QtCore.QSize(30, 30))
        self.search_btn.setFixedSize(70,50)
        self.search_btn.setStyleSheet(
'''
QPushButton {
    background-color: #14B57A;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #24E29D;
}
QPushButton:pressed {
    background-color: #1A4E3B;
}
''')
        self.addcode_btn = QtWidgets.QPushButton()
        self.addcode_btn.setIcon(QtGui.QIcon("icons\\add_btn.png"))
        self.addcode_btn.setIconSize(QtCore.QSize(40, 40))
        self.addcode_btn.setFixedSize(70,50)
        self.addcode_btn.setStyleSheet(
'''
QPushButton {
    background-color: #14B57A;
    border-radius: 12px;
}
QPushButton:hover {
    background-color: #24E29D;
}
QPushButton:pressed {
    background-color: #1A4E3B;
}
''')
#-----------------code adding window------------------------------------------------
        def code_text():
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
        self.addcode_btn.clicked.connect(code_text)
        self.top_horizontalLayout = QtWidgets.QHBoxLayout()

        self.horizontalLayout.addWidget(self.search_text)
        self.horizontalLayout.addWidget(self.search_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        combobox_list = ["Most Used","Alphabet","Newest"]

        self.choice_group = QtWidgets.QComboBox()
        #self.choice_group.setFixedSize(200,35)
        self.choice_group.addItems(combobox_list)
        self.choice_group.setStyleSheet(
'''
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
'''
)
        lang_lst = ["All Languages","Python", "Java", "C++", "C#", "Golang", "Javascript", "Typescript",
                    "Html", "CSS", "PHP","Dart", "Scala", "Ruby", "R", "kotlin", "rust", "Lua",
                    "Haskel"]
        self.trans_to_lang_combo = QtWidgets.QComboBox()
        #self.trans_to_lang_combo.setFixedSize(200,35)
        self.trans_to_lang_combo.addItems(lang_lst)
        self.trans_to_lang_combo.setStyleSheet(
'''
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
'''
)
        self.sort_label = QtWidgets.QLabel("Sort by")
        self.sort_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.sort_layout = QtWidgets.QVBoxLayout()
        self.sort_layout.addWidget(self.sort_label)
        self.sort_layout.addWidget(self.choice_group)

        self.lang_label = QtWidgets.QLabel("Choose Language")
        self.lang_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.lang_layout = QtWidgets.QVBoxLayout()
        self.lang_layout.addWidget(self.lang_label)
        self.lang_layout.addWidget(self.trans_to_lang_combo)
        #self.top_horizontalLayout.addStretch(1)
        self.top_horizontalLayout.addLayout(self.lang_layout)
        self.top_horizontalLayout.addLayout(self.sort_layout)
        self.top_horizontalLayout.addWidget(self.addcode_btn)
        

        self.verticalLayout.addLayout(self.top_horizontalLayout)


        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
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
        self.scrollArea.setStyleSheet("background: #2ABF88; border-radius: 7px;")
        self.scrollAreaWidgetContents = QtWidgets.QWidget(self.scrollArea)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)


        def copyed(txt):
            import clipboard
            file = open(f".\\codes\\{txt}.txt", 'r')
            file = file.read()
            clipboard.copy(file)


        for i,s in enumerate(files):
            btn_horizontal = QtWidgets.QHBoxLayout()
            main_btn = QPushButton(files[i])
            main_btn.setFixedSize(300,60)
            main_btn.setStyleSheet(
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
    background-color: #27A97A;
}
QPushButton:pressed {
    background-color: #1A4E3B;
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
    background-color: #27A97A;
}
QPushButton:pressed {
    background-color: #1A4E3B;
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
                main_btn = QPushButton(files[i])
                main_btn.setFixedSize(300,60)
                main_btn.setStyleSheet(
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
    background-color: #27A97A;
}
QPushButton:pressed {
    background-color: #1A4E3B;
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
    background-color: #27A97A;
}
QPushButton:pressed {
    background-color: #1A4E3B;
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
