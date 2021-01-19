from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.resize(430, 500)
        MainWindow.setMinimumSize(430, 500)
        MainWindow.setMaximumSize(430, 500)
        self.green_trans_centralwidget = QtWidgets.QWidget(MainWindow)
        self.green_trans_vertical_layout = QtWidgets.QVBoxLayout(self.green_trans_centralwidget)
        QtGui.QFontDatabase.addApplicationFont("fonts\\RobotoMono-Regular.ttf")
        QtGui.QFontDatabase.addApplicationFont("fonts\\TitilliumWeb-Bold.ttf")
        QtGui.QFontDatabase.addApplicationFont("fonts\\Cabin-Medium.ttf")
        QtGui.QFontDatabase.addApplicationFont("fonts\\Goldman-Bold.ttf")  
        QtGui.QFontDatabase.addApplicationFont("fonts\\PirataOne-Regular.ttf")
        MainWindow.setStyleSheet(
"""
QMainWindow {
    background-color: #14B57A;
}
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
        self.green_trans_home_btn = QtWidgets.QPushButton()
        self.green_trans_home_btn.setIcon(QtGui.QIcon("pic\\home"))
        self.green_trans_home_btn.setIconSize(QtCore.QSize(25, 25))
        self.green_trans_home_btn.setFixedSize(40,40)
        self.green_trans_home_btn.setStyleSheet(
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

        self.green_trans_title_label = QtWidgets.QLabel("    Robert Translation")
        self.green_trans_title_label.setStyleSheet("""
QLabel {
    color: #FFFFFF;
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
""")
        self.green_trans_title_layout = QtWidgets.QHBoxLayout()
        self.green_trans_title_layout.addWidget(self.green_trans_home_btn)
        self.green_trans_title_layout.addWidget(self.green_trans_title_label)
        self.green_trans_vertical_layout.addLayout(self.green_trans_title_layout)
        self.green_trans_vertical_layout.addStretch(1)

        self.green_trans_lang_lst = ["English", "German", "Arabic", "Spanish", "French"]
        self.green_trans_from_lang_combo = QtWidgets.QComboBox()
        self.green_trans_from_lang_combo.addItems(self.green_trans_lang_lst)
        
        self.green_trans_to_lang_lst = ["French", "German", "Arabic", "Spanish", "English"]
        self.green_trans_to_lang_combo = QtWidgets.QComboBox()
        self.green_trans_to_lang_combo.addItems(self.green_trans_to_lang_lst)
    
        self.green_trans_from_label = QtWidgets.QLabel("From_")
        self.green_trans_from_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.green_trans_from_layout = QtWidgets.QVBoxLayout()
        self.green_trans_from_layout.addWidget(self.green_trans_from_label)
        self.green_trans_from_layout.addWidget(self.green_trans_from_lang_combo)

        self.green_trans_to_label = QtWidgets.QLabel("To_")
        self.green_trans_to_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.green_trans_to_layout = QtWidgets.QVBoxLayout()
        self.green_trans_to_layout.addWidget(self.green_trans_to_label)
        self.green_trans_to_layout.addWidget(self.green_trans_to_lang_combo)  

        self.green_trans_lang_layout = QtWidgets.QHBoxLayout()
        self.green_trans_lang_layout.addLayout(self.green_trans_from_layout)
        self.green_trans_lang_layout.addLayout(self.green_trans_to_layout)
        self.green_trans_vertical_layout.addLayout(self.green_trans_lang_layout)
        self.green_trans_vertical_layout.addStretch(15)

        self.green_trans_from_textedit = QtWidgets.QTextEdit()
        self.green_trans_from_textedit.setFixedSize(410,120)
        self.green_trans_from_textedit.setPlaceholderText("How are you")
        self.green_trans_from_textedit.setStyleSheet(
'''
QTextEdit {
    font-family: 'Cabin', sans-serif;
    font-size: 22px;
    background: #24E29D;
    border-radius: 5px;
}
'''
)
        self.green_trans_translate_btn = QtWidgets.QPushButton()
        self.green_trans_translate_btn.setIcon(QtGui.QIcon("pic\\translate"))
        self.green_trans_translate_btn.setIconSize(QtCore.QSize(30, 30))
        #self.green_trans_translate_btn.setText("Translate")
        self.green_trans_translate_btn.setFixedSize(120,40)
        self.green_trans_translate_btn.setStyleSheet(
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
    background-color: #1F986C;
}
QPushButton:pressed {
    background-color: #1A6C4E;
}
''')
        self.green_trans_translate_layout = QtWidgets.QHBoxLayout()
        self.green_trans_translate_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.green_trans_translate_layout.addWidget(self.green_trans_translate_btn)

        self.green_trans_to_textedit = QtWidgets.QTextEdit()
        self.green_trans_to_textedit.setFixedSize(410,180)
        self.green_trans_to_textedit.setPlaceholderText("Comment allez-vous")
        self.green_trans_to_textedit.setReadOnly(True)
        self.green_trans_to_textedit.setStyleSheet(
'''
QTextEdit {
    font-family: 'Cabin', sans-serif;
    font-size: 22px;
    background: #24E293;
    border-radius: 5px;
}
'''
)
        self.green_trans_vertical_layout.addWidget(self.green_trans_from_textedit)
        self.green_trans_vertical_layout.addLayout(self.green_trans_translate_layout)
        self.green_trans_vertical_layout.addWidget(self.green_trans_to_textedit)
        self.green_trans_vertical_layout.addStretch(200)


        MainWindow.setCentralWidget(self.green_trans_centralwidget)
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