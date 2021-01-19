from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.resize(430, 500)
        MainWindow.setMinimumSize(430, 500)
        MainWindow.setMaximumSize(430, 500)
        self.light_trans_centralwidget = QtWidgets.QWidget(MainWindow)
        self.light_trans_vertical_layout = QtWidgets.QVBoxLayout(self.light_trans_centralwidget)
        QtGui.QFontDatabase.addApplicationFont("fonts\\RobotoMono-Regular.ttf")
        QtGui.QFontDatabase.addApplicationFont("fonts\\TitilliumWeb-Bold.ttf")
        QtGui.QFontDatabase.addApplicationFont("fonts\\Cabin-Medium.ttf")
        QtGui.QFontDatabase.addApplicationFont("fonts\\Goldman-Bold.ttf")  
        QtGui.QFontDatabase.addApplicationFont("fonts\\PirataOne-Regular.ttf")
        MainWindow.setStyleSheet(
"""
QMainWindow {
    background-color: #ffffff;
}
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
        self.light_trans_home_btn = QtWidgets.QPushButton()
        self.light_trans_home_btn.setIcon(QtGui.QIcon("pic\\home"))
        self.light_trans_home_btn.setIconSize(QtCore.QSize(25, 25))
        self.light_trans_home_btn.setFixedSize(40,40)
        self.light_trans_home_btn.setStyleSheet(
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

        self.light_trans_title_label = QtWidgets.QLabel("    Robert Translation")
        self.light_trans_title_label.setStyleSheet("""
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
""")
        self.light_trans_title_layout = QtWidgets.QHBoxLayout()
        self.light_trans_title_layout.addWidget(self.light_trans_home_btn)
        self.light_trans_title_layout.addWidget(self.light_trans_title_label)
        self.light_trans_vertical_layout.addLayout(self.light_trans_title_layout)
        self.light_trans_vertical_layout.addStretch(1)

        self.light_trans_lang_lst = ["English", "German", "Arabic", "Spanish", "French"]
        self.light_trans_from_lang_combo = QtWidgets.QComboBox()
        self.light_trans_from_lang_combo.addItems(self.light_trans_lang_lst)
        
        self.light_trans_to_lang_lst = ["French", "German", "Arabic", "Spanish", "English"]
        self.light_trans_to_lang_combo = QtWidgets.QComboBox()
        self.light_trans_to_lang_combo.addItems(self.light_trans_to_lang_lst)

        self.light_trans_from_label = QtWidgets.QLabel("From_")
        self.light_trans_from_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.light_trans_from_layout = QtWidgets.QVBoxLayout()
        self.light_trans_from_layout.addWidget(self.light_trans_from_label)
        self.light_trans_from_layout.addWidget(self.light_trans_from_lang_combo)

        self.light_trans_to_label = QtWidgets.QLabel("To_")
        self.light_trans_to_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.light_trans_to_layout = QtWidgets.QVBoxLayout()
        self.light_trans_to_layout.addWidget(self.light_trans_to_label)
        self.light_trans_to_layout.addWidget(self.light_trans_to_lang_combo)  

        self.light_trans_lang_layout = QtWidgets.QHBoxLayout()
        self.light_trans_lang_layout.addLayout(self.light_trans_from_layout)
        self.light_trans_lang_layout.addLayout(self.light_trans_to_layout)
        self.light_trans_vertical_layout.addLayout(self.light_trans_lang_layout)
        self.light_trans_vertical_layout.addStretch(15)

        self.light_trans_from_textedit = QtWidgets.QTextEdit()
        self.light_trans_from_textedit.setFixedSize(410,120)
        self.light_trans_from_textedit.setPlaceholderText("How are you")
        self.light_trans_from_textedit.setStyleSheet(
'''
QTextEdit {
    font-family: 'Cabin', sans-serif;
    font-size: 20px;
    background: #ebedef;
    border-radius: 5px;
}
'''
)
        self.light_trans_translate_btn = QtWidgets.QPushButton()
        self.light_trans_translate_btn.setIcon(QtGui.QIcon("pic\\translate"))
        self.light_trans_translate_btn.setIconSize(QtCore.QSize(30, 30))
        #self.light_trans_translate_btn.setText("Translate")
        self.light_trans_translate_btn.setFixedSize(120,40)
        self.light_trans_translate_btn.setStyleSheet(
'''
QPushButton {
    background-color: #e3e5e8;
    border-radius: 3px;
    font-family: 'Cabin', sans-serif;
    font-size: 20px;
}
QPushButton:hover {
    background-color: #C9C9C9;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
''')
        self.light_trans_translate_layout = QtWidgets.QHBoxLayout()
        self.light_trans_translate_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.light_trans_translate_layout.addWidget(self.light_trans_translate_btn)

        self.light_trans_to_textedit = QtWidgets.QTextEdit()
        self.light_trans_to_textedit.setFixedSize(410,180)
        self.light_trans_to_textedit.setPlaceholderText("Comment allez-vous")
        self.light_trans_to_textedit.setReadOnly(True)
        self.light_trans_to_textedit.setStyleSheet(
'''
QTextEdit {
    font-family: 'Cabin', sans-serif;
    font-size: 20px;
    background: #ebedea;
    border-radius: 5px;
}
'''
)
        self.light_trans_vertical_layout.addWidget(self.light_trans_from_textedit)
        self.light_trans_vertical_layout.addLayout(self.light_trans_translate_layout)
        self.light_trans_vertical_layout.addWidget(self.light_trans_to_textedit)
        self.light_trans_vertical_layout.addStretch(200)


        MainWindow.setCentralWidget(self.light_trans_centralwidget)
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