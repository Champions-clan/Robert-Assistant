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
