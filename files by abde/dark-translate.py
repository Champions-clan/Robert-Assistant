from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.resize(430, 500)
        MainWindow.setMinimumSize(430, 500)
        MainWindow.setMaximumSize(430, 500)
        self.dark_trans_centralwidget = QtWidgets.QWidget(MainWindow)
        self.dark_trans_vertical_layout = QtWidgets.QVBoxLayout(self.dark_trans_centralwidget)
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
        self.dark_trans_home_btn = QtWidgets.QPushButton()
        self.dark_trans_home_btn.setIcon(QtGui.QIcon("pic\\home"))
        self.dark_trans_home_btn.setIconSize(QtCore.QSize(25, 25))
        self.dark_trans_home_btn.setFixedSize(40,40)
        self.dark_trans_home_btn.setStyleSheet(
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

        self.dark_trans_title_label = QtWidgets.QLabel("    Robert Translation")
        self.dark_trans_title_label.setStyleSheet("""
QLabel {
    color: #FFFFFF;
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
""")
        self.dark_trans_title_layout = QtWidgets.QHBoxLayout()
        self.dark_trans_title_layout.addWidget(self.dark_trans_home_btn)
        self.dark_trans_title_layout.addWidget(self.dark_trans_title_label)
        self.dark_trans_vertical_layout.addLayout(self.dark_trans_title_layout)
        self.dark_trans_vertical_layout.addStretch(1)

        self.dark_trans_lang_lst = ["English", "German", "Arabic", "Spanish", "French"]
        self.dark_trans_from_lang_combo = QtWidgets.QComboBox()
        self.dark_trans_from_lang_combo.addItems(self.dark_trans_lang_lst)
        
        self.dark_trans_to_lang_lst = ["French", "German", "Arabic", "Spanish", "English"]
        self.dark_trans_to_lang_combo = QtWidgets.QComboBox()
        self.dark_trans_to_lang_combo.addItems(self.dark_trans_to_lang_lst)
        
        self.dark_trans_from_label = QtWidgets.QLabel("From_")
        self.dark_trans_from_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.dark_trans_from_layout = QtWidgets.QVBoxLayout()
        self.dark_trans_from_layout.addWidget(self.dark_trans_from_label)
        self.dark_trans_from_layout.addWidget(self.dark_trans_from_lang_combo)

        self.dark_trans_to_label = QtWidgets.QLabel("To_")
        self.dark_trans_to_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.dark_trans_to_layout = QtWidgets.QVBoxLayout()
        self.dark_trans_to_layout.addWidget(self.dark_trans_to_label)
        self.dark_trans_to_layout.addWidget(self.dark_trans_to_lang_combo)  

        self.dark_trans_lang_layout = QtWidgets.QHBoxLayout()
        self.dark_trans_lang_layout.addLayout(self.dark_trans_from_layout)
        self.dark_trans_lang_layout.addLayout(self.dark_trans_to_layout)
        self.dark_trans_vertical_layout.addLayout(self.dark_trans_lang_layout)
        self.dark_trans_vertical_layout.addStretch(15)

        self.dark_trans_from_textedit = QtWidgets.QTextEdit()
        self.dark_trans_from_textedit.setFixedSize(410,120)
        self.dark_trans_from_textedit.setPlaceholderText("How are you")
        self.dark_trans_from_textedit.setStyleSheet(
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
        self.dark_trans_translate_btn = QtWidgets.QPushButton()
        self.dark_trans_translate_btn.setIcon(QtGui.QIcon("pic\\translate"))
        self.dark_trans_translate_btn.setIconSize(QtCore.QSize(30, 30))
        #self.dark_trans_translate_btn.setText("Translate")
        self.dark_trans_translate_btn.setFixedSize(120,40)
        self.dark_trans_translate_btn.setStyleSheet(
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
        self.dark_trans_translate_layout = QtWidgets.QHBoxLayout()
        self.dark_trans_translate_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.dark_trans_translate_layout.addWidget(self.dark_trans_translate_btn)

        self.dark_trans_to_textedit = QtWidgets.QTextEdit()
        self.dark_trans_to_textedit.setFixedSize(410,180)
        self.dark_trans_to_textedit.setPlaceholderText("Comment allez-vous")
        self.dark_trans_to_textedit.setReadOnly(True)
        self.dark_trans_to_textedit.setStyleSheet(
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
        self.dark_trans_vertical_layout.addWidget(self.dark_trans_from_textedit)
        self.dark_trans_vertical_layout.addLayout(self.dark_trans_translate_layout)
        self.dark_trans_vertical_layout.addWidget(self.dark_trans_to_textedit)
        self.dark_trans_vertical_layout.addStretch(200)


        MainWindow.setCentralWidget(self.dark_trans_centralwidget)
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