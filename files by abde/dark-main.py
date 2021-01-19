from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.resize(430, 500)
        MainWindow.setMinimumSize(430, 500)
        MainWindow.setMaximumSize(430, 500)
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
        self.dark_main_central_widget= QtWidgets.QWidget(MainWindow)
        self.dark_main_main_layout = QtWidgets.QVBoxLayout(self.dark_main_central_widget)
#-------------------------title area------------------------------------------
        self.dark_main_title_label = QtWidgets.QLabel("           My Robert")
        self.dark_main_title_label.setStyleSheet(
"""
QLabel {
    color: #FFFFFF;
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}        
""")    
        self.dark_main_setting_btn = QtWidgets.QPushButton()
        self.dark_main_setting_btn.setShortcut("s")
        self.dark_main_setting_btn.setFixedSize(40, 40)
        self.dark_main_setting_btn.setIcon(QtGui.QIcon("pic\\setting"))
        self.dark_main_setting_btn.setIconSize(QtCore.QSize(30, 30))


        self.dark_main_title_layout = QtWidgets.QHBoxLayout()
        self.dark_main_title_layout.addWidget(self.dark_main_title_label)
        self.dark_main_title_layout.addWidget(self.dark_main_setting_btn)
        self.dark_main_main_layout.addLayout(self.dark_main_title_layout)

        self.dark_main_horizontal_layout = QtWidgets.QHBoxLayout()

        self.dark_main_left_scroll_btn = QtWidgets.QPushButton()
        self.dark_main_left_scroll_btn.setShortcut("Left")
        self.dark_main_left_scroll_btn.setFixedSize(30,50)
        self.dark_main_left_scroll_btn.setIcon(QtGui.QIcon("pic\\left_arrow"))
        self.dark_main_left_scroll_btn.setIconSize(QtCore.QSize(30, 50))

        self.dark_main_code_page = QtWidgets.QToolButton()
        self.dark_main_code_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.dark_main_code_page .setFixedSize(330,420)
        self.dark_main_code_page.setText("Code Snippets")
        self.dark_main_code_page.setIcon(QtGui.QIcon("pic\\copying"))
        
        self.dark_main_code_page.setIconSize(QtCore.QSize(300, 400))
        

        self.dark_main_trans_page = QtWidgets.QToolButton()
        self.dark_main_trans_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.dark_main_trans_page .setFixedSize(330,420)
        self.dark_main_trans_page.setText("Translation")
        self.dark_main_trans_page.setIcon(QtGui.QIcon("pic\\translation"))
        
        self.dark_main_trans_page.setIconSize(QtCore.QSize(300, 400))
        
    
        self.dark_main_task_page = QtWidgets.QToolButton()
        self.dark_main_task_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.dark_main_task_page .setFixedSize(330,420)
        self.dark_main_task_page.setText("Task Manager")
        self.dark_main_task_page.setIcon(QtGui.QIcon("pic\\task"))
        
        self.dark_main_task_page.setIconSize(QtCore.QSize(300, 400))
        

        self.dark_main_alarm_page = QtWidgets.QToolButton()
        self.dark_main_alarm_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.dark_main_alarm_page .setFixedSize(330,420)
        self.dark_main_alarm_page.setText("Reminder")
        self.dark_main_alarm_page.setIcon(QtGui.QIcon("pic\\alarm"))
        
        self.dark_main_alarm_page.setIconSize(QtCore.QSize(300, 400))

        self.dark_main_right_scroll_btn = QtWidgets.QPushButton()
        self.dark_main_right_scroll_btn.setShortcut("Right")
        self.dark_main_right_scroll_btn.setFixedSize(30,50)
        self.dark_main_right_scroll_btn.setIcon(QtGui.QIcon("pic\\right_arrow"))
        self.dark_main_right_scroll_btn.setIconSize(QtCore.QSize(30, 50))


        self.dark_main_horizontal_layout.addWidget(self.dark_main_left_scroll_btn)
        self.dark_main_left_scroll_btn.hide()
        self.dark_main_horizontal_layout.addWidget(self.dark_main_code_page)
        self.dark_main_horizontal_layout.addWidget(self.dark_main_trans_page)
        self.dark_main_horizontal_layout.addWidget(self.dark_main_task_page)
        self.dark_main_horizontal_layout.addWidget(self.dark_main_alarm_page)
        self.i = 0
        self.dark_main_serv_lst = [self.dark_main_code_page, self.dark_main_trans_page, self.dark_main_task_page, self.dark_main_alarm_page]
        for page in self.dark_main_serv_lst[1:]:
            page.hide()
        self.dark_main_horizontal_layout.addWidget(self.dark_main_right_scroll_btn)
        self.dark_main_main_layout.addLayout(self.dark_main_horizontal_layout)

        def dark_main_switch_func(sw):
            self.dark_main_serv_lst[self.i].hide()
            if sw == "right":
                self.i += 1
                self.dark_main_serv_lst[self.i].show()
                if self.i == 0:
                    self.dark_main_left_scroll_btn.hide()
                elif self.i == 3:
                    self.dark_main_right_scroll_btn.hide()
                else:
                    self.dark_main_left_scroll_btn.show()
                    self.dark_main_right_scroll_btn.show()

            else:
                self.i -= 1
                self.dark_main_serv_lst[self.i].show()
                if self.i == 0:
                    self.dark_main_left_scroll_btn.hide()
                elif self.i == 3:
                    self.dark_main_right_scroll_btn.hide()
                else:
                    self.dark_main_left_scroll_btn.show()
                    self.dark_main_right_scroll_btn.show()

        self.dark_main_left_scroll_btn.clicked.connect(lambda: dark_main_switch_func("left"))
        self.dark_main_right_scroll_btn.clicked.connect(lambda: dark_main_switch_func("right"))

        MainWindow.setCentralWidget(self.dark_main_central_widget)
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
