from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton,QMainWindow, QTextEdit


class Ui_MainWindow(object):
    def __init__(self, MainWindow,files):
        MainWindow.resize(430, 500)
        MainWindow.setMinimumSize(430, 500)
        MainWindow.setMaximumSize(430, 500)
        self.centralwidget = QtWidgets.QWidget()
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setFixedSize(430, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        QtGui.QFontDatabase.addApplicationFont("fonts\\RobotoMono-Regular.ttf")
        QtGui.QFontDatabase.addApplicationFont("fonts\\TitilliumWeb-Bold.ttf")
        QtGui.QFontDatabase.addApplicationFont("fonts\\Cabin-Medium.ttf")
        QtGui.QFontDatabase.addApplicationFont("fonts\\Goldman-Bold.ttf")  
        QtGui.QFontDatabase.addApplicationFont("fonts\\PirataOne-Regular.ttf")
        self.centralwidget.setStyleSheet(
"""
QWidget {
    background-color: #36393f;
}
QPushButton {
    background-color: transparent;
    border-radius: 12.4px;
}
QPushButton:hover {
    background-color: #40444b;
}
QPushButton:pressed {
    background-color: #202225;
}
""")
#-------------------------title area------------------------------------------
        self.title_label = QtWidgets.QLabel("           My Robert")
        self.title_label.setStyleSheet(
"""
QLabel {
    color: #FFFFFF;
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}        
""")    
        self.setting_btn = QtWidgets.QPushButton()
        self.setting_btn.setShortcut("s")
        self.setting_btn.setFixedSize(40, 40)
        self.setting_btn.setIcon(QtGui.QIcon("pic\\setting"))
        self.setting_btn.setIconSize(QtCore.QSize(30, 30))


        self.title_layout = QtWidgets.QHBoxLayout()
        self.title_layout.addWidget(self.title_label)
        self.title_layout.addWidget(self.setting_btn)
        self.verticalLayout.addLayout(self.title_layout)

        self.btn_layout = QtWidgets.QHBoxLayout()

        self.left_scroll_btn = QtWidgets.QPushButton()
        self.left_scroll_btn.setShortcut("Left")
        self.left_scroll_btn.setFixedSize(30,50)
        self.left_scroll_btn.setIcon(QtGui.QIcon("pic\\left_arrow"))
        self.left_scroll_btn.setIconSize(QtCore.QSize(30, 50))

        self.code_btn = QtWidgets.QToolButton()
        self.code_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.code_btn .setFixedSize(330,420)
        self.code_btn.setText("Code Snippets")
        self.code_btn.setIcon(QtGui.QIcon("pic\\copying"))
        
        self.code_btn.setIconSize(QtCore.QSize(300, 400))
        self.code_btn.setStyleSheet("""
QToolButton {
    background-color: #2f3136;
    border-radius: 20px;
    font-family: 'Roboto Mono', monospace;
    font-size: 35px;
}
QToolButton:hover {
    background-color: #40444b;
}
QToolButton:pressed {
    background-color: #202225;
}
""")

        self.trans_btn = QtWidgets.QToolButton()
        self.trans_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.trans_btn .setFixedSize(330,420)
        self.trans_btn.setText("Translation")
        self.trans_btn.setIcon(QtGui.QIcon("pic\\translation"))
        
        self.trans_btn.setIconSize(QtCore.QSize(300, 400))
        self.trans_btn.setStyleSheet("""
QToolButton {
    background-color: #2f3136;
    border-radius: 20px;
    font-family: 'Roboto Mono', monospace;
    font-size: 35px;
}
QToolButton:hover {
    background-color: #40444b;
}
QToolButton:pressed {
    background-color: #202225;
}
""")
    
        self.task_btn = QtWidgets.QToolButton()
        self.task_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.task_btn .setFixedSize(330,420)
        self.task_btn.setText("Task Manager")
        self.task_btn.setIcon(QtGui.QIcon("pic\\task"))
        
        self.task_btn.setIconSize(QtCore.QSize(300, 400))
        self.task_btn.setStyleSheet("""
QToolButton {
    background-color: #2f3136;
    border-radius: 20px;
    font-family: 'Roboto Mono', monospace;
    font-size: 35px;
}
QToolButton:hover {
    background-color: #40444b;
}
QToolButton:pressed {
    background-color: #202225;
}
""")

        self.alarm_btn = QtWidgets.QToolButton()
        self.alarm_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.alarm_btn .setFixedSize(330,420)
        self.alarm_btn.setText("Reminder")
        self.alarm_btn.setIcon(QtGui.QIcon("pic\\alarm"))
        
        self.alarm_btn.setIconSize(QtCore.QSize(300, 400))
        self.alarm_btn.setStyleSheet("""
QToolButton {
    background-color: #2f3136;
    border-radius: 20px;
    font-family: 'Roboto Mono', monospace;
    font-size: 35px;
}
QToolButton:hover {
    background-color: #40444b;
}
QToolButton:pressed {
    background-color: #202225;
}
""")

        self.right_scroll_btn = QtWidgets.QPushButton()
        self.right_scroll_btn.setShortcut("Right")
        self.right_scroll_btn.setFixedSize(30,50)
        self.right_scroll_btn.setIcon(QtGui.QIcon("pic\\right_arrow"))
        self.right_scroll_btn.setIconSize(QtCore.QSize(30, 50))


        self.btn_layout.addWidget(self.left_scroll_btn)
        self.left_scroll_btn.hide()
        self.btn_layout.addWidget(self.code_btn)
        self.btn_layout.addWidget(self.trans_btn)
        self.btn_layout.addWidget(self.task_btn)
        self.btn_layout.addWidget(self.alarm_btn)
        self.i = 0
        self.serv_lst = [self.code_btn, self.trans_btn, self.task_btn, self.alarm_btn]
        for page in self.serv_lst[1:]:
            page.hide()
        self.btn_layout.addWidget(self.right_scroll_btn)
        self.verticalLayout.addLayout(self.btn_layout)

        def switch(sw):
            self.serv_lst[self.i].hide()
            if sw == "right":
                self.i += 1
                self.serv_lst[self.i].show()
                if self.i == 0:
                    self.left_scroll_btn.hide()
                elif self.i == 3:
                    self.right_scroll_btn.hide()
                else:
                    self.left_scroll_btn.show()
                    self.right_scroll_btn.show()

            else:
                self.i -= 1
                self.serv_lst[self.i].show()
                if self.i == 0:
                    self.left_scroll_btn.hide()
                elif self.i == 3:
                    self.right_scroll_btn.hide()
                else:
                    self.left_scroll_btn.show()
                    self.right_scroll_btn.show()

        self.left_scroll_btn.clicked.connect(lambda: switch("left"))
        self.right_scroll_btn.clicked.connect(lambda: switch("right"))
















        self.darkcode_frame = QtWidgets.QFrame(self.centralwidget)
        self.darkcode_verticalLayout = QtWidgets.QVBoxLayout(self.darkcode_frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.robert_label = QtWidgets.QLabel("             Robert")
        self.robert_label.setStyleSheet(
'''
QLabel {
    color: #FFFFFF;
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
''')
        self.title_layout = QtWidgets.QHBoxLayout()
        self.title_layout.addWidget(self.robert_label)
        self.darkcode_verticalLayout.addLayout(self.title_layout)

        self.search_text = QtWidgets.QTextEdit()
        self.search_text.setFixedSize(340,50)
        self.search_text.setPlaceholderText("Search for snippets")
        self.search_text.setStyleSheet(
'''
QTextEdit {
    color: #FFFFFF;
    font-family: 'Cabin', sans-serif;
    font-size: 22px;
    background: #40444b;
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
        self.darkcode_verticalLayout.addLayout(self.horizontalLayout)

        combobox_list = ["Most Used","Alphabet","Newest"]

        self.choice_group = QtWidgets.QComboBox()
        #self.choice_group.setFixedSize(200,35)
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
        lang_lst = ["All Languages","Python", "Java", "C++", "C#", "Golang", "Javascript", "Typescript",
                    "Html", "CSS", "PHP","Dart", "Scala", "Ruby", "R", "kotlin", "rust", "Lua",
                    "Haskel"]
        self.lang_group = QtWidgets.QComboBox()
        #self.lang_group.setFixedSize(200,35)
        self.lang_group.addItems(lang_lst)
        self.lang_group.setStyleSheet(
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

        self.lang_label = QtWidgets.QLabel("Choose Language")
        self.lang_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.lang_layout = QtWidgets.QVBoxLayout()
        self.lang_layout.addWidget(self.lang_label)
        self.lang_layout.addWidget(self.lang_group)
        self.top_horizontalLayout.addLayout(self.lang_layout)
        self.top_horizontalLayout.addLayout(self.sort_layout)
        self.top_horizontalLayout.addWidget(self.addcode_btn)
        

        self.darkcode_verticalLayout.addLayout(self.top_horizontalLayout)


        self.scrollArea = QtWidgets.QScrollArea(self.darkcode_frame)
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

        self.darkcode_verticalLayout.addWidget(self.scrollArea)

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

        self.darkcode_frame.hide()
        def change_to(from_, to_):
            from_.hide()
            to_.show()
        self.code_btn.clicked.connect(lambda: change_to(self.main_frame, self.darkcode_frame))


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

files = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow,files)
    MainWindow.show()
    sys.exit(app.exec_())
