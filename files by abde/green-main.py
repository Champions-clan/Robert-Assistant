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
QToolButton {
    background-color: #2ABF88;
    border-radius: 20px;
    font-family: 'Roboto Mono', monospace;
    font-size: 35px;
}
QToolButton:hover {
    background-color: #39DFA2;
}
QToolButton:pressed {
    background-color: #3ABA8B;
}
""")
        self.green_main_central_widget= QtWidgets.QWidget(MainWindow)
        self.green_main_main_layout = QtWidgets.QVBoxLayout(self.green_main_central_widget)
#-------------------------title area------------------------------------------
        self.green_main_title_label = QtWidgets.QLabel("           My Robert")
        self.green_main_title_label.setStyleSheet(
"""
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}       
""")    
        self.green_main_setting_btn = QtWidgets.QPushButton()
        self.green_main_setting_btn.setShortcut("s")
        self.green_main_setting_btn.setFixedSize(40, 40)
        self.green_main_setting_btn.setIcon(QtGui.QIcon("pic\\setting"))
        self.green_main_setting_btn.setIconSize(QtCore.QSize(30, 30))


        self.green_main_title_layout = QtWidgets.QHBoxLayout()
        self.green_main_title_layout.addWidget(self.green_main_title_label)
        self.green_main_title_layout.addWidget(self.green_main_setting_btn)
        self.green_main_main_layout.addLayout(self.green_main_title_layout)

        self.green_main_horizontal_layout = QtWidgets.QHBoxLayout()

        self.green_main_left_scroll_btn = QtWidgets.QPushButton()
        self.green_main_left_scroll_btn.setShortcut("Left")
        self.green_main_left_scroll_btn.setFixedSize(30,50)
        self.green_main_left_scroll_btn.setIcon(QtGui.QIcon("pic\\left_arrow"))
        self.green_main_left_scroll_btn.setIconSize(QtCore.QSize(30, 50))

        self.green_main_code_page = QtWidgets.QToolButton()
        self.green_main_code_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.green_main_code_page .setFixedSize(330,420)
        self.green_main_code_page.setText("Code Snippets")
        self.green_main_code_page.setIcon(QtGui.QIcon("pic\\copying"))
        
        self.green_main_code_page.setIconSize(QtCore.QSize(300, 400))
        

        self.green_main_trans_page = QtWidgets.QToolButton()
        self.green_main_trans_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.green_main_trans_page .setFixedSize(330,420)
        self.green_main_trans_page.setText("Translation")
        self.green_main_trans_page.setIcon(QtGui.QIcon("pic\\translation"))
        
        self.green_main_trans_page.setIconSize(QtCore.QSize(300, 400))
        
    
        self.green_main_task_page = QtWidgets.QToolButton()
        self.green_main_task_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.green_main_task_page .setFixedSize(330,420)
        self.green_main_task_page.setText("Task Manager")
        self.green_main_task_page.setIcon(QtGui.QIcon("pic\\task"))
        
        self.green_main_task_page.setIconSize(QtCore.QSize(300, 400))
        

        self.green_main_alarm_page = QtWidgets.QToolButton()
        self.green_main_alarm_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.green_main_alarm_page .setFixedSize(330,420)
        self.green_main_alarm_page.setText("Reminder")
        self.green_main_alarm_page.setIcon(QtGui.QIcon("pic\\alarm"))
        
        self.green_main_alarm_page.setIconSize(QtCore.QSize(300, 400))

        self.green_main_right_scroll_btn = QtWidgets.QPushButton()
        self.green_main_right_scroll_btn.setShortcut("Right")
        self.green_main_right_scroll_btn.setFixedSize(30,50)
        self.green_main_right_scroll_btn.setIcon(QtGui.QIcon("pic\\right_arrow"))
        self.green_main_right_scroll_btn.setIconSize(QtCore.QSize(30, 50))


        self.green_main_horizontal_layout.addWidget(self.green_main_left_scroll_btn)
        self.green_main_left_scroll_btn.hide()
        self.green_main_horizontal_layout.addWidget(self.green_main_code_page)
        self.green_main_horizontal_layout.addWidget(self.green_main_trans_page)
        self.green_main_horizontal_layout.addWidget(self.green_main_task_page)
        self.green_main_horizontal_layout.addWidget(self.green_main_alarm_page)
        self.i = 0
        self.green_main_serv_lst = [self.green_main_code_page, self.green_main_trans_page, self.green_main_task_page, self.green_main_alarm_page]
        for page in self.green_main_serv_lst[1:]:
            page.hide()
        self.green_main_horizontal_layout.addWidget(self.green_main_right_scroll_btn)
        self.green_main_main_layout.addLayout(self.green_main_horizontal_layout)

        def dark_main_switch_func(sw):
            self.green_main_serv_lst[self.i].hide()
            if sw == "right":
                self.i += 1
                self.green_main_serv_lst[self.i].show()
                if self.i == 0:
                    self.green_main_left_scroll_btn.hide()
                elif self.i == 3:
                    self.green_main_right_scroll_btn.hide()
                else:
                    self.green_main_left_scroll_btn.show()
                    self.green_main_right_scroll_btn.show()

            else:
                self.i -= 1
                self.green_main_serv_lst[self.i].show()
                if self.i == 0:
                    self.green_main_left_scroll_btn.hide()
                elif self.i == 3:
                    self.green_main_right_scroll_btn.hide()
                else:
                    self.green_main_left_scroll_btn.show()
                    self.green_main_right_scroll_btn.show()

        self.green_main_left_scroll_btn.clicked.connect(lambda: dark_main_switch_func("left"))
        self.green_main_right_scroll_btn.clicked.connect(lambda: dark_main_switch_func("right"))

        MainWindow.setCentralWidget(self.green_main_central_widget)
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
