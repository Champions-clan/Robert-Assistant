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
    background-color: #ffffff;
}
QPushButton {
    background-color: transparent;
    border-radius: 12.4px;
}
QPushButton:hover {
    background-color: #ebedef;
}
QPushButton:pressed {
    background-color: #e3e5e8;
}
QToolButton {
    background-color: #f2f3f5;
    border-radius: 20px;
    font-family: 'Roboto Mono', monospace;
    font-size: 35px;
}
QToolButton:hover {
    background-color: #e3e5e8;
}
QToolButton:pressed {
    background-color: #C9C9C9;
}
""")
        self.light_main_central_widget= QtWidgets.QWidget(MainWindow)
        self.light_main_main_layout = QtWidgets.QVBoxLayout(self.light_main_central_widget)
#-------------------------title area------------------------------------------
        self.light_main_title_label = QtWidgets.QLabel("           My Robert")
        self.light_main_title_label.setStyleSheet(
"""
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}        
""")    
        self.light_main_setting_btn = QtWidgets.QPushButton()
        self.light_main_setting_btn.setShortcut("s")
        self.light_main_setting_btn.setFixedSize(40, 40)
        self.light_main_setting_btn.setIcon(QtGui.QIcon("pic\\setting"))
        self.light_main_setting_btn.setIconSize(QtCore.QSize(30, 30))


        self.light_main_title_layout = QtWidgets.QHBoxLayout()
        self.light_main_title_layout.addWidget(self.light_main_title_label)
        self.light_main_title_layout.addWidget(self.light_main_setting_btn)
        self.light_main_main_layout.addLayout(self.light_main_title_layout)

        self.light_main_horizontal_layout = QtWidgets.QHBoxLayout()

        self.light_main_left_scroll_btn = QtWidgets.QPushButton()
        self.light_main_left_scroll_btn.setShortcut("Left")
        self.light_main_left_scroll_btn.setFixedSize(30,50)
        self.light_main_left_scroll_btn.setIcon(QtGui.QIcon("pic\\left_arrow"))
        self.light_main_left_scroll_btn.setIconSize(QtCore.QSize(30, 50))

        self.light_main_code_page = QtWidgets.QToolButton()
        self.light_main_code_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.light_main_code_page .setFixedSize(330,420)
        self.light_main_code_page.setText("Code Snippets")
        self.light_main_code_page.setIcon(QtGui.QIcon("pic\\copying"))
        
        self.light_main_code_page.setIconSize(QtCore.QSize(300, 400))
        

        self.light_main_trans_page = QtWidgets.QToolButton()
        self.light_main_trans_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.light_main_trans_page .setFixedSize(330,420)
        self.light_main_trans_page.setText("Translation")
        self.light_main_trans_page.setIcon(QtGui.QIcon("pic\\translation"))
        
        self.light_main_trans_page.setIconSize(QtCore.QSize(300, 400))
    
        self.light_main_task_page = QtWidgets.QToolButton()
        self.light_main_task_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.light_main_task_page .setFixedSize(330,420)
        self.light_main_task_page.setText("Task Manager")
        self.light_main_task_page.setIcon(QtGui.QIcon("pic\\task"))
        
        self.light_main_task_page.setIconSize(QtCore.QSize(300, 400))

        self.light_main_alarm_page = QtWidgets.QToolButton()
        self.light_main_alarm_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.light_main_alarm_page .setFixedSize(330,420)
        self.light_main_alarm_page.setText("Reminder")
        self.light_main_alarm_page.setIcon(QtGui.QIcon("pic\\alarm"))
        
        self.light_main_alarm_page.setIconSize(QtCore.QSize(300, 400))

        self.light_main_right_scroll_btn = QtWidgets.QPushButton()
        self.light_main_right_scroll_btn.setShortcut("Right")
        self.light_main_right_scroll_btn.setFixedSize(30,50)
        self.light_main_right_scroll_btn.setIcon(QtGui.QIcon("pic\\right_arrow"))
        self.light_main_right_scroll_btn.setIconSize(QtCore.QSize(30, 50))


        self.light_main_horizontal_layout.addWidget(self.light_main_left_scroll_btn)
        self.light_main_left_scroll_btn.hide()
        self.light_main_horizontal_layout.addWidget(self.light_main_code_page)
        self.light_main_horizontal_layout.addWidget(self.light_main_trans_page)
        self.light_main_horizontal_layout.addWidget(self.light_main_task_page)
        self.light_main_horizontal_layout.addWidget(self.light_main_alarm_page)
        self.i = 0
        self.light_main_serv_lst = [self.light_main_code_page, self.light_main_trans_page, self.light_main_task_page, self.light_main_alarm_page]
        for page in self.light_main_serv_lst[1:]:
            page.hide()
        self.light_main_horizontal_layout.addWidget(self.light_main_right_scroll_btn)
        self.light_main_main_layout.addLayout(self.light_main_horizontal_layout)

        def dark_main_switch_func(sw):
            self.light_main_serv_lst[self.i].hide()
            if sw == "right":
                self.i += 1
                self.light_main_serv_lst[self.i].show()
                if self.i == 0:
                    self.light_main_left_scroll_btn.hide()
                elif self.i == 3:
                    self.light_main_right_scroll_btn.hide()
                else:
                    self.light_main_left_scroll_btn.show()
                    self.light_main_right_scroll_btn.show()

            else:
                self.i -= 1
                self.light_main_serv_lst[self.i].show()
                if self.i == 0:
                    self.light_main_left_scroll_btn.hide()
                elif self.i == 3:
                    self.light_main_right_scroll_btn.hide()
                else:
                    self.light_main_left_scroll_btn.show()
                    self.light_main_right_scroll_btn.show()

        self.light_main_left_scroll_btn.clicked.connect(lambda: dark_main_switch_func("left"))
        self.light_main_right_scroll_btn.clicked.connect(lambda: dark_main_switch_func("right"))

        MainWindow.setCentralWidget(self.light_main_central_widget)
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
