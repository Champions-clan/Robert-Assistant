from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.resize(430, 500)
        MainWindow.setMinimumSize(430, 500)
        MainWindow.setMaximumSize(430, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        QtGui.QFontDatabase.addApplicationFont("fonts\\RobotoMono-Regular.ttf")
        QtGui.QFontDatabase.addApplicationFont("fonts\\TitilliumWeb-Bold.ttf")
        QtGui.QFontDatabase.addApplicationFont("fonts\\Cabin-Medium.ttf")
        QtGui.QFontDatabase.addApplicationFont("fonts\\Goldman-Bold.ttf")  
        QtGui.QFontDatabase.addApplicationFont("fonts\\PirataOne-Regular.ttf")
        MainWindow.setStyleSheet(
"""
QMainWindow {
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

        self.trans_title = QtWidgets.QLabel("    Robert Translation")
        self.trans_title.setStyleSheet("""
QLabel {
    color: #FFFFFF;
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
""")
        self.trans_title_layout = QtWidgets.QHBoxLayout()
        self.trans_title_layout.addWidget(self.trans_home_btn)
        self.trans_title_layout.addWidget(self.trans_title)
        self.verticalLayout.addLayout(self.trans_title_layout)
        self.verticalLayout.addStretch(1)

        self.trans_lang_lst = ["English", "German", "Arabic", "Spanish", "French"]
        self.trans_from_lang_combo = QtWidgets.QComboBox()
        self.trans_from_lang_combo.addItems(self.trans_lang_lst)
        self.trans_from_lang_combo.setStyleSheet(
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
        self.trans_to_lang_lst = ["French", "German", "Arabic", "Spanish", "English"]
        self.trans_to_lang_combo = QtWidgets.QComboBox()
        self.trans_to_lang_combo.addItems(self.trans_to_lang_lst)
        self.trans_to_lang_combo.setStyleSheet(
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
        self.trans_from_label = QtWidgets.QLabel("From_")
        self.trans_from_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.trans_from_layout = QtWidgets.QVBoxLayout()
        self.trans_from_layout.addWidget(self.trans_from_label)
        self.trans_from_layout.addWidget(self.trans_from_lang_combo)

        self.trans_to_label = QtWidgets.QLabel("To_")
        self.trans_to_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.trans_to_layout = QtWidgets.QVBoxLayout()
        self.trans_to_layout.addWidget(self.trans_to_label)
        self.trans_to_layout.addWidget(self.trans_to_lang_combo)  

        self.trans_lang_layout = QtWidgets.QHBoxLayout()
        self.trans_lang_layout.addLayout(self.trans_from_layout)
        self.trans_lang_layout.addLayout(self.trans_to_layout)
        self.verticalLayout.addLayout(self.trans_lang_layout)
        self.verticalLayout.addStretch(15)

        self.trans_from_textedit = QtWidgets.QTextEdit()
        self.trans_from_textedit.setFixedSize(410,120)
        self.trans_from_textedit.setPlaceholderText("How are you")
        self.trans_from_textedit.setStyleSheet(
'''
QTextEdit {
    color: #FFFFFF;
    font-family: 'Cabin', sans-serif;
    font-size: 15px;
    background: #40444b;
    border-radius: 5px;
}
'''
)
        self.trans_translate_btn = QtWidgets.QPushButton()
        self.trans_translate_btn.setIcon(QtGui.QIcon("pic\\translate"))
        self.trans_translate_btn.setIconSize(QtCore.QSize(30, 30))
        #self.trans_translate_btn.setText("Translate")
        self.trans_translate_btn.setFixedSize(120,40)
        self.trans_translate_btn.setStyleSheet(
'''
QPushButton {
    background-color: #2f3136;
    border-radius: 3px;
    font-family: 'Cabin', sans-serif;
    font-size: 20px;
}
QPushButton:hover {
    background-color: #40444b;
}
QPushButton:pressed {
    background-color: #202225;
}
''')
        self.trans_translate_layout = QtWidgets.QHBoxLayout()
        self.trans_translate_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.trans_translate_layout.addWidget(self.trans_translate_btn)

        self.trans_to_textedit = QtWidgets.QTextEdit()
        self.trans_to_textedit.setFixedSize(410,180)
        self.trans_to_textedit.setPlaceholderText("Comment allez-vous")
        self.trans_to_textedit.setReadOnly(True)
        self.trans_to_textedit.setStyleSheet(
'''
QTextEdit {
    color: #FFFFFF;
    font-family: 'Cabin', sans-serif;
    font-size: 20px;
    background-color: #35363F;
    border-radius: 5px;
}
'''
)
        self.verticalLayout.addWidget(self.trans_from_textedit)
        self.verticalLayout.addLayout(self.trans_translate_layout)
        self.verticalLayout.addWidget(self.trans_to_textedit)
        self.verticalLayout.addStretch(200)


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())