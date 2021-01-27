from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton,QMainWindow, QTextEdit
from googletrans import Translator
from db_worker import Snippets, TaskManager


class Ui_MainWindow(object):
    def __init__(self, MainWindow, c_th, files):
#<<<<<<<<<<<<<<<Dark Main Window
        self.c_th = c_th
        self.i = 0
        MainWindow.resize(430, 500)
        MainWindow.setMinimumSize(430, 500)
        MainWindow.setMaximumSize(430, 500)
        QtGui.QFontDatabase.addApplicationFont(r".\Asserts\fonts\RobotoMono-Regular.ttf")
        QtGui.QFontDatabase.addApplicationFont(r".\Asserts\fonts\TitilliumWeb-Bold.ttf")
        QtGui.QFontDatabase.addApplicationFont(r".\Asserts\fonts\Cabin-Medium.ttf")
        QtGui.QFontDatabase.addApplicationFont(r".\Asserts\fonts\Goldman-Bold.ttf")
        QtGui.QFontDatabase.addApplicationFont(r".\Asserts\fonts\PirataOne-Regular.ttf")

        self.dark_main_central_widget= QtWidgets.QWidget(MainWindow)
        self.dark_main_central_widget.setFixedSize(430, 500)
        self.dark_main_central_widget.setStyleSheet("""
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
        self.dark_main_setting_btn.setIcon(QtGui.QIcon(r".\Asserts\images\setting"))
        self.dark_main_setting_btn.setIconSize(QtCore.QSize(30, 30))


        self.dark_main_title_layout = QtWidgets.QHBoxLayout()
        self.dark_main_title_layout.addWidget(self.dark_main_title_label)
        self.dark_main_title_layout.addWidget(self.dark_main_setting_btn)
        self.dark_main_main_layout.addLayout(self.dark_main_title_layout)

        self.dark_main_horizontal_layout = QtWidgets.QHBoxLayout()

        self.dark_main_left_scroll_btn = QtWidgets.QPushButton()
        self.dark_main_left_scroll_btn.setShortcut("Left")
        self.dark_main_left_scroll_btn.setFixedSize(30,50)
        self.dark_main_left_scroll_btn.setIcon(QtGui.QIcon(r".\Asserts\images\left_arrow"))
        self.dark_main_left_scroll_btn.setIconSize(QtCore.QSize(30, 50))

        self.dark_main_code_page = QtWidgets.QToolButton()
        self.dark_main_code_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.dark_main_code_page .setFixedSize(330,420)
        self.dark_main_code_page.setText("Code Snippets")
        self.dark_main_code_page.setIcon(QtGui.QIcon(r".\Asserts\images\copying"))

        self.dark_main_code_page.setIconSize(QtCore.QSize(300, 400))


        self.dark_main_trans_page = QtWidgets.QToolButton()
        self.dark_main_trans_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.dark_main_trans_page .setFixedSize(330,420)
        self.dark_main_trans_page.setText("Translation")
        self.dark_main_trans_page.setIcon(QtGui.QIcon(r".\Asserts\images\translation"))

        self.dark_main_trans_page.setIconSize(QtCore.QSize(300, 400))


        self.dark_main_task_page = QtWidgets.QToolButton()
        self.dark_main_task_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.dark_main_task_page .setFixedSize(330,420)
        self.dark_main_task_page.setText("Task Manager")
        self.dark_main_task_page.setIcon(QtGui.QIcon(r".\Asserts\images\task"))

        self.dark_main_task_page.setIconSize(QtCore.QSize(300, 400))


        self.dark_main_alarm_page = QtWidgets.QToolButton()
        self.dark_main_alarm_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.dark_main_alarm_page .setFixedSize(330,420)
        self.dark_main_alarm_page.setText("Reminder")
        self.dark_main_alarm_page.setIcon(QtGui.QIcon(r".\Asserts\images\alarm"))

        self.dark_main_alarm_page.setIconSize(QtCore.QSize(300, 400))

        self.dark_main_right_scroll_btn = QtWidgets.QPushButton()
        self.dark_main_right_scroll_btn.setShortcut("Right")
        self.dark_main_right_scroll_btn.setFixedSize(30,50)
        self.dark_main_right_scroll_btn.setIcon(QtGui.QIcon(r".\Asserts\images\right_arrow"))
        self.dark_main_right_scroll_btn.setIconSize(QtCore.QSize(30, 50))


        self.dark_main_horizontal_layout.addWidget(self.dark_main_left_scroll_btn)
        self.dark_main_left_scroll_btn.hide()
        self.dark_main_horizontal_layout.addWidget(self.dark_main_code_page)
        self.dark_main_horizontal_layout.addWidget(self.dark_main_trans_page)
        self.dark_main_horizontal_layout.addWidget(self.dark_main_task_page)
        self.dark_main_horizontal_layout.addWidget(self.dark_main_alarm_page)

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

#<<<<<<<<<<<<<<<Light Main Window---------------------------------------------------------------------
        self.light_main_central_widget= QtWidgets.QWidget(MainWindow)
        self.light_main_central_widget.setFixedSize(430, 500)
        self.light_main_central_widget.setStyleSheet(
"""
QWidget {
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
        self.light_main_setting_btn.setIcon(QtGui.QIcon(r".\Asserts\images\setting"))
        self.light_main_setting_btn.setIconSize(QtCore.QSize(30, 30))


        self.light_main_title_layout = QtWidgets.QHBoxLayout()
        self.light_main_title_layout.addWidget(self.light_main_title_label)
        self.light_main_title_layout.addWidget(self.light_main_setting_btn)
        self.light_main_main_layout.addLayout(self.light_main_title_layout)

        self.light_main_horizontal_layout = QtWidgets.QHBoxLayout()

        self.light_main_left_scroll_btn = QtWidgets.QPushButton()
        self.light_main_left_scroll_btn.setShortcut("Left")
        self.light_main_left_scroll_btn.setFixedSize(30,50)
        self.light_main_left_scroll_btn.setIcon(QtGui.QIcon(r".\Asserts\images\left_arrow"))
        self.light_main_left_scroll_btn.setIconSize(QtCore.QSize(30, 50))

        self.light_main_code_page = QtWidgets.QToolButton()
        self.light_main_code_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.light_main_code_page .setFixedSize(330,420)
        self.light_main_code_page.setText("Code Snippets")
        self.light_main_code_page.setIcon(QtGui.QIcon(r".\Asserts\images\copying"))

        self.light_main_code_page.setIconSize(QtCore.QSize(300, 400))


        self.light_main_trans_page = QtWidgets.QToolButton()
        self.light_main_trans_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.light_main_trans_page .setFixedSize(330,420)
        self.light_main_trans_page.setText("Translation")
        self.light_main_trans_page.setIcon(QtGui.QIcon(r".\Asserts\images\translation"))

        self.light_main_trans_page.setIconSize(QtCore.QSize(300, 400))

        self.light_main_task_page = QtWidgets.QToolButton()
        self.light_main_task_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.light_main_task_page .setFixedSize(330,420)
        self.light_main_task_page.setText("Task Manager")
        self.light_main_task_page.setIcon(QtGui.QIcon(r".\Asserts\images\task"))

        self.light_main_task_page.setIconSize(QtCore.QSize(300, 400))

        self.light_main_alarm_page = QtWidgets.QToolButton()
        self.light_main_alarm_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.light_main_alarm_page .setFixedSize(330,420)
        self.light_main_alarm_page.setText("Reminder")
        self.light_main_alarm_page.setIcon(QtGui.QIcon(r".\Asserts\images\alarm"))

        self.light_main_alarm_page.setIconSize(QtCore.QSize(300, 400))

        self.light_main_right_scroll_btn = QtWidgets.QPushButton()
        self.light_main_right_scroll_btn.setShortcut("Right")
        self.light_main_right_scroll_btn.setFixedSize(30,50)
        self.light_main_right_scroll_btn.setIcon(QtGui.QIcon(r".\Asserts\images\right_arrow"))
        self.light_main_right_scroll_btn.setIconSize(QtCore.QSize(30, 50))


        self.light_main_horizontal_layout.addWidget(self.light_main_left_scroll_btn)
        self.light_main_left_scroll_btn.hide()
        self.light_main_horizontal_layout.addWidget(self.light_main_code_page)
        self.light_main_horizontal_layout.addWidget(self.light_main_trans_page)
        self.light_main_horizontal_layout.addWidget(self.light_main_task_page)
        self.light_main_horizontal_layout.addWidget(self.light_main_alarm_page)
        self.light_main_serv_lst = [self.light_main_code_page, self.light_main_trans_page, self.light_main_task_page, self.light_main_alarm_page]
        for page in self.light_main_serv_lst[1:]:
            page.hide()
        self.light_main_horizontal_layout.addWidget(self.light_main_right_scroll_btn)
        self.light_main_main_layout.addLayout(self.light_main_horizontal_layout)

        def light_main_switch_func(sw):
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

        self.light_main_left_scroll_btn.clicked.connect(lambda: light_main_switch_func("left"))
        self.light_main_right_scroll_btn.clicked.connect(lambda: light_main_switch_func("right"))
#<<<<<<<<<<<<<<<Green Main Window
        self.green_main_central_widget = QtWidgets.QWidget(MainWindow)
        self.green_main_central_widget.setFixedSize(430,500)
        self.green_main_central_widget.setStyleSheet(
"""
QWidget {
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
        self.green_main_setting_btn.setIcon(QtGui.QIcon(r".\Asserts\images\setting"))
        self.green_main_setting_btn.setIconSize(QtCore.QSize(30, 30))


        self.green_main_title_layout = QtWidgets.QHBoxLayout()
        self.green_main_title_layout.addWidget(self.green_main_title_label)
        self.green_main_title_layout.addWidget(self.green_main_setting_btn)
        self.green_main_main_layout.addLayout(self.green_main_title_layout)

        self.green_main_horizontal_layout = QtWidgets.QHBoxLayout()

        self.green_main_left_scroll_btn = QtWidgets.QPushButton()
        self.green_main_left_scroll_btn.setShortcut("Left")
        self.green_main_left_scroll_btn.setFixedSize(30,50)
        self.green_main_left_scroll_btn.setIcon(QtGui.QIcon(r".\Asserts\images\left_arrow"))
        self.green_main_left_scroll_btn.setIconSize(QtCore.QSize(30, 50))

        self.green_main_code_page = QtWidgets.QToolButton()
        self.green_main_code_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.green_main_code_page .setFixedSize(330,420)
        self.green_main_code_page.setText("Code Snippets")
        self.green_main_code_page.setIcon(QtGui.QIcon(r".\Asserts\images\copying"))

        self.green_main_code_page.setIconSize(QtCore.QSize(300, 400))


        self.green_main_trans_page = QtWidgets.QToolButton()
        self.green_main_trans_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.green_main_trans_page .setFixedSize(330,420)
        self.green_main_trans_page.setText("Translation")
        self.green_main_trans_page.setIcon(QtGui.QIcon(r".\Asserts\images\translation"))

        self.green_main_trans_page.setIconSize(QtCore.QSize(300, 400))


        self.green_main_task_page = QtWidgets.QToolButton()
        self.green_main_task_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.green_main_task_page .setFixedSize(330,420)
        self.green_main_task_page.setText("Task Manager")
        self.green_main_task_page.setIcon(QtGui.QIcon(r".\Asserts\images\task"))

        self.green_main_task_page.setIconSize(QtCore.QSize(300, 400))


        self.green_main_alarm_page = QtWidgets.QToolButton()
        self.green_main_alarm_page.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.green_main_alarm_page .setFixedSize(330,420)
        self.green_main_alarm_page.setText("Reminder")
        self.green_main_alarm_page.setIcon(QtGui.QIcon(r".\Asserts\images\alarm"))

        self.green_main_alarm_page.setIconSize(QtCore.QSize(300, 400))

        self.green_main_right_scroll_btn = QtWidgets.QPushButton()
        self.green_main_right_scroll_btn.setShortcut("Right")
        self.green_main_right_scroll_btn.setFixedSize(30,50)
        self.green_main_right_scroll_btn.setIcon(QtGui.QIcon(r".\Asserts\images\right_arrow"))
        self.green_main_right_scroll_btn.setIconSize(QtCore.QSize(30, 50))


        self.green_main_horizontal_layout.addWidget(self.green_main_left_scroll_btn)
        self.green_main_left_scroll_btn.hide()
        self.green_main_horizontal_layout.addWidget(self.green_main_code_page)
        self.green_main_horizontal_layout.addWidget(self.green_main_trans_page)
        self.green_main_horizontal_layout.addWidget(self.green_main_task_page)
        self.green_main_horizontal_layout.addWidget(self.green_main_alarm_page)
        self.green_main_serv_lst = [self.green_main_code_page, self.green_main_trans_page, self.green_main_task_page, self.green_main_alarm_page]
        for page in self.green_main_serv_lst[1:]:
            page.hide()
        self.green_main_horizontal_layout.addWidget(self.green_main_right_scroll_btn)
        self.green_main_main_layout.addLayout(self.green_main_horizontal_layout)

        def green_main_switch_func(sw):
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

        self.green_main_left_scroll_btn.clicked.connect(lambda: green_main_switch_func("left"))
        self.green_main_right_scroll_btn.clicked.connect(lambda: green_main_switch_func("right"))
#<<<<<<<<<<<<<<<Dark setting Window
        self.dark_setting_centralwidget = QtWidgets.QWidget(MainWindow)
        self.dark_setting_centralwidget.setFixedSize(430,500)
        self.dark_setting_centralwidget.setStyleSheet(
"""
QWidget {
    background-color: #36393F;
}
QLabel {
    color: #FFFFFF;
    font-family: 'Roboto Mono', monospace;
    font-size: 18px;
}
QFrame {
    background-color: #2f3136;
    border-radius: 7px;
}
"""
)
        self.dark_setting_verticalLayout = QtWidgets.QVBoxLayout(self.dark_setting_centralwidget)
        self.dark_setting_title_layout = QtWidgets.QHBoxLayout()

        self.dark_setting_home_btn = QtWidgets.QPushButton()
        self.dark_setting_home_btn.setIcon(QtGui.QIcon(r".\Asserts\images\home"))
        self.dark_setting_home_btn.setIconSize(QtCore.QSize(25, 25))
        self.dark_setting_home_btn.setFixedSize(40,40)
        self.dark_setting_home_btn.setStyleSheet(
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

        self.dark_setting_title_label = QtWidgets.QLabel("           Setting")
        self.dark_setting_title_label.setStyleSheet(
"""
QLabel {
    background-color: transparent;
    color: #FFFFFF;
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
"""
        )
        self.dark_setting_title_layout = QtWidgets.QHBoxLayout()
        self.dark_setting_title_layout.addWidget(self.dark_setting_home_btn)
        self.dark_setting_title_layout.addWidget(self.dark_setting_title_label)


        self.dark_setting_verticalLayout.addLayout(self.dark_setting_title_layout)

        self.dark_setting_apperance_frame = QtWidgets.QFrame()
        self.dark_setting_apperance_frame.setFixedSize(400, 180)
        self.dark_setting_apperance_layout = QtWidgets.QVBoxLayout(self.dark_setting_apperance_frame)

        self.dark_setting_apperance_label = QtWidgets.QLabel("        Apperance")
        self.dark_setting_apperance_label.setStyleSheet(
"""
QLabel {
    color: #FFFFFF;
    font-family: 'Titillium Web', sans-serif;
    font-size: 30px;
}
"""
)

        self.dark_setting_apperance_layout.addWidget(self.dark_setting_apperance_label)
        self.dark_setting_apperance_layout.addStretch(1)

        self.dark_setting_dark_theme_btn = QtWidgets.QRadioButton()
        self.dark_setting_dark_theme_btn.setFixedSize(25,25)
        self.dark_setting_light_theme_btn = QtWidgets.QRadioButton()
        self.dark_setting_light_theme_btn.setFixedSize(25,25)
        self.dark_setting_green_theme_btn = QtWidgets.QRadioButton()
        self.dark_setting_green_theme_btn.setFixedSize(25,25)

        self.dark_setting_dark_theme_label = QtWidgets.QLabel("Dark Mode")
        self.dark_setting_light_theme_label = QtWidgets.QLabel("Light Mode")
        self.dark_setting_green_theme_label = QtWidgets.QLabel("Green Mode")

        self.dark_setting_dark_theme_layout = QtWidgets.QHBoxLayout()
        self.dark_setting_light_theme_layout = QtWidgets.QHBoxLayout()
        self.dark_setting_green_theme_layout = QtWidgets.QHBoxLayout()

        self.dark_setting_dark_theme_layout.addWidget(self.dark_setting_dark_theme_btn)
        self.dark_setting_dark_theme_layout.addWidget(self.dark_setting_dark_theme_label)
        self.dark_setting_light_theme_layout.addWidget(self.dark_setting_light_theme_btn)
        self.dark_setting_light_theme_layout.addWidget(self.dark_setting_light_theme_label)
        self.dark_setting_green_theme_layout.addWidget(self.dark_setting_green_theme_btn)
        self.dark_setting_green_theme_layout.addWidget(self.dark_setting_green_theme_label)

        self.dark_setting_apperance_layout.addLayout(self.dark_setting_dark_theme_layout)
        self.dark_setting_apperance_layout.addLayout(self.dark_setting_light_theme_layout)
        self.dark_setting_apperance_layout.addLayout(self.dark_setting_green_theme_layout)
        self.dark_setting_apperance_layout.addStretch(1)

        self.dark_setting_verticalLayout.addSpacing(12)
        self.dark_setting_verticalLayout.addWidget(self.dark_setting_apperance_frame)
        self.dark_setting_verticalLayout.addStretch(1)

        self.dark_setting_keyboard_frame = QtWidgets.QFrame()
        self.dark_setting_keyboard_frame.setFixedSize(400, 120)
        self.dark_setting_keyboard_layout = QtWidgets.QVBoxLayout(self.dark_setting_keyboard_frame)

        self.dark_setting_keyboard_label = QtWidgets.QLabel()
        self.dark_setting_keyboard_label.setText("         Keyboard Shortcut")
        self.dark_setting_keyboard_label.setStyleSheet(
'''
QLabel {
    color: #FFFFFF;
    font-family: 'Titillium Web', sans-serif;
    font-size: 27px;
}
''')
        self.dark_setting_keyboard_layout.addWidget(self.dark_setting_keyboard_label)
        self.dark_setting_keyboard_shortcut_label = QtWidgets.QLabel("Home Page  :-  Shift + Tab + 6\nRobert Listener  :-  Shift + Tab + 7")
        self.dark_setting_keyboard_layout.addWidget(self.dark_setting_keyboard_shortcut_label)

        self.dark_setting_verticalLayout.addWidget(self.dark_setting_keyboard_frame)
        self.dark_setting_verticalLayout.addStretch(5)
#<<<<<<<<<<<<<<<Light setting Window
        self.light_setting_centralwidget = QtWidgets.QWidget(MainWindow)
        self.light_setting_centralwidget.setFixedSize(430,500)
        self.light_setting_centralwidget.setStyleSheet(
"""
QWidget {
    background-color: #ffffff;
}
QLabel {
    font-family: 'Roboto Mono', monospace;
    font-size: 18px;
}
QFrame {
    background-color: #ebedef;
    border-radius: 7px;
}
"""
)
        self.light_setting_verticalLayout = QtWidgets.QVBoxLayout(self.light_setting_centralwidget)
        self.light_setting_title_layout = QtWidgets.QHBoxLayout()

        self.light_setting_home_btn = QtWidgets.QPushButton()
        self.light_setting_home_btn.setIcon(QtGui.QIcon(r".\Asserts\images\home"))
        self.light_setting_home_btn.setIconSize(QtCore.QSize(25, 25))
        self.light_setting_home_btn.setFixedSize(40,40)
        self.light_setting_home_btn.setStyleSheet(
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

        self.light_setting_title_label = QtWidgets.QLabel("           Setting")
        self.light_setting_title_label.setStyleSheet(
"""
QLabel {
    background-color: transparent;
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
"""
        )
        self.light_setting_title_layout = QtWidgets.QHBoxLayout()
        self.light_setting_title_layout.addWidget(self.light_setting_home_btn)
        self.light_setting_title_layout.addWidget(self.light_setting_title_label)


        self.light_setting_verticalLayout.addLayout(self.light_setting_title_layout)

        self.light_setting_apperance_frame = QtWidgets.QFrame()
        self.light_setting_apperance_frame.setFixedSize(400, 180)
        self.light_setting_apperance_layout = QtWidgets.QVBoxLayout(self.light_setting_apperance_frame)

        self.light_setting_apperance_label = QtWidgets.QLabel("        Apperance")
        self.light_setting_apperance_label.setStyleSheet(
"""
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 30px;
}
"""
)

        self.light_setting_apperance_layout.addWidget(self.light_setting_apperance_label)
        self.light_setting_apperance_layout.addStretch(1)

        self.light_setting_dark_theme_btn = QtWidgets.QRadioButton()
        self.light_setting_dark_theme_btn.setFixedSize(25,25)
        self.light_setting_light_theme_btn = QtWidgets.QRadioButton()
        self.light_setting_light_theme_btn.setFixedSize(25,25)
        self.light_setting_green_theme_btn = QtWidgets.QRadioButton()
        self.light_setting_green_theme_btn.setFixedSize(25,25)

        self.light_setting_dark_theme_label = QtWidgets.QLabel("Dark Mode")
        self.light_setting_light_theme_label = QtWidgets.QLabel("Light Mode")
        self.light_setting_green_theme_label = QtWidgets.QLabel("Green Mode")

        self.light_setting_dark_theme_layout = QtWidgets.QHBoxLayout()
        self.light_setting_light_theme_layout = QtWidgets.QHBoxLayout()
        self.light_setting_green_theme_layout = QtWidgets.QHBoxLayout()

        self.light_setting_dark_theme_layout.addWidget(self.light_setting_dark_theme_btn)
        self.light_setting_dark_theme_layout.addWidget(self.light_setting_dark_theme_label)
        self.light_setting_light_theme_layout.addWidget(self.light_setting_light_theme_btn)
        self.light_setting_light_theme_layout.addWidget(self.light_setting_light_theme_label)
        self.light_setting_green_theme_layout.addWidget(self.light_setting_green_theme_btn)
        self.light_setting_green_theme_layout.addWidget(self.light_setting_green_theme_label)

        self.light_setting_apperance_layout.addLayout(self.light_setting_dark_theme_layout)
        self.light_setting_apperance_layout.addLayout(self.light_setting_light_theme_layout)
        self.light_setting_apperance_layout.addLayout(self.light_setting_green_theme_layout)
        self.light_setting_apperance_layout.addStretch(1)

        self.light_setting_verticalLayout.addSpacing(12)
        self.light_setting_verticalLayout.addWidget(self.light_setting_apperance_frame)
        self.light_setting_verticalLayout.addStretch(1)

        self.light_setting_keyboard_frame = QtWidgets.QFrame()
        self.light_setting_keyboard_frame.setFixedSize(400, 120)
        self.light_setting_keyboard_layout = QtWidgets.QVBoxLayout(self.light_setting_keyboard_frame)

        self.light_setting_keyboard_label = QtWidgets.QLabel()
        self.light_setting_keyboard_label.setText("         Keyboard Shortcut")
        self.light_setting_keyboard_label.setStyleSheet(
'''
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 27px;
}
''')
        self.light_setting_keyboard_layout.addWidget(self.light_setting_keyboard_label)
        self.light_setting_keyboard_shortcut_label = QtWidgets.QLabel("Home Page  :-  Shift + Tab + 6\nRobert Listener  :-  Shift + Tab + 7")

        self.light_setting_keyboard_layout.addWidget(self.light_setting_keyboard_shortcut_label)
        self.light_setting_verticalLayout.addWidget(self.light_setting_keyboard_frame)
        self.light_setting_verticalLayout.addStretch(5)

#<<<<<<<<<<<<<<<Green setting Window
        self.green_setting_centralwidget = QtWidgets.QWidget(MainWindow)
        self.green_setting_centralwidget.setFixedSize(430,500)
        self.green_setting_centralwidget.setStyleSheet(
"""
QWidget {
    background-color: #14B57A;
}
QLabel {
    font-family: 'Roboto Mono', monospace;
    font-size: 18px;
}
QFrame {
    background-color: #24E29D;
    border-radius: 7px;
}
"""
)
        self.green_setting_verticalLayout = QtWidgets.QVBoxLayout(self.green_setting_centralwidget)
        self.green_setting_title_layout = QtWidgets.QHBoxLayout()

        self.green_setting_home_btn = QtWidgets.QPushButton()
        self.green_setting_home_btn.setIcon(QtGui.QIcon(r".\Asserts\images\home"))
        self.green_setting_home_btn.setIconSize(QtCore.QSize(25, 25))
        self.green_setting_home_btn.setFixedSize(40,40)
        self.green_setting_home_btn.setStyleSheet(
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

        self.green_setting_title_label = QtWidgets.QLabel("           Setting")
        self.green_setting_title_label.setStyleSheet(
"""
QLabel {
    background-color: transparent;
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
"""
        )
        self.green_setting_title_layout = QtWidgets.QHBoxLayout()
        self.green_setting_title_layout.addWidget(self.green_setting_home_btn)
        self.green_setting_title_layout.addWidget(self.green_setting_title_label)


        self.green_setting_verticalLayout.addLayout(self.green_setting_title_layout)

        self.green_setting_apperance_frame = QtWidgets.QFrame()
        self.green_setting_apperance_frame.setFixedSize(400, 180)
        self.green_setting_apperance_layout = QtWidgets.QVBoxLayout(self.green_setting_apperance_frame)

        self.green_setting_apperance_label = QtWidgets.QLabel("        Apperance")
        self.green_setting_apperance_label.setStyleSheet(
"""
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 30px;
}
"""
)

        self.green_setting_apperance_layout.addWidget(self.green_setting_apperance_label)
        self.green_setting_apperance_layout.addStretch(1)

        self.green_setting_dark_theme_btn = QtWidgets.QRadioButton()
        self.green_setting_dark_theme_btn.setFixedSize(25,25)
        self.green_setting_light_theme_btn = QtWidgets.QRadioButton()
        self.green_setting_light_theme_btn.setFixedSize(25,25)
        self.green_setting_green_theme_btn = QtWidgets.QRadioButton()
        self.green_setting_green_theme_btn.setFixedSize(25,25)

        self.green_setting_dark_theme_label = QtWidgets.QLabel("Dark Mode")
        self.green_setting_light_theme_label = QtWidgets.QLabel("Light Mode")
        self.green_setting_green_theme_label = QtWidgets.QLabel("Green Mode")

        self.green_setting_dark_theme_layout = QtWidgets.QHBoxLayout()
        self.green_setting_light_theme_layout = QtWidgets.QHBoxLayout()
        self.green_setting_green_theme_layout = QtWidgets.QHBoxLayout()

        self.green_setting_dark_theme_layout.addWidget(self.green_setting_dark_theme_btn)
        self.green_setting_dark_theme_layout.addWidget(self.green_setting_dark_theme_label)
        self.green_setting_light_theme_layout.addWidget(self.green_setting_light_theme_btn)
        self.green_setting_light_theme_layout.addWidget(self.green_setting_light_theme_label)
        self.green_setting_green_theme_layout.addWidget(self.green_setting_green_theme_btn)
        self.green_setting_green_theme_layout.addWidget(self.green_setting_green_theme_label)

        self.green_setting_apperance_layout.addLayout(self.green_setting_dark_theme_layout)
        self.green_setting_apperance_layout.addLayout(self.green_setting_light_theme_layout)
        self.green_setting_apperance_layout.addLayout(self.green_setting_green_theme_layout)
        self.green_setting_apperance_layout.addStretch(1)

        self.green_setting_verticalLayout.addSpacing(12)
        self.green_setting_verticalLayout.addWidget(self.green_setting_apperance_frame)
        self.green_setting_verticalLayout.addStretch(1)

        self.green_setting_keyboard_frame = QtWidgets.QFrame()

        self.green_setting_keyboard_frame.setFixedSize(400, 120)
        self.green_setting_keyboard_layout = QtWidgets.QVBoxLayout(self.green_setting_keyboard_frame)

        self.green_setting_keyboard_label = QtWidgets.QLabel()
        self.green_setting_keyboard_label.setText("         Keyboard Shortcut")
        self.green_setting_keyboard_label.setStyleSheet(
'''
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 27px;
}
''')
        self.green_setting_keyboard_layout.addWidget(self.green_setting_keyboard_label)


        self.green_setting_keyboard_shortcut_label = QtWidgets.QLabel("Home Page  :-  Shift + Tab + 6\nRobert Listener  :-  Shift + Tab + 7")

        self.green_setting_keyboard_layout.addWidget(self.green_setting_keyboard_label)
        self.green_setting_keyboard_layout.addWidget(self.green_setting_keyboard_shortcut_label)
        self.green_setting_verticalLayout.addWidget(self.green_setting_keyboard_frame)
        self.green_setting_verticalLayout.addStretch(5)

#<<<<<<<<<<<<<<<Dark code Window
        self.sort_cu = 0
        self.dark_code_centralwidget = QtWidgets.QWidget(MainWindow)
        self.dark_code_centralwidget.setFixedSize(430,500)
        self.dark_code_main_layout = QtWidgets.QVBoxLayout(self.dark_code_centralwidget)

        def dark_code_edit_popup_func(s):
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
                code = open(self.file_selected,'r')
                code = code.read()
                snippet = Snippets()
                snippet.edit_snippet(s[0],code)
            dark_code_scroll_files()

        def dark_code_scroll_files():
            code_snippet = Snippets()
            if self.sort_cu == 0:
                #self.sort_cu = 0
                self.files = [[i[0],i[3].capitalize()] for i in code_snippet.list_snippets()]
                self.files.reverse()
            else:
                #self.sort_cu = 1
                self.files = [[i[0],i[3].lower()] for i in code_snippet.list_snippets()]
                sorted(self.files, key=lambda x: x[1])
                self.files = [[i[0],i[1].capitalize()] for i in self.files]

            self.dark_code_scrollAreaWidgetContents.deleteLater()
            self.dark_code_scrollAreaWidgetContents = QtWidgets.QWidget(self.dark_code_scrollArea)
            self.dark_code_scrollArea.setWidget(self.dark_code_scrollAreaWidgetContents)
            self.dark_code_form_layout = QtWidgets.QFormLayout(self.dark_code_scrollAreaWidgetContents)
            for i,s in enumerate(self.files):
                dark_code_scroll_btns_layout = QtWidgets.QHBoxLayout()
                dark_code_scroll_main_btn = QPushButton(self.files[i][1])
                dark_code_scroll_main_btn.setFixedSize(300,60)
                dark_code_scroll_main_btn.setStyleSheet(
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
                dark_code_scroll_edit_btn = QPushButton()
                dark_code_scroll_edit_btn.setIcon(QtGui.QIcon(r".\Asserts\images\edit_icon.png"))
                dark_code_scroll_edit_btn.setIconSize(QtCore.QSize(28, 28))
                dark_code_scroll_edit_btn.setFixedSize(30,60)
                dark_code_scroll_edit_btn.clicked.connect(lambda checked, i= s: dark_code_edit_popup_func(i))
                dark_code_scroll_edit_btn.setStyleSheet(
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
                dark_code_scroll_del_btn = QPushButton()
                dark_code_scroll_del_btn.setIcon(QtGui.QIcon(r".\Asserts\images\del_icon.png"))
                dark_code_scroll_del_btn.setIconSize(QtCore.QSize(28, 28))
                dark_code_scroll_del_btn.setFixedSize(30,60)
                dark_code_scroll_del_btn.clicked.connect(lambda checked, txt=s:dark_code_delete_action(txt))
                dark_code_scroll_del_btn.setStyleSheet(
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
                dark_code_scroll_btns_layout.addWidget(dark_code_scroll_main_btn)
                dark_code_scroll_btns_layout.addWidget(dark_code_scroll_edit_btn)
                dark_code_scroll_btns_layout.addWidget(dark_code_scroll_del_btn)
                self.dark_code_form_layout.addRow(dark_code_scroll_btns_layout)

        self.dark_code_search_layout = QtWidgets.QHBoxLayout()

        self.dark_code_title_label = QtWidgets.QLabel("    Robert codes")
        self.dark_code_title_label.setStyleSheet(
'''
QLabel {
    color: #FFFFFF;
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
''')
        self.dark_code_title_layout = QtWidgets.QHBoxLayout()
        self.dark_code_home_btn = QtWidgets.QPushButton()
        self.dark_code_home_btn.setIcon(QtGui.QIcon(r".\Asserts\images\home"))
        self.dark_code_home_btn.setIconSize(QtCore.QSize(25, 25))
        self.dark_code_home_btn.setFixedSize(40,40)
        self.dark_code_home_btn.setStyleSheet(
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
        self.dark_code_title_layout.addWidget(self.dark_code_home_btn)
        self.dark_code_title_layout.addWidget(self.dark_code_title_label)
        self.dark_code_main_layout.addLayout(self.dark_code_title_layout)

        self.dark_code_search_textarea = QtWidgets.QTextEdit()
        self.dark_code_search_textarea.setFixedSize(340,50)
        self.dark_code_search_textarea.setPlaceholderText("Search for snippets")
        self.dark_code_search_textarea.setStyleSheet(
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
        self.dark_code_search_btn = QtWidgets.QPushButton()
        self.dark_code_search_btn.setIcon(QtGui.QIcon(r".\Asserts\images\search_icon"))
        self.dark_code_search_btn.setIconSize(QtCore.QSize(30, 30))
        self.dark_code_search_btn.setFixedSize(70,50)
        self.dark_code_search_btn.setStyleSheet(
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
        self.dark_code_addcode_btn = QtWidgets.QPushButton()
        self.dark_code_addcode_btn.setIcon(QtGui.QIcon(r".\Asserts\images\add_btn.png"))
        self.dark_code_addcode_btn.setIconSize(QtCore.QSize(40, 40))
        self.dark_code_addcode_btn.setFixedSize(70,50)
        self.dark_code_addcode_btn.setStyleSheet(
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
        self.dark_code_search_layout.addWidget(self.dark_code_search_textarea)
        self.dark_code_search_layout.addWidget(self.dark_code_search_btn)
        self.dark_code_main_layout.addLayout(self.dark_code_search_layout)

        combobox_list = ["Newest","Alphabet"]

        self.dark_code_choice_group = QtWidgets.QComboBox()
        #self.dark_code_choice_group.setFixedSize(200,35)
        self.dark_code_choice_group.addItems(combobox_list)
        self.dark_code_choice_group.setStyleSheet(
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
        self.dark_code_lang_choice = QtWidgets.QComboBox()
        self.dark_code_lang_choice.addItems(lang_lst)
        self.dark_code_lang_choice.setStyleSheet(
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
        self.dark_code_sort_label = QtWidgets.QLabel("Sort by")
        self.dark_code_sort_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.dark_code_sort_layout = QtWidgets.QVBoxLayout()
        self.dark_code_sort_layout.addWidget(self.dark_code_sort_label)
        self.dark_code_sort_layout.addWidget(self.dark_code_choice_group)

        self.dark_code_lang_label = QtWidgets.QLabel("Choose Language")
        self.dark_code_lang_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.dark_code_lang_layout = QtWidgets.QVBoxLayout()
        self.dark_code_lang_layout.addWidget(self.dark_code_lang_label)
        self.dark_code_lang_layout.addWidget(self.dark_code_lang_choice)
        self.dark_code_choice_layout = QtWidgets.QHBoxLayout()
        self.dark_code_choice_layout.addLayout(self.dark_code_lang_layout)
        self.dark_code_choice_layout.addLayout(self.dark_code_sort_layout)
        self.dark_code_choice_layout.addWidget(self.dark_code_addcode_btn)

        self.dark_code_main_layout.addLayout(self.dark_code_choice_layout)
        self.dark_code_scrollArea = QtWidgets.QScrollArea(self.dark_code_centralwidget)
        self.dark_code_scrollArea.setWidgetResizable(True)
        self.dark_code_centralwidget.setStyleSheet(
"QWidget {"
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
        self.dark_code_scrollArea.setStyleSheet("background: #2f3136; border-radius: 7px;")
        self.dark_code_scrollAreaWidgetContents = QtWidgets.QWidget(self.dark_code_scrollArea)
        self.dark_code_scrollArea.setWidget(self.dark_code_scrollAreaWidgetContents)

        self.dark_code_main_layout.addWidget(self.dark_code_scrollArea)
        self.dark_code_form_layout = QtWidgets.QFormLayout(self.dark_code_scrollAreaWidgetContents)

        def copyed(txt):
            import clipboard
            file = open(f".\\codes\\{txt}.txt", 'r')
            file = file.read()
            clipboard.copy(file)

        def dark_code_delete_action(s):
            del_snippet = Snippets()
            del_snippet.delete_snippet(s[0])
            dark_code_scroll_files()

        dark_code_scroll_files()

        def dark_code_combo(index):
            self.sort_cu = index
            dark_code_scroll_files()

        #-----------------code adding window------------------------------------------------
        def dark_code_dialog_popup_func():
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

                def popup_cancel_func():
                    self.files_set_DialogWindow.accept()

                self.dialog_cancel_btn.clicked.connect(lambda: popup_cancel_func())

                self.dialog_textEdit = QtWidgets.QTextEdit(self.files_set_DialogWindow)
                self.dialog_textEdit.setGeometry(QtCore.QRect(20, 80, 291, 41))
                self.dialog_textEdit.setPlaceholderText("Type Name of your Code")
                self.dialog_label = QtWidgets.QLabel(self.files_set_DialogWindow)
                self.dialog_label.setGeometry(QtCore.QRect(60, 20, 231, 41))
                self.dialog_label.setText("Name your Code")

                def add_clicked():
                    if self.dialog_textEdit.toPlainText() == "":
                        pass
                    else:
                        code = open(self.file_selected,"r")
                        code = code.read()
                        code_ext = self.file_selected.split(".")[1]
                        code_snippet = Snippets()
                        code_snippet.insert_snippet(code, code_ext, self.dialog_textEdit.toPlainText())
                        dark_code_scroll_files()
                        self.files_set_DialogWindow.accept()

                self.dialog_ok_btn.clicked.connect(lambda: add_clicked())

                import sys
                self.files_set_DialogWindow.exec_()

#-----------------end of code adding--------------------------------------
        self.dark_code_addcode_btn.clicked.connect(lambda: dark_code_dialog_popup_func())
        self.dark_code_choice_group.activated.connect(dark_code_combo)

#<<<<<<<<<<<<<<<Light code Window
        self.light_code_centralwidget = QtWidgets.QWidget(MainWindow)
        self.light_code_centralwidget.setFixedSize(430,500)
        self.light_code_main_layout = QtWidgets.QVBoxLayout(self.light_code_centralwidget)

        def light_code_edit_popup_func(s):
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
                code = open(self.file_selected,'r')
                code = code.read()
                snippet = Snippets()
                snippet.edit_snippet(s[0],code)
            light_code_scroll_files()

        def light_code_scroll_files():
            code_snippet = Snippets()
            if self.sort_cu == 0:
                self.sort_cu = 0
                self.files = [[i[0],i[3].capitalize()] for i in code_snippet.list_snippets()]
                self.files.reverse()
            else:
                self.sort_cu = 1
                self.files = [[i[0],i[3].lower()] for i in code_snippet.list_snippets()]
                sorted(self.files, key=lambda x: x[1])
                self.files = [[i[0],i[1].capitalize()] for i in self.files]

            self.light_code_scrollAreaWidgetContents.deleteLater()
            self.light_code_scrollAreaWidgetContents = QtWidgets.QWidget(self.light_code_scrollArea)
            self.light_code_scrollArea.setWidget(self.light_code_scrollAreaWidgetContents)
            self.light_code_form_layout = QtWidgets.QFormLayout(self.light_code_scrollAreaWidgetContents)
            for i,s in enumerate(self.files):
                light_code_scroll_btns_layout = QtWidgets.QHBoxLayout()
                light_code_scroll_main_btn = QPushButton(self.files[i][1])
                light_code_scroll_main_btn.setFixedSize(300,60)
                light_code_scroll_main_btn.setStyleSheet(
'''
QPushButton {
    background-color: #e3e5e8;
    font-family: 'Roboto Mono', monospace;
    font-size: 20px;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    border-top-right-radius: 0px;
    border-bottom-right-radius: 0px;
}
QPushButton:hover {
    background-color: #C9C9C9;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
''')
                light_code_scroll_edit_btn = QPushButton()
                light_code_scroll_edit_btn.setIcon(QtGui.QIcon(r".\Asserts\images\edit_icon.png"))
                light_code_scroll_edit_btn.setIconSize(QtCore.QSize(28, 28))
                light_code_scroll_edit_btn.setFixedSize(30,60)
                light_code_scroll_edit_btn.clicked.connect(lambda checked, i= s: light_code_edit_popup_func(i))
                light_code_scroll_edit_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-radius: 0px;
}
QPushButton:hover {
    background-color: #e3e5e8;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
''')
                light_code_scroll_del_btn = QPushButton()
                light_code_scroll_del_btn.setIcon(QtGui.QIcon(r".\Asserts\images\del_icon.png"))
                light_code_scroll_del_btn.setIconSize(QtCore.QSize(28, 28))
                light_code_scroll_del_btn.setFixedSize(30,60)
                light_code_scroll_del_btn.clicked.connect(lambda checked, txt=s:light_code_delete_action(txt))
                light_code_scroll_del_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-top-left-radius: 0;
    border-bottom-left-radius: 00px;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
}
QPushButton:hover {
    background-color: #e3e5e8;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
''')
                light_code_scroll_btns_layout.addWidget(light_code_scroll_main_btn)
                light_code_scroll_btns_layout.addWidget(light_code_scroll_edit_btn)
                light_code_scroll_btns_layout.addWidget(light_code_scroll_del_btn)
                self.light_code_form_layout.addRow(light_code_scroll_btns_layout)

        self.light_code_search_layout = QtWidgets.QHBoxLayout()

        self.light_code_title_label = QtWidgets.QLabel("    Robert codes")
        self.light_code_title_label.setStyleSheet(
'''
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
''')
        self.light_code_title_layout = QtWidgets.QHBoxLayout()
        self.light_code_home_btn = QtWidgets.QPushButton()
        self.light_code_home_btn.setIcon(QtGui.QIcon(r".\Asserts\images\home"))
        self.light_code_home_btn.setIconSize(QtCore.QSize(25, 25))
        self.light_code_home_btn.setFixedSize(40,40)
        self.light_code_home_btn.setStyleSheet(
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
        self.light_code_title_layout.addWidget(self.light_code_home_btn)
        self.light_code_title_layout.addWidget(self.light_code_title_label)
        self.light_code_main_layout.addLayout(self.light_code_title_layout)

        self.light_code_search_textarea = QtWidgets.QTextEdit()
        self.light_code_search_textarea.setFixedSize(340,50)
        self.light_code_search_textarea.setPlaceholderText("Search for snippets")
        self.light_code_search_textarea.setStyleSheet(
'''
QTextEdit {
    font-family: 'Cabin', sans-serif;
    font-size: 22px;
    background: #ebedef;
    border-radius: 5px;
}
'''
)
        self.light_code_search_btn = QtWidgets.QPushButton()
        self.light_code_search_btn.setIcon(QtGui.QIcon(r".\Asserts\images\search_icon"))
        self.light_code_search_btn.setIconSize(QtCore.QSize(30, 30))
        self.light_code_search_btn.setFixedSize(70,50)
        self.light_code_search_btn.setStyleSheet(
'''
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
''')
        self.light_code_addcode_btn = QtWidgets.QPushButton()
        self.light_code_addcode_btn.setIcon(QtGui.QIcon(r".\Asserts\images\add_btn.png"))
        self.light_code_addcode_btn.setIconSize(QtCore.QSize(40, 40))
        self.light_code_addcode_btn.setFixedSize(70,50)
        self.light_code_addcode_btn.setStyleSheet(
'''
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
''')
        self.light_code_search_layout.addWidget(self.light_code_search_textarea)
        self.light_code_search_layout.addWidget(self.light_code_search_btn)
        self.light_code_main_layout.addLayout(self.light_code_search_layout)

        combobox_list = ["Newest","Alphabet"]

        self.light_code_choice_group = QtWidgets.QComboBox()
        self.light_code_choice_group.addItems(combobox_list)
        self.light_code_choice_group.setStyleSheet(
'''
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
'''
)
        lang_lst = ["All Languages","Python", "Java", "C++", "C#", "Golang", "Javascript", "Typescript",
                    "Html", "CSS", "PHP","Dart", "Scala", "Ruby", "R", "kotlin", "rust", "Lua",
                    "Haskel"]
        self.light_code_lang_choice = QtWidgets.QComboBox()
        self.light_code_lang_choice.addItems(lang_lst)
        self.light_code_lang_choice.setStyleSheet(
'''
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
'''
)
        self.light_code_sort_label = QtWidgets.QLabel("Sort by")
        self.light_code_sort_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.light_code_sort_layout = QtWidgets.QVBoxLayout()
        self.light_code_sort_layout.addWidget(self.light_code_sort_label)
        self.light_code_sort_layout.addWidget(self.light_code_choice_group)

        self.light_code_lang_label = QtWidgets.QLabel("Choose Language")
        self.light_code_lang_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.light_code_lang_layout = QtWidgets.QVBoxLayout()
        self.light_code_lang_layout.addWidget(self.light_code_lang_label)
        self.light_code_lang_layout.addWidget(self.light_code_lang_choice)
        self.light_code_choice_layout = QtWidgets.QHBoxLayout()
        self.light_code_choice_layout.addLayout(self.light_code_lang_layout)
        self.light_code_choice_layout.addLayout(self.light_code_sort_layout)
        self.light_code_choice_layout.addWidget(self.light_code_addcode_btn)

        self.light_code_main_layout.addLayout(self.light_code_choice_layout)
        self.light_code_scrollArea = QtWidgets.QScrollArea(self.light_code_centralwidget)
        self.light_code_scrollArea.setWidgetResizable(True)
        self.light_code_centralwidget.setStyleSheet(
"QWidget {"
"   background: #ffffff;"
"}"
"QScrollArea {"
"background-color: #f2f3f5"
"}"
"/* VERTICAL SCROLLBAR */"
" QScrollBar:vertical {"
"    border: none;"
"    background: #e3e5e8;"
"    width: 14px;"
"    margin: 15px 0 15px 0;"
"    "
" }"
""
"/*  HANDLE BAR VERTICAL */"
"QScrollBar::handle:vertical {    "
"    background-color: #D0D0D0;"
"    min-height: 30px;"
"    "
"}"
"QScrollBar::handle:vertical:hover{    "
"    background-color: #B7B7B7;"
"}"
"QScrollBar::handle:vertical:pressed {    "
"    background-color: #A9A9A9;"
"}"
""
"/* BTN TOP - SCROLLBAR */"
"QScrollBar::sub-line:vertical {"
"    border: none;"
"    background-color: #D0D0D0;"
"    height: 15px;"
"    border-top-left-radius: 7px;"
"    border-top-right-radius: 7px;"
"    subcontrol-position: top;"
"    subcontrol-origin: margin;"
"}"
"QScrollBar::sub-line:vertical:hover {    "
"    background-color: #B7B7B7;"
"}"
"QScrollBar::sub-line:vertical:pressed {    "
"    background-color: #A9A9A9;"
"}"
""
"/* BTN BOTTOM - SCROLLBAR */"
"QScrollBar::add-line:vertical {"
"    border: none;"
"    background-color: #D0D0D0;"
"    height: 15px;"
"    border-bottom-left-radius: 7px;"
"    border-bottom-right-radius: 7px;"
"    subcontrol-position: bottom;"
"    subcontrol-origin: margin;"
"}"
"QScrollBar::add-line:vertical:hover {    "
"    background-color: #B7B7B7;"
"}"
"QScrollBar::add-line:vertical:pressed {    "
"    background-color: #A9A9A9;"
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
        self.light_code_scrollArea.setStyleSheet("background: #f2f3f5; border-radius: 7px;")
        self.light_code_scrollAreaWidgetContents = QtWidgets.QWidget(self.light_code_scrollArea)
        self.light_code_scrollArea.setWidget(self.light_code_scrollAreaWidgetContents)

        self.light_code_main_layout.addWidget(self.light_code_scrollArea)
        self.light_code_form_layout = QtWidgets.QFormLayout(self.light_code_scrollAreaWidgetContents)

        def copyed(txt):
            import clipboard
            file = open(f".\\codes\\{txt}.txt", 'r')
            file = file.read()
            clipboard.copy(file)

        def light_code_delete_action(s):
            del_snippet = Snippets()
            del_snippet.delete_snippet(s[0])
            light_code_scroll_files()

        light_code_scroll_files()

        def light_code_combo(index):
            self.sort_cu = index
            light_code_scroll_files()

        #-----------------code adding window------------------------------------------------
        def light_code_dialog_popup_func():
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
    background-color: #ffffff;
}
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 30px;
}
QPushButton {
    background-color: #e3e5e8;
    border-radius: 5px;
    font-family: 'Roboto Mono', monospace;
    font-size: 20px;
}
QPushButton:hover {
    background-color: #C9C9C9;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
QTextEdit{
    background-color: #ebedef;
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

                def popup_cancel_func():
                    self.files_set_DialogWindow.accept()

                self.dialog_cancel_btn.clicked.connect(lambda: popup_cancel_func())

                self.dialog_textEdit = QtWidgets.QTextEdit(self.files_set_DialogWindow)
                self.dialog_textEdit.setGeometry(QtCore.QRect(20, 80, 291, 41))
                self.dialog_textEdit.setPlaceholderText("Type Name of your Code")
                self.dialog_label = QtWidgets.QLabel(self.files_set_DialogWindow)
                self.dialog_label.setGeometry(QtCore.QRect(60, 20, 231, 41))
                self.dialog_label.setText("Name your Code")

                def add_clicked():
                    if self.dialog_textEdit.toPlainText() == "":
                        pass
                    else:
                        code = open(self.file_selected,"r")
                        code = code.read()
                        code_ext = self.file_selected.split(".")[1]
                        code_snippet = Snippets()
                        code_snippet.insert_snippet(code, code_ext, self.dialog_textEdit.toPlainText())
                        light_code_scroll_files()
                        self.files_set_DialogWindow.accept()

                self.dialog_ok_btn.clicked.connect(lambda: add_clicked())

                import sys
                self.files_set_DialogWindow.exec_()

#-----------------end of code adding--------------------------------------
        self.light_code_addcode_btn.clicked.connect(lambda: light_code_dialog_popup_func())
        self.light_code_choice_group.activated.connect(light_code_combo)

#<<<<<<<<<<<<<<<Green code Window
        self.green_code_centralwidget = QtWidgets.QWidget(MainWindow)
        self.green_code_centralwidget.setFixedSize(430,500)
        self.green_code_main_layout = QtWidgets.QVBoxLayout(self.green_code_centralwidget)

        def green_code_edit_popup_func(s):
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
                code = open(self.file_selected,'r')
                code = code.read()
                snippet = Snippets()
                snippet.edit_snippet(s[0],code)
            green_code_scroll_files()

        def green_code_scroll_files():
            code_snippet = Snippets()
            if self.sort_cu == 0:
                self.sort_cu = 0
                self.files = [[i[0],i[3].capitalize()] for i in code_snippet.list_snippets()]
                self.files.reverse()
            else:
                self.sort_cu = 1
                self.files = [[i[0],i[3].lower()] for i in code_snippet.list_snippets()]
                sorted(self.files, key=lambda x: x[1])
                self.files = [[i[0],i[1].capitalize()] for i in self.files]

            self.green_code_scrollAreaWidgetContents.deleteLater()
            self.green_code_scrollAreaWidgetContents = QtWidgets.QWidget(self.green_code_scrollArea)
            self.green_code_scrollArea.setWidget(self.green_code_scrollAreaWidgetContents)
            self.green_code_form_layout = QtWidgets.QFormLayout(self.green_code_scrollAreaWidgetContents)
            for i,s in enumerate(self.files):
                green_code_scroll_btns_layout = QtWidgets.QHBoxLayout()
                green_code_scroll_main_btn = QPushButton(self.files[i][1])
                green_code_scroll_main_btn.setFixedSize(300,60)
                green_code_scroll_main_btn.setStyleSheet(
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
                green_code_scroll_edit_btn = QPushButton()
                green_code_scroll_edit_btn.setIcon(QtGui.QIcon(r".\Asserts\images\edit_icon.png"))
                green_code_scroll_edit_btn.setIconSize(QtCore.QSize(28, 28))
                green_code_scroll_edit_btn.setFixedSize(30,60)
                green_code_scroll_edit_btn.clicked.connect(lambda checked, i= s: green_code_edit_popup_func(i))
                green_code_scroll_edit_btn.setStyleSheet(
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
                green_code_scroll_del_btn = QPushButton()
                green_code_scroll_del_btn.setIcon(QtGui.QIcon(r".\Asserts\images\del_icon.png"))
                green_code_scroll_del_btn.setIconSize(QtCore.QSize(28, 28))
                green_code_scroll_del_btn.setFixedSize(30,60)
                green_code_scroll_del_btn.clicked.connect(lambda checked, txt=s:green_code_delete_action(txt))
                green_code_scroll_del_btn.setStyleSheet(
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
                green_code_scroll_btns_layout.addWidget(green_code_scroll_main_btn)
                green_code_scroll_btns_layout.addWidget(green_code_scroll_edit_btn)
                green_code_scroll_btns_layout.addWidget(green_code_scroll_del_btn)
                self.green_code_form_layout.addRow(green_code_scroll_btns_layout)

        self.green_code_search_layout = QtWidgets.QHBoxLayout()

        self.green_code_title_label = QtWidgets.QLabel("    Robert codes")
        self.green_code_title_label.setStyleSheet(
'''
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
''')
        self.green_code_title_layout = QtWidgets.QHBoxLayout()
        self.green_code_home_btn = QtWidgets.QPushButton()
        self.green_code_home_btn.setIcon(QtGui.QIcon(r".\Asserts\images\home"))
        self.green_code_home_btn.setIconSize(QtCore.QSize(25, 25))
        self.green_code_home_btn.setFixedSize(40,40)
        self.green_code_home_btn.setStyleSheet(
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
        self.green_code_title_layout.addWidget(self.green_code_home_btn)
        self.green_code_title_layout.addWidget(self.green_code_title_label)
        self.green_code_main_layout.addLayout(self.green_code_title_layout)

        self.green_code_search_textarea = QtWidgets.QTextEdit()
        self.green_code_search_textarea.setFixedSize(340,50)
        self.green_code_search_textarea.setPlaceholderText("Search for snippets")
        self.green_code_search_textarea.setStyleSheet(
'''
QTextEdit {
    font-family: 'Cabin', sans-serif;
    font-size: 22px;
    background: #24E29D;
    border-radius: 5px;
}
'''
)
        self.green_code_search_btn = QtWidgets.QPushButton()
        self.green_code_search_btn.setIcon(QtGui.QIcon(r".\Asserts\images\search_icon"))
        self.green_code_search_btn.setIconSize(QtCore.QSize(30, 30))
        self.green_code_search_btn.setFixedSize(70,50)
        self.green_code_search_btn.setStyleSheet(
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
        self.green_code_addcode_btn = QtWidgets.QPushButton()
        self.green_code_addcode_btn.setIcon(QtGui.QIcon(r".\Asserts\images\add_btn.png"))
        self.green_code_addcode_btn.setIconSize(QtCore.QSize(40, 40))
        self.green_code_addcode_btn.setFixedSize(70,50)
        self.green_code_addcode_btn.setStyleSheet(
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
        self.green_code_search_layout.addWidget(self.green_code_search_textarea)
        self.green_code_search_layout.addWidget(self.green_code_search_btn)
        self.green_code_main_layout.addLayout(self.green_code_search_layout)

        combobox_list = ["Newest","Alphabet"]

        self.green_code_choice_group = QtWidgets.QComboBox()
        #self.green_code_choice_group.setFixedSize(200,35)
        self.green_code_choice_group.addItems(combobox_list)
        self.green_code_choice_group.setStyleSheet(
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
        self.green_code_lang_choice = QtWidgets.QComboBox()
        self.green_code_lang_choice.addItems(lang_lst)
        self.green_code_lang_choice.setStyleSheet(
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
        self.green_code_sort_label = QtWidgets.QLabel("Sort by")
        self.green_code_sort_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.green_code_sort_layout = QtWidgets.QVBoxLayout()
        self.green_code_sort_layout.addWidget(self.green_code_sort_label)
        self.green_code_sort_layout.addWidget(self.green_code_choice_group)

        self.green_code_lang_label = QtWidgets.QLabel("Choose Language")
        self.green_code_lang_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.green_code_lang_layout = QtWidgets.QVBoxLayout()
        self.green_code_lang_layout.addWidget(self.green_code_lang_label)
        self.green_code_lang_layout.addWidget(self.green_code_lang_choice)
        self.green_code_choice_layout = QtWidgets.QHBoxLayout()
        self.green_code_choice_layout.addLayout(self.green_code_lang_layout)
        self.green_code_choice_layout.addLayout(self.green_code_sort_layout)
        self.green_code_choice_layout.addWidget(self.green_code_addcode_btn)

        self.green_code_main_layout.addLayout(self.green_code_choice_layout)
        self.green_code_scrollArea = QtWidgets.QScrollArea(self.green_code_centralwidget)
        self.green_code_scrollArea.setWidgetResizable(True)
        self.green_code_centralwidget.setStyleSheet(
"QWidget {"
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
        self.green_code_scrollArea.setStyleSheet("background: #2ABF88; border-radius: 7px;")
        self.green_code_scrollAreaWidgetContents = QtWidgets.QWidget(self.green_code_scrollArea)
        self.green_code_scrollArea.setWidget(self.green_code_scrollAreaWidgetContents)

        self.green_code_main_layout.addWidget(self.green_code_scrollArea)
        self.green_code_form_layout = QtWidgets.QFormLayout(self.green_code_scrollAreaWidgetContents)

        def copyed(txt):
            import clipboard
            file = open(f".\\codes\\{txt}.txt", 'r')
            file = file.read()
            clipboard.copy(file)

        def green_code_delete_action(s):
            del_snippet = Snippets()
            del_snippet.delete_snippet(s[0])
            green_code_scroll_files()

        green_code_scroll_files()

        def green_code_combo(index):
            self.sort_cu = index
            green_code_scroll_files()

        #-----------------code adding window------------------------------------------------
        def green_code_dialog_popup_func():
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

                def popup_cancel_func():
                    self.files_set_DialogWindow.accept()

                self.dialog_cancel_btn.clicked.connect(lambda: popup_cancel_func())

                self.dialog_textEdit = QtWidgets.QTextEdit(self.files_set_DialogWindow)
                self.dialog_textEdit.setGeometry(QtCore.QRect(20, 80, 291, 41))
                self.dialog_textEdit.setPlaceholderText("Type Name of your Code")
                self.dialog_label = QtWidgets.QLabel(self.files_set_DialogWindow)
                self.dialog_label.setGeometry(QtCore.QRect(60, 20, 231, 41))
                self.dialog_label.setText("Name your Code")

                def add_clicked():
                    if self.dialog_textEdit.toPlainText() == "":
                        pass
                    else:
                        code = open(self.file_selected,"r")
                        code = code.read()
                        code_ext = self.file_selected.split(".")[1]
                        code_snippet = Snippets()
                        code_snippet.insert_snippet(code, code_ext, self.dialog_textEdit.toPlainText())
                        green_code_scroll_files()
                        self.files_set_DialogWindow.accept()

                self.dialog_ok_btn.clicked.connect(lambda: add_clicked())

                import sys
                self.files_set_DialogWindow.exec_()

#-----------------end of code adding--------------------------------------
        self.green_code_addcode_btn.clicked.connect(lambda: green_code_dialog_popup_func())
        self.green_code_choice_group.activated.connect(green_code_combo)

#<<<<<<<<<<<<<<<Dark trans Window
        self.to_combo_index = 0
        self.dark_trans_centralwidget = QtWidgets.QWidget(MainWindow)
        self.dark_trans_centralwidget.setFixedSize(430,500)
        self.dark_trans_vertical_layout = QtWidgets.QVBoxLayout(self.dark_trans_centralwidget)
        self.dark_trans_centralwidget.setStyleSheet(
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

        self.trans_to_lang_lst = ["French", "Hindi", "German", "Arabic", "Amharic", "Spanish", "English"
        ,"Portuguese","Chinese", "Tamil","Russian","Malayalam","Bengali","Punjabi","filipino"]
        self.dark_trans_to_lang_combo = QtWidgets.QComboBox()
        self.dark_trans_to_lang_combo.addItems(self.trans_to_lang_lst)

        self.dark_trans_to_label = QtWidgets.QLabel("To Language")
        self.dark_trans_to_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.dark_trans_to_layout = QtWidgets.QVBoxLayout()
        self.dark_trans_to_layout.addWidget(self.dark_trans_to_label)
        self.dark_trans_to_layout.addWidget(self.dark_trans_to_lang_combo)
        """
        self.dark_trans_lang_layout = QtWidgets.QHBoxLayout()
        self.dark_trans_lang_layout.addLayout(self.dark_trans_from_layout)
        self.dark_trans_lang_layout.addLayout(self.dark_trans_to_layout)
        self.dark_trans_vertical_layout.addLayout(self.dark_trans_lang_layout)
        self.dark_trans_vertical_layout.addStretch(15)
        """

        self.dark_trans_from_textedit = QtWidgets.QTextEdit()
        self.dark_trans_from_textedit.setFixedSize(410,120)
        self.dark_trans_from_textedit.setPlaceholderText("Type here")
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
        self.dark_trans_translate_btn.setIcon(QtGui.QIcon(r".\Asserts\images\translate"))
        self.dark_trans_translate_btn.setIconSize(QtCore.QSize(30, 30))
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
        self.dark_trans_translate_layout.addLayout(self.dark_trans_to_layout)
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
    font-size: 17px;
    background-color: #40444b;
    border-radius: 5px;
}
'''
)
        self.dark_trans_vertical_layout.addWidget(self.dark_trans_from_textedit)
        self.dark_trans_vertical_layout.addLayout(self.dark_trans_translate_layout)
        self.dark_trans_vertical_layout.addWidget(self.dark_trans_to_textedit)
        self.dark_trans_vertical_layout.addStretch(200)

        def dark_translation():
            translate = Translator()
            from_text = self.dark_trans_from_textedit.toPlainText()
            if from_text == "":
                pass
            else:
                translation = translate.translate(from_text, self.trans_to_lang_lst[self.to_combo_index])
                self.dark_trans_to_textedit.setText(translation.text)
                self.dark_trans_to_textedit.repaint()

        self.dark_trans_translate_btn.clicked.connect(lambda: dark_translation())

        def trans_combo(index):
            self.to_combo_index = index
        self.dark_trans_to_lang_combo.activated.connect(trans_combo)

#<<<<<<<<<<<<<<<light trans Window
        self.light_trans_centralwidget = QtWidgets.QWidget(MainWindow)
        self.light_trans_centralwidget.setFixedSize(430,500)
        self.light_trans_vertical_layout = QtWidgets.QVBoxLayout(self.light_trans_centralwidget)
        self.light_trans_centralwidget.setStyleSheet(
"""
QWidget {
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
        self.light_trans_home_btn.setIcon(QtGui.QIcon(r".\Asserts\images\home"))
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

        self.light_trans_to_lang_combo = QtWidgets.QComboBox()
        self.light_trans_to_lang_combo.addItems(self.trans_to_lang_lst)

        self.light_trans_to_label = QtWidgets.QLabel("To Language")
        self.light_trans_to_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.light_trans_to_layout = QtWidgets.QVBoxLayout()
        self.light_trans_to_layout.addWidget(self.light_trans_to_label)
        self.light_trans_to_layout.addWidget(self.light_trans_to_lang_combo)

        self.light_trans_from_textedit = QtWidgets.QTextEdit()
        self.light_trans_from_textedit.setFixedSize(410,120)
        self.light_trans_from_textedit.setPlaceholderText("Type here")
        self.light_trans_from_textedit.setStyleSheet(
'''
QTextEdit {
    font-family: 'Cabin', sans-serif;
    font-size: 15px;
    background: #ebedef;
    border-radius: 5px;
}
'''
)
        self.light_trans_translate_btn = QtWidgets.QPushButton()
        self.light_trans_translate_btn.setIcon(QtGui.QIcon(r".\Asserts\images\translate"))
        self.light_trans_translate_btn.setIconSize(QtCore.QSize(30, 30))
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
        self.light_trans_translate_layout.addLayout(self.light_trans_to_layout)
        self.light_trans_translate_layout.addWidget(self.light_trans_translate_btn)

        self.light_trans_to_textedit = QtWidgets.QTextEdit()
        self.light_trans_to_textedit.setFixedSize(410,180)
        self.light_trans_to_textedit.setPlaceholderText("Comment allez-vous")
        self.light_trans_to_textedit.setReadOnly(True)
        self.light_trans_to_textedit.setStyleSheet(
'''
QTextEdit {
    font-family: 'Cabin', sans-serif;
    font-size: 17px;
    background: #ebedea;
    border-radius: 5px;
}
'''
)
        self.light_trans_vertical_layout.addWidget(self.light_trans_from_textedit)
        self.light_trans_vertical_layout.addLayout(self.light_trans_translate_layout)
        self.light_trans_vertical_layout.addWidget(self.light_trans_to_textedit)
        self.light_trans_vertical_layout.addStretch(200)

        def light_translation():
            translate = Translator()
            from_text = self.light_trans_from_textedit.toPlainText()
            if from_text == "":
                pass
            else:

                translation = translate.translate(from_text, self.trans_to_lang_lst[self.to_combo_index])
                self.light_trans_to_textedit.setText(translation.text)
                self.light_trans_to_textedit.repaint()

        self.light_trans_translate_btn.clicked.connect(lambda: light_translation())

        self.light_trans_to_lang_combo.activated.connect(trans_combo)

#<<<<<<<<<<<<<<<green trans Window
        self.green_trans_centralwidget = QtWidgets.QWidget(MainWindow)
        self.green_trans_centralwidget.setFixedSize(430,500)
        self.green_trans_vertical_layout = QtWidgets.QVBoxLayout(self.green_trans_centralwidget)
        self.green_trans_centralwidget.setStyleSheet(
"""
QWidget {
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
        self.green_trans_home_btn.setIcon(QtGui.QIcon(r".\Asserts\images\home"))
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

        self.green_trans_to_lang_combo = QtWidgets.QComboBox()
        self.green_trans_to_lang_combo.addItems(self.trans_to_lang_lst)

        self.green_trans_to_label = QtWidgets.QLabel("To Language")
        self.green_trans_to_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.green_trans_to_layout = QtWidgets.QVBoxLayout()
        self.green_trans_to_layout.addWidget(self.green_trans_to_label)
        self.green_trans_to_layout.addWidget(self.green_trans_to_lang_combo)

        self.green_trans_from_textedit = QtWidgets.QTextEdit()
        self.green_trans_from_textedit.setFixedSize(410,120)
        self.green_trans_from_textedit.setPlaceholderText("Type here")
        self.green_trans_from_textedit.setStyleSheet(
'''
QTextEdit {
    font-family: 'Cabin', sans-serif;
    font-size: 15px;
    background: #24E29D;
    border-radius: 5px;
}
'''
)
        self.green_trans_translate_btn = QtWidgets.QPushButton()
        self.green_trans_translate_btn.setIcon(QtGui.QIcon(r".\Asserts\images\translate"))
        self.green_trans_translate_btn.setIconSize(QtCore.QSize(30, 30))
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
        self.green_trans_translate_layout.addLayout(self.green_trans_to_layout)
        self.green_trans_translate_layout.addWidget(self.green_trans_translate_btn)

        self.green_trans_to_textedit = QtWidgets.QTextEdit()
        self.green_trans_to_textedit.setFixedSize(410,180)
        self.green_trans_to_textedit.setPlaceholderText("Comment allez-vous")
        self.green_trans_to_textedit.setReadOnly(True)
        self.green_trans_to_textedit.setStyleSheet(
'''
QTextEdit {
    font-family: 'Cabin', sans-serif;
    font-size: 17px;
    background: #24E293;
    border-radius: 5px;
}
'''
)
        self.green_trans_vertical_layout.addWidget(self.green_trans_from_textedit)
        self.green_trans_vertical_layout.addLayout(self.green_trans_translate_layout)
        self.green_trans_vertical_layout.addWidget(self.green_trans_to_textedit)
        self.green_trans_vertical_layout.addStretch(200)

        def green_translation():
            translate = Translator()
            from_text = self.green_trans_from_textedit.toPlainText()
            if from_text == "":
                pass
            else:
                translation = translate.translate(from_text, self.trans_to_lang_lst[self.to_combo_index])
                self.green_trans_to_textedit.setText(translation.text)
                self.green_trans_to_textedit.repaint()

        self.green_trans_translate_btn.clicked.connect(lambda: green_translation())
        self.green_trans_to_lang_combo.activated.connect(trans_combo)

#<<<<<<<<<<<<<<<green task Window
        self.task_sort = 0
        self.green_task_centralwidget = QtWidgets.QWidget(MainWindow)
        self.green_task_centralwidget.setFixedSize(430,500)
        self.green_task_verticalLayout = QtWidgets.QVBoxLayout(self.green_task_centralwidget)
        self.green_task_title_layout = QtWidgets.QHBoxLayout()

        def green_task_delete_action(s):
            del_task = TaskManager()
            print(del_task.delete_task(s[0]))
            green_task_scroll_files()

        def green_task_task_add_func(txt,s):
            self.txt =txt
            self.s = s
            self.files_set_DialogWindow = QtWidgets.QDialog()
            self.files_set_DialogWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.files_set_DialogWindow.resize(380, 350)
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
QSpinBox {
    color: #FFFFFF;
	background-color: #2f3136;
    font-size: 15px;
	border-radius: 5px;
	padding: 5px;
	padding-left: 10px;
}
QSpinBox QAbstractItemView {
	color: #FFFFFF;
	background-color: #2f3136;
	padding: 10px;
	selection-background-color: #40444b;
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
            self.task_add_layout = QtWidgets.QVBoxLayout(self.files_set_DialogWindow)
            self.task_ok_layout = QtWidgets.QHBoxLayout()
            self.dialog_ok_btn = QtWidgets.QPushButton()
            if self.txt == "Add":
                self.dialog_ok_btn.setText("Add")
            else:
                self.dialog_ok_btn.setText("Save")

            self.dialog_cancel_btn = QtWidgets.QPushButton()
            self.dialog_cancel_btn.setText("Cancel")
            self.dialog_cancel_btn.clicked.connect(lambda: self.files_set_DialogWindow.reject())
            self.task_ok_layout.addWidget(self.dialog_ok_btn)
            self.task_ok_layout.addWidget(self.dialog_cancel_btn)

            self.dialog_label = QtWidgets.QLabel()
            self.dialog_label.setText(f"{self.txt} your Task")
            self.name_textEdit = QtWidgets.QTextEdit()
            self.name_textEdit.setPlaceholderText("Name")
            self.name_textEdit.setFixedHeight(40)

            self.desc_textedit = QtWidgets.QTextEdit()
            self.desc_textedit.setPlaceholderText("Description")
            self.desc_textedit.setFixedHeight(75)


            self.task_other_layout = QtWidgets.QHBoxLayout()
            self.task_priority_label = QtWidgets.QLabel("Priority")
            self.task_priority_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 20px;")
            self.task_priority_add = QtWidgets.QComboBox()
            self.task_priority_add.setFixedHeight(40)
            self.task_priority_add.addItems(["1", "2", "3", "4", "5"])

            self.task_priority_layout = QtWidgets.QVBoxLayout()
            self.task_priority_layout.addWidget(self.task_priority_label)
            self.task_priority_layout.addWidget(self.task_priority_add)

            self.task_other_layout.addLayout(self.task_priority_layout)


            self.task_add_layout.addWidget(self.dialog_label)
            self.task_add_layout.addWidget(self.name_textEdit)
            self.task_add_layout.addWidget(self.desc_textedit)
            self.task_add_layout.addLayout(self.task_other_layout)
            self.task_add_layout.addLayout(self.task_ok_layout)
            self.i = 1
            def add_clicked():
                name = self.name_textEdit.toPlainText()
                desc = self.desc_textedit.toPlainText()
                if name == "" or desc == "":
                        pass
                else:
                    task = TaskManager()
                    if self.txt == "Add":
                        print(task.insert_task(name, desc , self.i))
                    else:
                        print(task.edit_tasks(self.s[0], name, desc , self.i))
                    green_task_scroll_files()
                    self.files_set_DialogWindow.accept()

            self.dialog_ok_btn.clicked.connect(lambda: add_clicked())
            def combo_switch(index):
                self.i = index
                self.i += 1
                print(self.i)
            self.task_priority_add.activated.connect(combo_switch)

            self.files_set_DialogWindow.exec_()

        def green_task_scroll_files():
            task = TaskManager()
            if self.task_sort == 0:
                self.files = [[i[0],i[1].capitalize(),i[2]] for i in task.list_tasks()]
                self.files.reverse()
            elif self.task_sort == 1:
                self.files = [[i[3],i[1].capitalize(),i[2]] for i in task.list_tasks()]
                self.files.sort()
                self.files.reverse()
            else:
                self.files = [[i[0],i[1].lower(),i[2]] for i in task.list_tasks()]
                print(self.files)
                self.files = sorted(self.files, key=lambda x: x[1])
                self.files = [[i[0],i[1].capitalize(),i[2]] for i in self.files]

            self.green_task_scrollAreaWidgetContents.deleteLater()
            self.green_task_scrollAreaWidgetContents = QtWidgets.QWidget(self.green_task_scrollArea)
            self.green_task_scrollArea.setWidget(self.green_task_scrollAreaWidgetContents)
            self.green_task_form_layout = QtWidgets.QFormLayout(self.green_task_scrollAreaWidgetContents)


            for i,s in enumerate(self.files):
                green_task_scroll_btn_layout = QtWidgets.QHBoxLayout()
                green_task_checked_btn = QtWidgets.QPushButton()
                green_task_create_task_btn_func(green_task_checked_btn, i, s)
                green_task_scroll_btn_layout.addWidget(green_task_checked_btn)
                green_task_main_btn = QPushButton(self.files[i][1])
                green_task_main_btn.setFixedSize(250,60)
                green_task_main_btn.setStyleSheet(
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
                green_task_main_btn.clicked.connect(lambda checked, btn_text=s:green_task_show_des_func(btn_text))
                green_task_edit_btn = QPushButton()   #39DFA2
                green_task_edit_btn.setIcon(QtGui.QIcon(r".\Asserts\images\edit_icon.png"))
                green_task_edit_btn.setIconSize(QtCore.QSize(28, 28))
                green_task_edit_btn.setFixedSize(30,60)
                green_task_edit_btn.clicked.connect(lambda checked, s=s: green_task_task_add_func("Edit",s))
                green_task_edit_btn.setStyleSheet(
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
                green_task_del_btn = QPushButton()
                green_task_del_btn.setIcon(QtGui.QIcon(r".\Asserts\images/del_icon.png"))
                green_task_del_btn.setIconSize(QtCore.QSize(28, 28))
                green_task_del_btn.setFixedSize(30,60)
                green_task_del_btn.clicked.connect(lambda checked, s=s: green_task_delete_action(s))
                green_task_del_btn.setStyleSheet(
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
                green_task_scroll_btn_layout.addWidget(green_task_main_btn)
                green_task_scroll_btn_layout.addWidget(green_task_edit_btn)
                green_task_scroll_btn_layout.addWidget(green_task_del_btn)
                self.green_task_form_layout.addRow(green_task_scroll_btn_layout)


        self.green_task_home_btn = QtWidgets.QPushButton()
        self.green_task_home_btn.setIcon(QtGui.QIcon(r".\Asserts\images\home"))
        self.green_task_home_btn.setIconSize(QtCore.QSize(25, 25))
        self.green_task_home_btn.setFixedSize(40,40)
        self.green_task_home_btn.setStyleSheet(
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

        self.green_task_title_label = QtWidgets.QLabel("      Robert Task")
        self.green_task_title_label.setStyleSheet(
'''
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
''')
        self.green_task_title_layout = QtWidgets.QHBoxLayout()
        self.green_task_title_layout.addWidget(self.green_task_home_btn)
        self.green_task_title_layout.addWidget(self.green_task_title_label)

        self.green_task_task_addcode_btn = QtWidgets.QPushButton()
        self.green_task_task_addcode_btn.setIcon(QtGui.QIcon(r".\Asserts\images\add_btn.png"))
        self.green_task_task_addcode_btn.setIconSize(QtCore.QSize(40, 40))
        self.green_task_task_addcode_btn.setFixedSize(70,50)
        self.green_task_task_addcode_btn.setStyleSheet(
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
        self.green_task_verticalLayout.addLayout(self.green_task_title_layout)
        self.green_task_task_addcode_btn.clicked.connect(lambda checked, t="Add",s="J":green_task_task_add_func(t,s))
        self.green_task_second_layout = QtWidgets.QHBoxLayout()

        task_sort_combo_lst = ["Newest", "Priority", "Alphabet"]

        self.green_task_sort_combo = QtWidgets.QComboBox()
        self.green_task_sort_combo.setFixedSize(200,30)
        self.green_task_sort_combo.addItems(task_sort_combo_lst)
        self.green_task_sort_combo.setStyleSheet(
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
        self.green_task_sort_label = QtWidgets.QLabel("Sort by")
        self.green_task_sort_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.green_task_sort_layout = QtWidgets.QVBoxLayout()
        self.green_task_sort_layout.addWidget(self.green_task_sort_label)
        self.green_task_sort_layout.addWidget(self.green_task_sort_combo)
        self.green_task_second_layout.addLayout(self.green_task_sort_layout)
        self.green_task_second_layout.addStretch(20)
        self.green_task_second_layout.addWidget(self.green_task_task_addcode_btn)

        self.green_task_verticalLayout.addLayout(self.green_task_second_layout)
        self.green_task_scrollArea = QtWidgets.QScrollArea(self.green_task_centralwidget)
        self.green_task_scrollArea.setWidgetResizable(True)
        self.green_task_centralwidget.setStyleSheet(
"QWidget {"
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
        self.green_task_scrollArea.setStyleSheet("background: #2ABF88; border-radius: 7px;")
        self.green_task_scrollAreaWidgetContents = QtWidgets.QWidget(self.green_task_scrollArea)
        self.green_task_scrollArea.setWidget(self.green_task_scrollAreaWidgetContents)

        def green_task_show_des_func(btn_info):
            self.task_show_widget = QtWidgets.QDialog()
            vertical_lay = QtWidgets.QVBoxLayout(self.task_show_widget)
            scroll_area = QtWidgets.QScrollArea(self.task_show_widget)
            scroll_area.setWidgetResizable(True)
            scroll_area_content = QtWidgets.QWidget(scroll_area)
            scroll_area.setWidget(scroll_area_content)
            scroll_area.setStyleSheet("background: #2ABF88; border-radius: 7px;")
            form_lay = QtWidgets.QHBoxLayout(scroll_area_content)


            self.task_show_widget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.task_show_widget.resize(350, 220)
            self.task_show_widget.setMinimumSize(QtCore.QSize(350, 220))
            self.task_show_widget.setMaximumSize(QtCore.QSize(350, 220))
            self.task_show_widget.setStyleSheet("""
QDialog {
    background-color: #14B57A;
}
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 30px;
}
QPushButton {
    background-color: transparent;
    border-radius: 5px;
    font-family: 'Roboto Mono', monospace;
    font-size: 20px;
}
QPushButton:hover {
    background-color: #39DFA2;
}
QPushButton:pressed {
    background-color: #1A4E3B;
}
""")
            self.exit_btn = QtWidgets.QPushButton()
            self.exit_lay = QtWidgets.QHBoxLayout()
            self.exit_lay.addStretch(1)
            self.exit_lay.addWidget(self.exit_btn)
            self.exit_btn.setIcon(QtGui.QIcon(r".\Asserts\images\exit_icon"))
            self.exit_btn.setIconSize(QtCore.QSize(20, 20))
            self.exit_btn.setGeometry(QtCore.QRect(315, 5, 25, 25))
            self.exit_btn.clicked.connect(self.task_show_widget.accept)

            vertical_lay.addLayout(self.exit_lay)
            vertical_lay.addWidget(scroll_area)

            btn_info = btn_info[2]

            self.des_label = QtWidgets.QLabel()
            form_lay.addWidget(self.des_label)
            self.des_label.setText(f"Description:\n  {btn_info}")
            self.des_label.setGeometry(QtCore.QRect(10, 10, 300, 180))

            self.task_show_widget.exec_()

        self.green_task_verticalLayout.addWidget(self.green_task_scrollArea)

        self.green_task_form_layout = QtWidgets.QFormLayout(self.green_task_scrollAreaWidgetContents)
        self.green_task_cond_lst = [r".\Asserts\images\unchecked.png", r".\Asserts\images\checked.png"]
        self.green_task_cond = {}

        def green_task_create_task_btn_func(btn, i, s):
            self.green_task_cond[btn] = 0
            btn.setFixedSize(25,25)
            btn.setIcon(QtGui.QIcon(self.green_task_cond_lst[self.green_task_cond[btn]]))
            btn.setIconSize(QtCore.QSize(25,25))
            btn.setStyleSheet("""
QPushButton {
    background-color: transparent;
    font-size: 12px;
}
QPushButton:hover {
    background-color: #27A97A;
}
QPushButton:pressed {
    background-color: #1A4E3B;
}
""")
            def task_switch():
                self.green_task_cond[btn] = not self.green_task_cond[btn]
                btn.setIcon(QtGui.QIcon(self.green_task_cond_lst[self.green_task_cond[btn]]))
            btn.clicked.connect(lambda: task_switch())

        green_task_scroll_files()

        def green_task_combo(index):
            self.task_sort = index
            green_task_scroll_files()

        self.green_task_sort_combo.activated.connect(green_task_combo)

#<<<<<<<<<<<<<<<dark task Window
        self.dark_task_centralwidget = QtWidgets.QWidget(MainWindow)
        self.dark_task_centralwidget.setFixedSize(430,500)
        self.dark_task_verticalLayout = QtWidgets.QVBoxLayout(self.dark_task_centralwidget)
        self.dark_task_title_layout = QtWidgets.QHBoxLayout()

        def dark_task_delete_action(s):
            del_task = TaskManager()
            print(del_task.delete_task(s[0]))
            dark_task_scroll_files()

        def dark_task_task_add_func(txt, s):
            self.txt = txt
            self.files_set_DialogWindow = QtWidgets.QDialog()
            self.files_set_DialogWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.files_set_DialogWindow.resize(380, 350)
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
QSpinBox {
    color: #FFFFFF;
	background-color: #2f3136;
    font-size: 15px;
	border-radius: 5px;
	padding: 5px;
	padding-left: 10px;
}
QSpinBox QAbstractItemView {
	color: #FFFFFF;
	background-color: #2f3136;
	padding: 10px;
	selection-background-color: #40444b;
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
            self.task_add_layout = QtWidgets.QVBoxLayout(self.files_set_DialogWindow)
            self.task_ok_layout = QtWidgets.QHBoxLayout()
            self.dialog_ok_btn = QtWidgets.QPushButton()
            if self.txt == "Add":
                self.dialog_ok_btn.setText("Add")
            else:
                self.dialog_ok_btn.setText("Save")

            self.dialog_cancel_btn = QtWidgets.QPushButton()
            self.dialog_cancel_btn.setText("Cancel")
            self.dialog_cancel_btn.clicked.connect(lambda: self.files_set_DialogWindow.reject())
            self.task_ok_layout.addWidget(self.dialog_ok_btn)
            self.task_ok_layout.addWidget(self.dialog_cancel_btn)

            self.dialog_label = QtWidgets.QLabel()
            self.dialog_label.setText(f"{self.txt} your Task")
            self.name_textEdit = QtWidgets.QTextEdit()
            self.name_textEdit.setPlaceholderText("Name")
            self.name_textEdit.setFixedHeight(40)

            self.desc_textedit = QtWidgets.QTextEdit()
            self.desc_textedit.setPlaceholderText("Description")
            self.desc_textedit.setFixedHeight(75)

            self.task_other_layout = QtWidgets.QHBoxLayout()
            self.task_priority_label = QtWidgets.QLabel("Priority")
            self.task_priority_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 20px;")
            self.task_priority_add = QtWidgets.QComboBox()
            self.task_priority_add.setFixedHeight(40)
            self.task_priority_add.addItems(["1", "2", "3", "4", "5"])

            self.task_priority_layout = QtWidgets.QVBoxLayout()
            self.task_priority_layout.addWidget(self.task_priority_label)
            self.task_priority_layout.addWidget(self.task_priority_add)
            self.task_other_layout.addLayout(self.task_priority_layout)

            self.task_add_layout.addWidget(self.dialog_label)
            self.task_add_layout.addWidget(self.name_textEdit)
            self.task_add_layout.addWidget(self.desc_textedit)
            self.task_add_layout.addLayout(self.task_other_layout)
            self.task_add_layout.addLayout(self.task_ok_layout)
            self.i = 1
            self.s = s
            def add_clicked():
                name = self.name_textEdit.toPlainText()
                desc = self.desc_textedit.toPlainText()
                if name == "" or desc == "":
                        pass
                else:
                    task = TaskManager()
                    if self.txt == "Add":
                        print(task.insert_task(name, desc , self.i))
                    else:
                        print(task.edit_tasks(self.s[0], name, desc , self.i))
                    dark_task_scroll_files()
                    self.files_set_DialogWindow.accept()

            self.dialog_ok_btn.clicked.connect(lambda: add_clicked())
            def combo_switch(index):
                self.i = index
                self.i += 1
                print(self.i)
            self.task_priority_add.activated.connect(combo_switch)

            self.files_set_DialogWindow.exec_()

        def dark_task_scroll_files():
            task = TaskManager()
            if self.task_sort == 0:
                self.files = [[i[0],i[1].capitalize(),i[2]] for i in task.list_tasks()]
                self.files.reverse()
            elif self.task_sort == 1:
                self.files = [[i[3],i[1].capitalize(),i[2]] for i in task.list_tasks()]
                self.files.sort()
                self.files.reverse()
            else:
                self.files = [[i[0],i[1].lower(),i[2]] for i in task.list_tasks()]
                print(self.files)
                self.files = sorted(self.files, key=lambda x: x[1])
                self.files = [[i[0],i[1].capitalize(),i[2]] for i in self.files]

            self.dark_task_scrollAreaWidgetContents.deleteLater()
            self.dark_task_scrollAreaWidgetContents = QtWidgets.QWidget(self.dark_task_scrollArea)
            self.dark_task_scrollArea.setWidget(self.dark_task_scrollAreaWidgetContents)
            self.dark_task_form_layout = QtWidgets.QFormLayout(self.dark_task_scrollAreaWidgetContents)

            for i,s in enumerate(self.files):
                dark_task_scroll_btn_layout = QtWidgets.QHBoxLayout()
                dark_task_checked_btn = QtWidgets.QPushButton()
                dark_task_create_task_btn_func(dark_task_checked_btn, i, s)
                dark_task_scroll_btn_layout.addWidget(dark_task_checked_btn)
                dark_task_main_btn = QPushButton(self.files[i][1])
                dark_task_main_btn.setFixedSize(250,60)
                dark_task_main_btn.setStyleSheet(
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
                dark_task_main_btn.clicked.connect(lambda checked, btn_text=s:dark_task_show_des_func(btn_text))
                dark_task_edit_btn = QPushButton()   #39DFA2
                dark_task_edit_btn.setIcon(QtGui.QIcon(r".\Asserts\images\edit_icon.png"))
                dark_task_edit_btn.setIconSize(QtCore.QSize(28, 28))
                dark_task_edit_btn.setFixedSize(30,60)
                dark_task_edit_btn.clicked.connect(lambda checked, s=s: dark_task_task_add_func("Edit",s))
                dark_task_edit_btn.setStyleSheet(
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
                dark_task_del_btn = QPushButton()
                dark_task_del_btn.setIcon(QtGui.QIcon(r".\Asserts\images/del_icon.png"))
                dark_task_del_btn.setIconSize(QtCore.QSize(28, 28))
                dark_task_del_btn.setFixedSize(30,60)
                dark_task_del_btn.clicked.connect(lambda checked, s=s: dark_task_delete_action(s))
                dark_task_del_btn.setStyleSheet(
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
                dark_task_scroll_btn_layout.addWidget(dark_task_main_btn)
                dark_task_scroll_btn_layout.addWidget(dark_task_edit_btn)
                dark_task_scroll_btn_layout.addWidget(dark_task_del_btn)
                self.dark_task_form_layout.addRow(dark_task_scroll_btn_layout)

        self.dark_task_home_btn = QtWidgets.QPushButton()
        self.dark_task_home_btn.setIcon(QtGui.QIcon(r".\Asserts\images\home"))
        self.dark_task_home_btn.setIconSize(QtCore.QSize(25, 25))
        self.dark_task_home_btn.setFixedSize(40,40)
        self.dark_task_home_btn.setStyleSheet(
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

        self.dark_task_title_label = QtWidgets.QLabel("      Robert Task")
        self.dark_task_title_label.setStyleSheet(
'''
QLabel {
    color: #FFFFFF;
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
''')
        self.dark_task_title_layout = QtWidgets.QHBoxLayout()
        self.dark_task_title_layout.addWidget(self.dark_task_home_btn)
        self.dark_task_title_layout.addWidget(self.dark_task_title_label)

        self.dark_task_task_addcode_btn = QtWidgets.QPushButton()
        self.dark_task_task_addcode_btn.setIcon(QtGui.QIcon(r".\Asserts\images\add_btn.png"))
        self.dark_task_task_addcode_btn.setIconSize(QtCore.QSize(40, 40))
        self.dark_task_task_addcode_btn.setFixedSize(70,50)
        self.dark_task_task_addcode_btn.setStyleSheet(
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
        self.dark_task_verticalLayout.addLayout(self.dark_task_title_layout)
        self.dark_task_task_addcode_btn.clicked.connect(lambda checked, t="Add",s="Just":dark_task_task_add_func(t,s))
        self.dark_task_second_layout = QtWidgets.QHBoxLayout()

        task_sort_combo_lst = ["Newest", "Priority", "Alphabet"]
        self.dark_task_sort_combo = QtWidgets.QComboBox()
        self.dark_task_sort_combo.setFixedSize(200,30)
        self.dark_task_sort_combo.addItems(task_sort_combo_lst)
        self.dark_task_sort_combo.setStyleSheet(
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
        self.dark_task_sort_label = QtWidgets.QLabel("Sort by")
        self.dark_task_sort_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.dark_task_sort_layout = QtWidgets.QVBoxLayout()
        self.dark_task_sort_layout.addWidget(self.dark_task_sort_label)
        self.dark_task_sort_layout.addWidget(self.dark_task_sort_combo)
        self.dark_task_second_layout.addLayout(self.dark_task_sort_layout)
        self.dark_task_second_layout.addStretch(20)
        self.dark_task_second_layout.addWidget(self.dark_task_task_addcode_btn)

        self.dark_task_verticalLayout.addLayout(self.dark_task_second_layout)
        self.dark_task_scrollArea = QtWidgets.QScrollArea(self.dark_task_centralwidget)
        self.dark_task_scrollArea.setWidgetResizable(True)
        self.dark_task_centralwidget.setStyleSheet(
"QWidget {"
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
        self.dark_task_scrollArea.setStyleSheet("background: #2f3136; border-radius: 7px;")
        self.dark_task_scrollAreaWidgetContents = QtWidgets.QWidget(self.dark_task_scrollArea)
        self.dark_task_scrollArea.setWidget(self.dark_task_scrollAreaWidgetContents)

        def dark_task_show_des_func(btn_info):
            self.task_show_widget = QtWidgets.QDialog()
            vertical_lay = QtWidgets.QVBoxLayout(self.task_show_widget)
            scroll_area = QtWidgets.QScrollArea(self.task_show_widget)
            scroll_area.setWidgetResizable(True)
            scroll_area_content = QtWidgets.QWidget(scroll_area)
            scroll_area.setWidget(scroll_area_content)
            scroll_area.setStyleSheet("background: #2f3136; border-radius: 7px;")
            form_lay = QtWidgets.QHBoxLayout(scroll_area_content)


            self.task_show_widget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.task_show_widget.resize(350, 220)
            self.task_show_widget.setMinimumSize(QtCore.QSize(350, 220))
            self.task_show_widget.setMaximumSize(QtCore.QSize(350, 220))
            self.task_show_widget.setStyleSheet("""
QDialog {
background-color: #36393f;
}
QLabel {
font-family: 'Titillium Web', sans-serif;
font-size: 30px;
}
QPushButton {
background-color: transparent;
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
            self.exit_btn = QtWidgets.QPushButton()
            self.exit_lay = QtWidgets.QHBoxLayout()
            self.exit_lay.addStretch(1)
            self.exit_lay.addWidget(self.exit_btn)
            self.exit_btn.setIcon(QtGui.QIcon(r".\Asserts\images\exit_icon"))
            self.exit_btn.setIconSize(QtCore.QSize(20, 20))
            self.exit_btn.setGeometry(QtCore.QRect(315, 5, 25, 25))
            self.exit_btn.clicked.connect(self.task_show_widget.accept)

            vertical_lay.addLayout(self.exit_lay)
            vertical_lay.addWidget(scroll_area)

            btn_info = btn_info[2]

            self.des_label = QtWidgets.QLabel()
            form_lay.addWidget(self.des_label)
            self.des_label.setText(f"Description:\n  {btn_info}")
            self.des_label.setGeometry(QtCore.QRect(10, 10, 300, 180))

            self.task_show_widget.exec_()

        self.dark_task_verticalLayout.addWidget(self.dark_task_scrollArea)

        self.dark_task_form_layout = QtWidgets.QFormLayout(self.dark_task_scrollAreaWidgetContents)
        self.dark_task_cond_lst = [r".\Asserts\images\unchecked.png", r".\Asserts\images\checked.png"]
        self.dark_task_cond = {}

        def dark_task_create_task_btn_func(btn, i, s):
            self.dark_task_cond[btn] = 0
            btn.setFixedSize(25,25)
            btn.setIcon(QtGui.QIcon(self.dark_task_cond_lst[self.dark_task_cond[btn]]))
            btn.setIconSize(QtCore.QSize(25,25))
            btn.setStyleSheet("""
QPushButton {
    background-color: transparent;
    font-size: 12px;
}
QPushButton:hover {
    background-color: #202225;
}
QPushButton:pressed {
    background-color: #18191c;
}
""")
            def task_switch():
                self.dark_task_cond[btn] = not self.dark_task_cond[btn]
                btn.setIcon(QtGui.QIcon(self.dark_task_cond_lst[self.dark_task_cond[btn]]))
            btn.clicked.connect(lambda: task_switch())

        dark_task_scroll_files()

        def dark_task_combo(index):
            self.task_sort = index
            dark_task_scroll_files()

        self.dark_task_sort_combo.activated.connect(dark_task_combo)

#<<<<<<<<<<<<<<<light task Window
        self.light_task_centralwidget = QtWidgets.QWidget(MainWindow)
        self.light_task_centralwidget.setFixedSize(430,500)
        self.light_task_verticalLayout = QtWidgets.QVBoxLayout(self.light_task_centralwidget)
        self.light_task_title_layout = QtWidgets.QHBoxLayout()

        def light_task_delete_action(s):
            del_task = TaskManager()
            print(del_task.delete_task(s[0]))
            light_task_scroll_files()

        def light_task_task_add_func(txt,s):
            self.txt =txt
            self.s = s
            self.files_set_DialogWindow = QtWidgets.QDialog()
            self.files_set_DialogWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.files_set_DialogWindow.resize(380, 350)
            self.files_set_DialogWindow.setStyleSheet("""
QDialog {
    background-color: #ffffff;
}
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 30px;
}
QPushButton {
    background-color: #e3e5e8;
    border-radius: 5px;
    font-family: 'Roboto Mono', monospace;
    font-size: 20px;
}
QPushButton:hover {
    background-color: #C9C9C9;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
QTextEdit{
    background-color: #ebedef;
    font-family: 'Cabin', sans-serif;
    font-size: 20px;
    border-radius: 5px;
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
            self.task_add_layout = QtWidgets.QVBoxLayout(self.files_set_DialogWindow)
            self.task_ok_layout = QtWidgets.QHBoxLayout()
            self.dialog_ok_btn = QtWidgets.QPushButton()
            if self.txt == "Add":
                self.dialog_ok_btn.setText("Add")
            else:
                self.dialog_ok_btn.setText("Save")

            self.dialog_cancel_btn = QtWidgets.QPushButton()
            self.dialog_cancel_btn.setText("Cancel")
            self.dialog_cancel_btn.clicked.connect(lambda: self.files_set_DialogWindow.reject())
            self.task_ok_layout.addWidget(self.dialog_ok_btn)
            self.task_ok_layout.addWidget(self.dialog_cancel_btn)

            self.dialog_label = QtWidgets.QLabel()
            self.dialog_label.setText(f"{self.txt} your Task")
            self.name_textEdit = QtWidgets.QTextEdit()
            self.name_textEdit.setPlaceholderText("Name")
            self.name_textEdit.setFixedHeight(40)

            self.desc_textedit = QtWidgets.QTextEdit()
            self.desc_textedit.setPlaceholderText("Description")
            self.desc_textedit.setFixedHeight(75)

            self.task_other_layout = QtWidgets.QHBoxLayout()
            self.task_priority_label = QtWidgets.QLabel("Priority")
            self.task_priority_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 20px;")
            self.task_priority_add = QtWidgets.QComboBox()
            self.task_priority_add.setFixedHeight(40)
            self.task_priority_add.addItems(["1", "2", "3", "4", "5"])

            self.task_priority_layout = QtWidgets.QVBoxLayout()
            self.task_priority_layout.addWidget(self.task_priority_label)
            self.task_priority_layout.addWidget(self.task_priority_add)
            self.task_other_layout.addLayout(self.task_priority_layout)

            self.task_add_layout.addWidget(self.dialog_label)
            self.task_add_layout.addWidget(self.name_textEdit)
            self.task_add_layout.addWidget(self.desc_textedit)
            self.task_add_layout.addLayout(self.task_other_layout)
            self.task_add_layout.addLayout(self.task_ok_layout)

            self.i = 1
            def add_clicked():
                name = self.name_textEdit.toPlainText()
                desc = self.desc_textedit.toPlainText()
                if name == "" or desc == "":
                        pass
                else:
                    task = TaskManager()
                    if self.txt == "Add":
                        print(task.insert_task(name, desc , self.i))
                    else:
                        print(task.edit_tasks(self.s[0], name, desc , self.i))
                    light_task_scroll_files()
                    self.files_set_DialogWindow.accept()

            self.dialog_ok_btn.clicked.connect(lambda: add_clicked())
            def combo_switch(index):
                self.i = index
                self.i += 1
                print(self.i)
            self.task_priority_add.activated.connect(combo_switch)

            self.files_set_DialogWindow.exec_()

        def light_task_scroll_files():
            task = TaskManager()
            if self.task_sort == 0:
                self.files = [[i[0],i[1].capitalize(),i[2]] for i in task.list_tasks()]
                self.files.reverse()
            elif self.task_sort == 1:
                self.files = [[i[3],i[1].capitalize(),i[2]] for i in task.list_tasks()]
                self.files.sort()
                self.files.reverse()
            else:
                self.files = [[i[0],i[1].lower(),i[2]] for i in task.list_tasks()]
                print(self.files)
                self.files = sorted(self.files, key=lambda x: x[1])
                self.files = [[i[0],i[1].capitalize(),i[2]] for i in self.files]

            self.light_task_scrollAreaWidgetContents.deleteLater()
            self.light_task_scrollAreaWidgetContents = QtWidgets.QWidget(self.light_task_scrollArea)
            self.light_task_scrollArea.setWidget(self.light_task_scrollAreaWidgetContents)
            self.light_task_form_layout = QtWidgets.QFormLayout(self.light_task_scrollAreaWidgetContents)

            for i,s in enumerate(self.files):
                light_task_scroll_btn_layout = QtWidgets.QHBoxLayout()
                light_task_checked_btn = QtWidgets.QPushButton()
                light_task_create_task_btn_func(light_task_checked_btn, i, s)
                light_task_scroll_btn_layout.addWidget(light_task_checked_btn)
                light_task_main_btn = QPushButton(self.files[i][1])
                light_task_main_btn.setFixedSize(250,60)
                light_task_main_btn.setStyleSheet(
'''
QPushButton {
    background-color: #e3e5e8;
    font-family: 'Roboto Mono', monospace;
    font-size: 20px;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    border-top-right-radius: 0px;
    border-bottom-right-radius: 0px;
}
QPushButton:hover {
    background-color: #C9C9C9;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
''')
                light_task_main_btn.clicked.connect(lambda checked, btn_text=s:light_task_show_des_func(btn_text))
                light_task_edit_btn = QPushButton()   #39DFA2
                light_task_edit_btn.setIcon(QtGui.QIcon(r".\Asserts\images\edit_icon.png"))
                light_task_edit_btn.setIconSize(QtCore.QSize(28, 28))
                light_task_edit_btn.setFixedSize(30,60)
                light_task_edit_btn.clicked.connect(lambda checked, s=s: light_task_task_add_func("Edit",s))
                light_task_edit_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-radius: 0px;
}
QPushButton:hover {
    background-color: #e3e5e8;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
''')
                light_task_del_btn = QPushButton()
                light_task_del_btn.setIcon(QtGui.QIcon(r".\Asserts\images/del_icon.png"))
                light_task_del_btn.setIconSize(QtCore.QSize(28, 28))
                light_task_del_btn.setFixedSize(30,60)
                light_task_del_btn.clicked.connect(lambda checked, s=s: light_task_delete_action(s))
                light_task_del_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-top-left-radius: 0;
    border-bottom-left-radius: 00px;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
}
QPushButton:hover {
    background-color: #e3e5e8;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
''')
                light_task_scroll_btn_layout.addWidget(light_task_main_btn)
                light_task_scroll_btn_layout.addWidget(light_task_edit_btn)
                light_task_scroll_btn_layout.addWidget(light_task_del_btn)
                self.light_task_form_layout.addRow(light_task_scroll_btn_layout)
        self.light_task_home_btn = QtWidgets.QPushButton()
        self.light_task_home_btn.setIcon(QtGui.QIcon(r".\Asserts\images\home"))
        self.light_task_home_btn.setIconSize(QtCore.QSize(25, 25))
        self.light_task_home_btn.setFixedSize(40,40)
        self.light_task_home_btn.setStyleSheet(
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

        self.light_task_title_label = QtWidgets.QLabel("      Robert Task")
        self.light_task_title_label.setStyleSheet(
'''
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
''')
        self.light_task_title_layout = QtWidgets.QHBoxLayout()
        self.light_task_title_layout.addWidget(self.light_task_home_btn)
        self.light_task_title_layout.addWidget(self.light_task_title_label)

        self.light_task_task_addcode_btn = QtWidgets.QPushButton()
        self.light_task_task_addcode_btn.setIcon(QtGui.QIcon(r".\Asserts\images\add_btn.png"))
        self.light_task_task_addcode_btn.setIconSize(QtCore.QSize(40, 40))
        self.light_task_task_addcode_btn.setFixedSize(70,50)
        self.light_task_task_addcode_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-radius: 12px;
}
QPushButton:hover {
    background-color: #e3e5e8;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
''')
        self.light_task_verticalLayout.addLayout(self.light_task_title_layout)
        self.light_task_task_addcode_btn.clicked.connect(lambda checked, t="Add",s="J":light_task_task_add_func(t,s))
        self.light_task_second_layout = QtWidgets.QHBoxLayout()

        task_sort_combo_lst = ["Newest", "Priority", "Alphabet"]

        self.light_task_sort_combo = QtWidgets.QComboBox()
        self.light_task_sort_combo.setFixedSize(200,30)
        self.light_task_sort_combo.addItems(task_sort_combo_lst)
        self.light_task_sort_combo.setStyleSheet(
'''
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
'''
)
        self.light_task_sort_label = QtWidgets.QLabel("Sort by")
        self.light_task_sort_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
        self.light_task_sort_layout = QtWidgets.QVBoxLayout()
        self.light_task_sort_layout.addWidget(self.light_task_sort_label)
        self.light_task_sort_layout.addWidget(self.light_task_sort_combo)
        self.light_task_second_layout.addLayout(self.light_task_sort_layout)
        self.light_task_second_layout.addStretch(20)
        self.light_task_second_layout.addWidget(self.light_task_task_addcode_btn)

        self.light_task_verticalLayout.addLayout(self.light_task_second_layout)
        self.light_task_scrollArea = QtWidgets.QScrollArea(self.light_task_centralwidget)
        self.light_task_scrollArea.setWidgetResizable(True)
        self.light_task_centralwidget.setStyleSheet(
"QWidget {"
"   background: #ffffff;"
"}"
"QScrollArea {"
"background-color: #f2f3f5"
"}"
"/* VERTICAL SCROLLBAR */"
" QScrollBar:vertical {"
"    border: none;"
"    background: #e3e5e8;"
"    width: 14px;"
"    margin: 15px 0 15px 0;"
"    "
" }"
""
"/*  HANDLE BAR VERTICAL */"
"QScrollBar::handle:vertical {    "
"    background-color: #D0D0D0;"
"    min-height: 30px;"
"    "
"}"
"QScrollBar::handle:vertical:hover{    "
"    background-color: #B7B7B7;"
"}"
"QScrollBar::handle:vertical:pressed {    "
"    background-color: #A9A9A9;"
"}"
""
"/* BTN TOP - SCROLLBAR */"
"QScrollBar::sub-line:vertical {"
"    border: none;"
"    background-color: #D0D0D0;"
"    height: 15px;"
"    border-top-left-radius: 7px;"
"    border-top-right-radius: 7px;"
"    subcontrol-position: top;"
"    subcontrol-origin: margin;"
"}"
"QScrollBar::sub-line:vertical:hover {    "
"    background-color: #B7B7B7;"
"}"
"QScrollBar::sub-line:vertical:pressed {    "
"    background-color: #A9A9A9;"
"}"
""
"/* BTN BOTTOM - SCROLLBAR */"
"QScrollBar::add-line:vertical {"
"    border: none;"
"    background-color: #D0D0D0;"
"    height: 15px;"
"    border-bottom-left-radius: 7px;"
"    border-bottom-right-radius: 7px;"
"    subcontrol-position: bottom;"
"    subcontrol-origin: margin;"
"}"
"QScrollBar::add-line:vertical:hover {    "
"    background-color: #B7B7B7;"
"}"
"QScrollBar::add-line:vertical:pressed {    "
"    background-color: #A9A9A9;"
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
        self.light_task_scrollArea.setStyleSheet("background-color: #f2f3f5; border-radius: 7px;")
        self.light_task_scrollAreaWidgetContents = QtWidgets.QWidget(self.light_task_scrollArea)
        self.light_task_scrollArea.setWidget(self.light_task_scrollAreaWidgetContents)

        def light_task_show_des_func(btn_info):
            self.task_show_widget = QtWidgets.QDialog()
            vertical_lay = QtWidgets.QVBoxLayout(self.task_show_widget)
            scroll_area = QtWidgets.QScrollArea(self.task_show_widget)
            scroll_area.setWidgetResizable(True)
            scroll_area_content = QtWidgets.QWidget(scroll_area)
            scroll_area.setWidget(scroll_area_content)
            scroll_area.setStyleSheet("background-color: #f2f3f5; border-radius: 7px;")
            form_lay = QtWidgets.QHBoxLayout(scroll_area_content)

            self.task_show_widget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.task_show_widget.resize(350, 220)
            self.task_show_widget.setMinimumSize(QtCore.QSize(350, 220))
            self.task_show_widget.setMaximumSize(QtCore.QSize(350, 220))
            self.task_show_widget.setStyleSheet("""
QDialog {
    background-color: #ffffff;
}
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 30px;
}
QPushButton {
    background-color: transparent;
    border-radius: 5px;
    font-family: 'Roboto Mono', monospace;
    font-size: 20px;
}
QPushButton:hover {
    background-color: #C9C9C9;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
""")
            self.exit_btn = QtWidgets.QPushButton()
            self.exit_lay = QtWidgets.QHBoxLayout()
            self.exit_lay.addStretch(1)
            self.exit_lay.addWidget(self.exit_btn)
            self.exit_btn.setIcon(QtGui.QIcon(r".\Asserts\images\exit_icon"))
            self.exit_btn.setIconSize(QtCore.QSize(20, 20))
            self.exit_btn.setGeometry(QtCore.QRect(315, 5, 25, 25))
            self.exit_btn.clicked.connect(self.task_show_widget.accept)

            vertical_lay.addLayout(self.exit_lay)
            vertical_lay.addWidget(scroll_area)

            btn_info = btn_info[2]

            self.des_label = QtWidgets.QLabel()
            form_lay.addWidget(self.des_label)
            self.des_label.setText(f"Description:\n  {btn_info}")
            self.des_label.setGeometry(QtCore.QRect(10, 10, 300, 180))

            self.task_show_widget.exec_()

        self.light_task_verticalLayout.addWidget(self.light_task_scrollArea)

        self.light_task_form_layout = QtWidgets.QFormLayout(self.light_task_scrollAreaWidgetContents)
        self.light_task_cond_lst = [r".\Asserts\images\unchecked.png", r".\Asserts\images\checked.png"]
        self.light_task_cond = {}

        def light_task_create_task_btn_func(btn, i, s):
            self.light_task_cond[btn] = 0
            btn.setFixedSize(25,25)
            btn.setIcon(QtGui.QIcon(self.light_task_cond_lst[self.light_task_cond[btn]]))
            btn.setIconSize(QtCore.QSize(25,25))
            btn.setStyleSheet("""
QPushButton {
    background-color: transparent;
    font-size: 12px;
}
QPushButton:hover {
    background-color: #e3e5e8;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
""")
            def task_switch():
                self.light_task_cond[btn] = not self.light_task_cond[btn]
                btn.setIcon(QtGui.QIcon(self.light_task_cond_lst[self.light_task_cond[btn]]))
            btn.clicked.connect(lambda: task_switch())

        light_task_scroll_files()

        def light_task_combo(index):
            self.task_sort = index
            light_task_scroll_files()

        self.light_task_sort_combo.activated.connect(light_task_combo)
#<<<<<<<<<<<<<<<dark alarm Window
        self.dark_alarm_centralwidget = QtWidgets.QWidget(MainWindow)
        self.dark_alarm_centralwidget.setFixedSize(430,500)
        self.dark_alarm_verticalLayout = QtWidgets.QVBoxLayout(self.dark_alarm_centralwidget)

        self.dark_alarm_home_btn = QtWidgets.QPushButton()
        self.dark_alarm_home_btn.setIcon(QtGui.QIcon(r".\Asserts\images\home"))
        self.dark_alarm_home_btn.setIconSize(QtCore.QSize(25, 25))
        self.dark_alarm_home_btn.setFixedSize(40,40)
        self.dark_alarm_home_btn.setStyleSheet(
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

        self.dark_alarm_title_label = QtWidgets.QLabel(" Robert Alarm")
        self.dark_alarm_title_label.setStyleSheet(
'''
QLabel {
    color: #FFFFFF;
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
''')
        self.dark_alarm_title_layout = QtWidgets.QHBoxLayout()
        self.dark_alarm_title_layout.addWidget(self.dark_alarm_home_btn)
        self.dark_alarm_title_layout.addWidget(self.dark_alarm_title_label)


        self.dark_alarm_addcode_btn = QtWidgets.QPushButton()
        self.dark_alarm_addcode_btn.setIcon(QtGui.QIcon(r".\Asserts\images\add_btn.png"))
        self.dark_alarm_addcode_btn.setIconSize(QtCore.QSize(40, 40))
        self.dark_alarm_addcode_btn.setFixedSize(70,50)
        self.dark_alarm_addcode_btn.setStyleSheet(
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
        self.dark_alarm_title_layout.addWidget(self.dark_alarm_addcode_btn)
        self.dark_alarm_verticalLayout.addLayout(self.dark_alarm_title_layout)
#-----------------alarm adding window------------------------------------------------
        def dark_alarm_add_window(txt):
            self.files_set_DialogWindow = QtWidgets.QDialog()
            self.files_set_DialogWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.files_set_DialogWindow.resize(400, 300)
            #self.files_set_DialogWindow.setMinimumSize(QtCore.QSize(480, 300))
            #self.files_set_DialogWindow.setMaximumSize(QtCore.QSize(480, 300))
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
QSpinBox {
    color: #FFFFFF;
	background-color: #2f3136;
    font-size: 15px;
	border-radius: 5px;
	padding: 5px;
	padding-left: 10px;
}
QSpinBox QAbstractItemView {
	color: #FFFFFF;
	background-color: #2f3136;
	padding: 10px;
	selection-background-color: #40444b;
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
            self.alarm_add_layout = QtWidgets.QVBoxLayout(self.files_set_DialogWindow)
            self.alarm_ok_layout = QtWidgets.QHBoxLayout()
            self.dialog_ok_btn = QtWidgets.QPushButton(s)
            if txt == "Add":
                self.dialog_ok_btn.setText("Add")
            else:
                self.dialog_ok_btn.setText("Save")
            self.dialog_cancel_btn = QtWidgets.QPushButton()
            self.dialog_cancel_btn.setText("Cancel")
            self.dialog_cancel_btn.clicked.connect(lambda: self.files_set_DialogWindow.reject())
            self.alarm_ok_layout.addWidget(self.dialog_ok_btn)
            self.alarm_ok_layout.addWidget(self.dialog_cancel_btn)

            self.dialog_textEdit = QtWidgets.QTextEdit()
            self.dialog_textEdit.setPlaceholderText("Name")
            self.dialog_textEdit.setFixedHeight(50)
            self.dialog_label = QtWidgets.QLabel()
            self.dialog_label.setText(f"{txt} your Alarm")

            self.alarm_hour_add = QtWidgets.QSpinBox()
            self.alarm_hour_add.setRange(1,12)
            self.alarm_minute_add = QtWidgets.QSpinBox()
            self.alarm_minute_add.setRange(0,59)

            self.alarm_time_add_layout = QtWidgets.QHBoxLayout()
            self.alarm_hour_layout = QtWidgets.QVBoxLayout()
            self.alarm_minute_layout = QtWidgets.QVBoxLayout()

            self.alarm_hour_label = QtWidgets.QLabel()
            self.alarm_hour_label.setText("Hour")
            self.alarm_hour_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
            self.alarm_minute_label = QtWidgets.QLabel()
            self.alarm_minute_label.setText("Minute")
            self.alarm_minute_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")

            self.alarm_hour_layout.addWidget(self.alarm_hour_label)
            self.alarm_hour_layout.addWidget(self.alarm_hour_add)
            self.alarm_minute_layout.addWidget(self.alarm_minute_label)
            self.alarm_minute_layout.addWidget(self.alarm_minute_add)

            self.alarm_mid_group = QtWidgets.QComboBox()
            self.alarm_mid_group.addItems(["AM", "PM"])


            self.alarm_time_add_layout.addLayout(self.alarm_hour_layout)
            self.alarm_time_add_layout.addLayout(self.alarm_minute_layout)
            self.alarm_mid_group_layout = QtWidgets.QVBoxLayout()
            self.alarm_mid_group_layout.addStretch(2)
            self.alarm_mid_group_layout.addWidget(self.alarm_mid_group)
            self.alarm_time_add_layout.addLayout(self.alarm_mid_group_layout)

            self.alarm_other_layout = QtWidgets.QHBoxLayout()
            self.alarm_repeats_label = QtWidgets.QLabel("Repeats")
            self.alarm_repeats_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
            self.alarm_sound_label = QtWidgets.QLabel("Sound")
            self.alarm_sound_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
            self.alarm_repeats_add = QtWidgets.QComboBox()
            self.alarm_repeats_add.addItems(["Only Once", "Every day", "Every week", "Every Month"])
            self.alarm_sound_add = QtWidgets.QComboBox()
            self.alarm_sound_add.addItems(["sound A", "sound B", "sound C", "sound D", "sound E"])

            self.alarm_repeats_layout = QtWidgets.QVBoxLayout()
            self.alarm_repeats_layout.addWidget(self.alarm_repeats_label)
            self.alarm_repeats_layout.addWidget(self.alarm_repeats_add)
            self.alarm_sound_layout = QtWidgets.QVBoxLayout()
            self.alarm_sound_layout.addWidget(self.alarm_sound_label)
            self.alarm_sound_layout.addWidget(self.alarm_sound_add)

            self.alarm_other_layout.addLayout(self.alarm_repeats_layout)
            self.alarm_other_layout.addLayout(self.alarm_sound_layout)


            self.alarm_add_layout.addWidget(self.dialog_label)
            self.alarm_add_layout.addWidget(self.dialog_textEdit)
            self.alarm_add_layout.addLayout(self.alarm_time_add_layout)
            self.alarm_add_layout.addLayout(self.alarm_other_layout)
            self.alarm_add_layout.addLayout(self.alarm_ok_layout)

            self.files_set_DialogWindow.exec_()

#-----------------end of code adding--------------------------------------
        self.dark_alarm_addcode_btn.clicked.connect(lambda : dark_alarm_add_window("Add"))
        self.dark_alarm_scroll_Area = QtWidgets.QScrollArea(self.dark_alarm_centralwidget)
        self.dark_alarm_scroll_Area.setWidgetResizable(True)
        self.dark_alarm_centralwidget.setStyleSheet(
"QWidget {"
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
        self.dark_alarm_scroll_Area.setStyleSheet("background: #2f3136; border-radius: 7px;")
        self.dark_alarm_scroll_AreaWidgetContents = QtWidgets.QWidget(self.dark_alarm_scroll_Area)
        self.dark_alarm_scroll_Area.setWidget(self.dark_alarm_scroll_AreaWidgetContents)

        self.dark_alarm_verticalLayout.addWidget(self.dark_alarm_scroll_Area)

        self.dark_alarm_scrollArea_formLayout = QtWidgets.QFormLayout(self.dark_alarm_scroll_AreaWidgetContents)
        self.dark_alarm_cond_lst = [r".\Asserts\images\off.png", r".\Asserts\images\on.png"]
        self.dark_alarm_cond_text = ["Off", "On"]
        self.dark_alarm_cond = {}
        def dark_alarm_create_alarm_btn(btn, i, s):
            self.dark_alarm_cond[btn] = 0
            btn.setFixedSize(60,35)
            btn.setIcon(QtGui.QIcon(self.dark_alarm_cond_lst[self.dark_alarm_cond[btn]]))
            btn.setIconSize(QtCore.QSize(40,35))
            btn.setText(self.dark_alarm_cond_text[self.dark_alarm_cond[btn]])
            btn.setStyleSheet("""
QPushButton {
    background-color: transparent;
    font-size: 12px;
}
QPushButton:hover {
    background-color: #202225;
}
QPushButton:pressed {
    background-color: #18191c;
}
""")
            def alarm_switch():
                self.dark_alarm_cond[btn] = not self.dark_alarm_cond[btn]
                btn.setIcon(QtGui.QIcon(self.dark_alarm_cond_lst[self.dark_alarm_cond[btn]]))
                btn.setText(self.dark_alarm_cond_text[self.dark_alarm_cond[btn]])
            btn.clicked.connect(lambda: alarm_switch())

        for i,s in enumerate(files):
            dark_alarm_create_scroll_btn_layout = QtWidgets.QHBoxLayout()
            dark_alarm_switch_btn = QtWidgets.QPushButton()
            dark_alarm_create_alarm_btn(dark_alarm_switch_btn, i, s)

            dark_alarm_main_btn = QtWidgets.QLabel()
            dark_alarm_main_btn.setFixedSize(240,60)
            dark_alarm_main_btn.setText(files[i])
            dark_alarm_main_btn.setAlignment(QtCore.Qt.AlignCenter)
            dark_alarm_main_btn.setStyleSheet(
'''
QLabel {
    color: #FFFFFF;
    background-color: #37393D;
    font-family: 'Roboto Mono', monospace;
    font-size: 20px;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    border-top-right-radius: 0px;
    border-bottom-right-radius: 0px;
}
''')

            dark_alarm_edit_btn = QtWidgets.QPushButton()   #39DFA2
            dark_alarm_edit_btn.setIcon(QtGui.QIcon(r".\Asserts\images\edit_icon.png"))
            dark_alarm_edit_btn.setIconSize(QtCore.QSize(28, 28))
            dark_alarm_edit_btn.setFixedSize(30,60)
            dark_alarm_edit_btn.setStyleSheet(
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
            dark_alarm_edit_btn.clicked.connect(lambda : dark_alarm_add_window("Edit"))

            dark_alarm_del_btn = QtWidgets.QPushButton()
            dark_alarm_del_btn.setIcon(QtGui.QIcon(r".\Asserts\images\del_icon.png"))
            dark_alarm_del_btn.setIconSize(QtCore.QSize(28, 28))
            dark_alarm_del_btn.setFixedSize(30,60)   #39DFA2
            dark_alarm_del_btn.setStyleSheet(
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
            dark_alarm_create_scroll_btn_layout.addWidget(dark_alarm_switch_btn)
            dark_alarm_create_scroll_btn_layout.addWidget(dark_alarm_main_btn)
            dark_alarm_create_scroll_btn_layout.addWidget(dark_alarm_edit_btn)
            dark_alarm_create_scroll_btn_layout.addWidget(dark_alarm_del_btn)
            self.dark_alarm_scrollArea_formLayout.addRow(dark_alarm_create_scroll_btn_layout)

#<<<<<<<<<<<<<<<light alarm Window

        self.light_alarm_centralwidget = QtWidgets.QWidget(MainWindow)
        self.light_alarm_centralwidget.setFixedSize(430,500)
        self.light_alarm_verticalLayout = QtWidgets.QVBoxLayout(self.light_alarm_centralwidget)

        self.light_alarm_home_btn = QtWidgets.QPushButton()
        self.light_alarm_home_btn.setIcon(QtGui.QIcon(r".\Asserts\images\home"))
        self.light_alarm_home_btn.setIconSize(QtCore.QSize(25, 25))
        self.light_alarm_home_btn.setFixedSize(40,40)
        self.light_alarm_home_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #e3e5e8;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
''')

        self.light_alarm_title_label = QtWidgets.QLabel(" Robert Alarm")
        self.light_alarm_title_label.setStyleSheet(
'''
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
''')
        self.light_alarm_title_layout = QtWidgets.QHBoxLayout()
        self.light_alarm_title_layout.addWidget(self.light_alarm_home_btn)
        self.light_alarm_title_layout.addWidget(self.light_alarm_title_label)


        self.light_alarm_addcode_btn = QtWidgets.QPushButton()
        self.light_alarm_addcode_btn.setIcon(QtGui.QIcon(r".\Asserts\images\add_btn.png"))
        self.light_alarm_addcode_btn.setIconSize(QtCore.QSize(40, 40))
        self.light_alarm_addcode_btn.setFixedSize(70,50)
        self.light_alarm_addcode_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-radius: 12px;
}
QPushButton:hover {
    background-color: #ebedef;
}
QPushButton:pressed {
    background-color: #e3e5e8;
}
''')
        self.light_alarm_title_layout.addWidget(self.light_alarm_addcode_btn)
        self.light_alarm_verticalLayout.addLayout(self.light_alarm_title_layout)
#-----------------alarm adding window------------------------------------------------
        def light_alarm_add_window(txt):
            self.files_set_DialogWindow = QtWidgets.QDialog()
            self.files_set_DialogWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.files_set_DialogWindow.resize(400, 300)
            #self.files_set_DialogWindow.setMinimumSize(QtCore.QSize(480, 300))
            #self.files_set_DialogWindow.setMaximumSize(QtCore.QSize(480, 300))
            self.files_set_DialogWindow.setStyleSheet("""
QDialog {
    background-color: #ffffff;
}
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 30px;
}
QPushButton {
    background-color: #e3e5e8;
    border-radius: 5px;
    font-family: 'Roboto Mono', monospace;
    font-size: 20px;
}
QPushButton:hover {
    background-color: #C9C9C9;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
QTextEdit{
    background-color: #ebedef;
    font-family: 'Cabin', sans-serif;
    font-size: 20px;
    border-radius: 5px;
}
QSpinBox {
    background-color: #e3e5e8;
    font-size: 15px;
	border-radius: 5px;
	padding: 5px;
	padding-left: 10px;
}
QSpinBox QAbstractItemView {
	color: #000000;
	background-color: #e3e5e8;
	padding: 10px;
	selection-background-color: #e3e5e8;
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
            self.alarm_add_layout = QtWidgets.QVBoxLayout(self.files_set_DialogWindow)
            self.alarm_ok_layout = QtWidgets.QHBoxLayout()
            self.dialog_ok_btn = QtWidgets.QPushButton(s)
            if txt == "Add":
                self.dialog_ok_btn.setText("Add")
            else:
                self.dialog_ok_btn.setText("Save")
            self.dialog_cancel_btn = QtWidgets.QPushButton()
            self.dialog_cancel_btn.setText("Cancel")
            self.dialog_cancel_btn.clicked.connect(lambda: self.files_set_DialogWindow.reject())
            self.alarm_ok_layout.addWidget(self.dialog_ok_btn)
            self.alarm_ok_layout.addWidget(self.dialog_cancel_btn)

            self.dialog_textEdit = QtWidgets.QTextEdit()
            self.dialog_textEdit.setPlaceholderText("Name")
            self.dialog_textEdit.setFixedHeight(50)
            self.dialog_label = QtWidgets.QLabel()
            self.dialog_label.setText(f"{txt} your Alarm")

            self.alarm_hour_add = QtWidgets.QSpinBox()
            self.alarm_hour_add.setRange(1,12)
            self.alarm_minute_add = QtWidgets.QSpinBox()
            self.alarm_minute_add.setRange(0,59)

            self.alarm_time_add_layout = QtWidgets.QHBoxLayout()
            self.alarm_hour_layout = QtWidgets.QVBoxLayout()
            self.alarm_minute_layout = QtWidgets.QVBoxLayout()

            self.alarm_hour_label = QtWidgets.QLabel()
            self.alarm_hour_label.setText("Hour")
            self.alarm_hour_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
            self.alarm_minute_label = QtWidgets.QLabel()
            self.alarm_minute_label.setText("Minute")
            self.alarm_minute_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")

            self.alarm_hour_layout.addWidget(self.alarm_hour_label)
            self.alarm_hour_layout.addWidget(self.alarm_hour_add)
            self.alarm_minute_layout.addWidget(self.alarm_minute_label)
            self.alarm_minute_layout.addWidget(self.alarm_minute_add)

            self.alarm_mid_group = QtWidgets.QComboBox()
            self.alarm_mid_group.addItems(["AM", "PM"])


            self.alarm_time_add_layout.addLayout(self.alarm_hour_layout)
            self.alarm_time_add_layout.addLayout(self.alarm_minute_layout)
            self.alarm_mid_group_layout = QtWidgets.QVBoxLayout()
            self.alarm_mid_group_layout.addStretch(2)
            self.alarm_mid_group_layout.addWidget(self.alarm_mid_group)
            self.alarm_time_add_layout.addLayout(self.alarm_mid_group_layout)

            self.alarm_other_layout = QtWidgets.QHBoxLayout()
            self.alarm_repeats_label = QtWidgets.QLabel("Repeats")
            self.alarm_repeats_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
            self.alarm_sound_label = QtWidgets.QLabel("Sound")
            self.alarm_sound_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
            self.alarm_repeats_add = QtWidgets.QComboBox()
            self.alarm_repeats_add.addItems(["Only Once", "Every day", "Every week", "Every Month"])
            self.alarm_sound_add = QtWidgets.QComboBox()
            self.alarm_sound_add.addItems(["sound A", "sound B", "sound C", "sound D", "sound E"])

            self.alarm_repeats_layout = QtWidgets.QVBoxLayout()
            self.alarm_repeats_layout.addWidget(self.alarm_repeats_label)
            self.alarm_repeats_layout.addWidget(self.alarm_repeats_add)
            self.alarm_sound_layout = QtWidgets.QVBoxLayout()
            self.alarm_sound_layout.addWidget(self.alarm_sound_label)
            self.alarm_sound_layout.addWidget(self.alarm_sound_add)

            self.alarm_other_layout.addLayout(self.alarm_repeats_layout)
            self.alarm_other_layout.addLayout(self.alarm_sound_layout)


            self.alarm_add_layout.addWidget(self.dialog_label)
            self.alarm_add_layout.addWidget(self.dialog_textEdit)
            self.alarm_add_layout.addLayout(self.alarm_time_add_layout)
            self.alarm_add_layout.addLayout(self.alarm_other_layout)
            self.alarm_add_layout.addLayout(self.alarm_ok_layout)

            self.files_set_DialogWindow.exec_()

#-----------------end of code adding--------------------------------------
        self.light_alarm_addcode_btn.clicked.connect(lambda : light_alarm_add_window("Add"))
        self.light_alarm_scroll_Area = QtWidgets.QScrollArea(self.light_alarm_centralwidget)
        self.light_alarm_scroll_Area.setWidgetResizable(True)
        self.light_alarm_centralwidget.setStyleSheet(
"QWidget {"
"   background: #ffffff;"
"}"
"QScrollArea {"
"background-color: #f2f3f5"
"}"
"/* VERTICAL SCROLLBAR */"
" QScrollBar:vertical {"
"    border: none;"
"    background: #e3e5e8;"
"    width: 14px;"
"    margin: 15px 0 15px 0;"
"    "
" }"
""
"/*  HANDLE BAR VERTICAL */"
"QScrollBar::handle:vertical {    "
"    background-color: #D0D0D0;"
"    min-height: 30px;"
"    "
"}"
"QScrollBar::handle:vertical:hover{    "
"    background-color: #B7B7B7;"
"}"
"QScrollBar::handle:vertical:pressed {    "
"    background-color: #A9A9A9;"
"}"
""
"/* BTN TOP - SCROLLBAR */"
"QScrollBar::sub-line:vertical {"
"    border: none;"
"    background-color: #D0D0D0;"
"    height: 15px;"
"    border-top-left-radius: 7px;"
"    border-top-right-radius: 7px;"
"    subcontrol-position: top;"
"    subcontrol-origin: margin;"
"}"
"QScrollBar::sub-line:vertical:hover {    "
"    background-color: #B7B7B7;"
"}"
"QScrollBar::sub-line:vertical:pressed {    "
"    background-color: #A9A9A9;"
"}"
""
"/* BTN BOTTOM - SCROLLBAR */"
"QScrollBar::add-line:vertical {"
"    border: none;"
"    background-color: #D0D0D0;"
"    height: 15px;"
"    border-bottom-left-radius: 7px;"
"    border-bottom-right-radius: 7px;"
"    subcontrol-position: bottom;"
"    subcontrol-origin: margin;"
"}"
"QScrollBar::add-line:vertical:hover {    "
"    background-color: #B7B7B7;"
"}"
"QScrollBar::add-line:vertical:pressed {    "
"    background-color: #A9A9A9;"
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
        self.light_alarm_scroll_Area.setStyleSheet("background: #f2f3f5; border-radius: 7px;")
        self.light_alarm_scroll_AreaWidgetContents = QtWidgets.QWidget(self.light_alarm_scroll_Area)
        self.light_alarm_scroll_Area.setWidget(self.light_alarm_scroll_AreaWidgetContents)

        self.light_alarm_verticalLayout.addWidget(self.light_alarm_scroll_Area)

        self.light_alarm_scrollArea_formLayout = QtWidgets.QFormLayout(self.light_alarm_scroll_AreaWidgetContents)
        self.light_alarm_cond_lst = [r".\Asserts\images\off.png", r".\Asserts\images\on.png"]
        self.light_alarm_cond_text = ["Off", "On"]
        self.light_alarm_cond = {}
        def light_alarm_create_alarm_btn(btn, i, s):
            self.light_alarm_cond[btn] = 0
            btn.setFixedSize(60,35)
            btn.setIcon(QtGui.QIcon(self.light_alarm_cond_lst[self.light_alarm_cond[btn]]))
            btn.setIconSize(QtCore.QSize(40,35))
            btn.setText(self.light_alarm_cond_text[self.light_alarm_cond[btn]])
            btn.setStyleSheet("""
QPushButton {
    background-color: transparent;
    font-size: 12px;
}
QPushButton:hover {
    background-color: #e3e5e8;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
""")
            def alarm_switch():
                self.light_alarm_cond[btn] = not self.light_alarm_cond[btn]
                btn.setIcon(QtGui.QIcon(self.light_alarm_cond_lst[self.light_alarm_cond[btn]]))
                btn.setText(self.light_alarm_cond_text[self.light_alarm_cond[btn]])
            btn.clicked.connect(lambda: alarm_switch())

        for i,s in enumerate(files):
            light_alarm_create_scroll_btn_layout = QtWidgets.QHBoxLayout()
            light_alarm_switch_btn = QtWidgets.QPushButton()
            light_alarm_create_alarm_btn(light_alarm_switch_btn, i, s)

            light_alarm_main_btn = QtWidgets.QPushButton()
            light_alarm_main_btn.setFixedSize(240,60)
            light_alarm_main_btn.setText(files[i])
            light_alarm_main_btn.setStyleSheet(
'''
QPushButton {
    background-color: #e3e5e8;
    font-family: 'Roboto Mono', monospace;
    font-size: 20px;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    border-top-right-radius: 0px;
    border-bottom-right-radius: 0px;
}
QPushButton:hover {
    background-color: #C9C9C9;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
''')

            light_alarm_edit_btn = QtWidgets.QPushButton()   #39DFA2
            light_alarm_edit_btn.setIcon(QtGui.QIcon(r".\Asserts\images\edit_icon.png"))
            light_alarm_edit_btn.setIconSize(QtCore.QSize(28, 28))
            light_alarm_edit_btn.setFixedSize(30,60)
            light_alarm_edit_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-radius: 0px;
}
QPushButton:hover {
    background-color: #e3e5e8;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
''')
            light_alarm_edit_btn.clicked.connect(lambda : light_alarm_add_window("Edit"))

            light_alarm_del_btn = QtWidgets.QPushButton()
            light_alarm_del_btn.setIcon(QtGui.QIcon(r".\Asserts\images/del_icon.png"))
            light_alarm_del_btn.setIconSize(QtCore.QSize(28, 28))
            light_alarm_del_btn.setFixedSize(30,60)   #39DFA2
            light_alarm_del_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-top-left-radius: 0;
    border-bottom-left-radius: 00px;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
}
QPushButton:hover {
    background-color: #e3e5e8;
}
QPushButton:pressed {
    background-color: #A2A2A2;
}
''')
            light_alarm_create_scroll_btn_layout.addWidget(light_alarm_switch_btn)
            light_alarm_create_scroll_btn_layout.addWidget(light_alarm_main_btn)
            light_alarm_create_scroll_btn_layout.addWidget(light_alarm_edit_btn)
            light_alarm_create_scroll_btn_layout.addWidget(light_alarm_del_btn)
            self.light_alarm_scrollArea_formLayout.addRow(light_alarm_create_scroll_btn_layout)

#<<<<<<<<<<<<<<<green alarm Window

        self.green_alarm_centralwidget = QtWidgets.QWidget(MainWindow)
        self.green_alarm_centralwidget.setFixedSize(430,500)
        self.green_alarm_verticalLayout = QtWidgets.QVBoxLayout(self.green_alarm_centralwidget)

        self.green_alarm_home_btn = QtWidgets.QPushButton()
        self.green_alarm_home_btn.setIcon(QtGui.QIcon(r".\Asserts\images\home"))
        self.green_alarm_home_btn.setIconSize(QtCore.QSize(25, 25))
        self.green_alarm_home_btn.setFixedSize(40,40)
        self.green_alarm_home_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #24E29D;
}
QPushButton:pressed {
    background-color: #1A4E3B;
}
''')

        self.green_alarm_title_label = QtWidgets.QLabel(" Robert Alarm")
        self.green_alarm_title_label.setStyleSheet(
'''
QLabel {
    font-family: 'Titillium Web', sans-serif;
    font-size: 40px;
}
''')
        self.green_alarm_title_layout = QtWidgets.QHBoxLayout()
        self.green_alarm_title_layout.addWidget(self.green_alarm_home_btn)
        self.green_alarm_title_layout.addWidget(self.green_alarm_title_label)


        self.green_alarm_addcode_btn = QtWidgets.QPushButton()
        self.green_alarm_addcode_btn.setIcon(QtGui.QIcon(r".\Asserts\images\add_btn.png"))
        self.green_alarm_addcode_btn.setIconSize(QtCore.QSize(40, 40))
        self.green_alarm_addcode_btn.setFixedSize(70,50)
        self.green_alarm_addcode_btn.setStyleSheet(
'''
QPushButton {
    background-color: transparent;
    border-radius: 12px;
}
QPushButton:hover {
    background-color: #24E29D;
}
QPushButton:pressed {
    background-color: #1A4E3B;
}
''')
        self.green_alarm_title_layout.addWidget(self.green_alarm_addcode_btn)
        self.green_alarm_verticalLayout.addLayout(self.green_alarm_title_layout)
#-----------------alarm adding window------------------------------------------------
        def green_alarm_add_window(txt):
            self.files_set_DialogWindow = QtWidgets.QDialog()
            self.files_set_DialogWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.files_set_DialogWindow.resize(400, 300)
            #self.files_set_DialogWindow.setMinimumSize(QtCore.QSize(480, 300))
            #self.files_set_DialogWindow.setMaximumSize(QtCore.QSize(480, 300))
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
QSpinBox {
    background-color: #39DFA2;
    font-size: 15px;
	border-radius: 5px;
	padding: 5px;
	padding-left: 10px;
}
QSpinBox QAbstractItemView {
	color: #000000;
	background-color: #2ABF88;
	padding: 10px;
	selection-background-color: #2ABF88;
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
            self.alarm_add_layout = QtWidgets.QVBoxLayout(self.files_set_DialogWindow)
            self.alarm_ok_layout = QtWidgets.QHBoxLayout()
            self.dialog_ok_btn = QtWidgets.QPushButton(s)
            if txt == "Add":
                self.dialog_ok_btn.setText("Add")
            else:
                self.dialog_ok_btn.setText("Save")
            self.dialog_cancel_btn = QtWidgets.QPushButton()
            self.dialog_cancel_btn.setText("Cancel")
            self.dialog_cancel_btn.clicked.connect(lambda: self.files_set_DialogWindow.reject())
            self.alarm_ok_layout.addWidget(self.dialog_ok_btn)
            self.alarm_ok_layout.addWidget(self.dialog_cancel_btn)

            self.dialog_textEdit = QtWidgets.QTextEdit()
            self.dialog_textEdit.setPlaceholderText("Name")
            self.dialog_textEdit.setFixedHeight(50)
            self.dialog_label = QtWidgets.QLabel()
            self.dialog_label.setText(f"{txt} your Alarm")

            self.alarm_hour_add = QtWidgets.QSpinBox()
            self.alarm_hour_add.setRange(1,12)
            self.alarm_minute_add = QtWidgets.QSpinBox()
            self.alarm_minute_add.setRange(0,59)

            self.alarm_time_add_layout = QtWidgets.QHBoxLayout()
            self.alarm_hour_layout = QtWidgets.QVBoxLayout()
            self.alarm_minute_layout = QtWidgets.QVBoxLayout()

            self.alarm_hour_label = QtWidgets.QLabel()
            self.alarm_hour_label.setText("Hour")
            self.alarm_hour_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
            self.alarm_minute_label = QtWidgets.QLabel()
            self.alarm_minute_label.setText("Minute")
            self.alarm_minute_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")

            self.alarm_hour_layout.addWidget(self.alarm_hour_label)
            self.alarm_hour_layout.addWidget(self.alarm_hour_add)
            self.alarm_minute_layout.addWidget(self.alarm_minute_label)
            self.alarm_minute_layout.addWidget(self.alarm_minute_add)

            self.alarm_mid_group = QtWidgets.QComboBox()
            self.alarm_mid_group.addItems(["AM", "PM"])


            self.alarm_time_add_layout.addLayout(self.alarm_hour_layout)
            self.alarm_time_add_layout.addLayout(self.alarm_minute_layout)
            self.alarm_mid_group_layout = QtWidgets.QVBoxLayout()
            self.alarm_mid_group_layout.addStretch(2)
            self.alarm_mid_group_layout.addWidget(self.alarm_mid_group)
            self.alarm_time_add_layout.addLayout(self.alarm_mid_group_layout)

            self.alarm_other_layout = QtWidgets.QHBoxLayout()
            self.alarm_repeats_label = QtWidgets.QLabel("Repeats")
            self.alarm_repeats_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
            self.alarm_sound_label = QtWidgets.QLabel("Sound")
            self.alarm_sound_label.setStyleSheet("font-family: 'Cabin', sans-serif;font-size: 15px;")
            self.alarm_repeats_add = QtWidgets.QComboBox()
            self.alarm_repeats_add.addItems(["Only Once", "Every day", "Every week", "Every Month"])
            self.alarm_sound_add = QtWidgets.QComboBox()
            self.alarm_sound_add.addItems(["sound A", "sound B", "sound C", "sound D", "sound E"])

            self.alarm_repeats_layout = QtWidgets.QVBoxLayout()
            self.alarm_repeats_layout.addWidget(self.alarm_repeats_label)
            self.alarm_repeats_layout.addWidget(self.alarm_repeats_add)
            self.alarm_sound_layout = QtWidgets.QVBoxLayout()
            self.alarm_sound_layout.addWidget(self.alarm_sound_label)
            self.alarm_sound_layout.addWidget(self.alarm_sound_add)

            self.alarm_other_layout.addLayout(self.alarm_repeats_layout)
            self.alarm_other_layout.addLayout(self.alarm_sound_layout)


            self.alarm_add_layout.addWidget(self.dialog_label)
            self.alarm_add_layout.addWidget(self.dialog_textEdit)
            self.alarm_add_layout.addLayout(self.alarm_time_add_layout)
            self.alarm_add_layout.addLayout(self.alarm_other_layout)
            self.alarm_add_layout.addLayout(self.alarm_ok_layout)

            self.files_set_DialogWindow.exec_()

#-----------------end of code adding--------------------------------------
        self.green_alarm_addcode_btn.clicked.connect(lambda : green_alarm_add_window("Add"))
        self.green_alarm_scroll_Area = QtWidgets.QScrollArea(self.green_alarm_centralwidget)
        self.green_alarm_scroll_Area.setWidgetResizable(True)
        self.green_alarm_centralwidget.setStyleSheet(
"QWidget {"
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
        self.green_alarm_scroll_Area.setStyleSheet("background: #2ABF88; border-radius: 7px;")
        self.green_alarm_scroll_AreaWidgetContents = QtWidgets.QWidget(self.green_alarm_scroll_Area)
        self.green_alarm_scroll_Area.setWidget(self.green_alarm_scroll_AreaWidgetContents)

        self.green_alarm_verticalLayout.addWidget(self.green_alarm_scroll_Area)

        self.green_alarm_scrollArea_formLayout = QtWidgets.QFormLayout(self.green_alarm_scroll_AreaWidgetContents)
        self.green_alarm_cond_lst = [r".\Asserts\images\off.png", r".\Asserts\images\on.png"]
        self.green_alarm_cond_text = ["Off", "On"]
        self.green_alarm_cond = {}
        def green_alarm_create_alarm_btn(btn, i, s):
            self.green_alarm_cond[btn] = 0
            btn.setFixedSize(60,35)
            btn.setIcon(QtGui.QIcon(self.green_alarm_cond_lst[self.green_alarm_cond[btn]]))
            btn.setIconSize(QtCore.QSize(40,35))
            btn.setText(self.green_alarm_cond_text[self.green_alarm_cond[btn]])
            btn.setStyleSheet("""
QPushButton {
    background-color: transparent;
    font-size: 12px;
}
QPushButton:hover {
    background-color: #27A97A;
}
QPushButton:pressed {
    background-color: #1A4E3B;
}
""")
            def alarm_switch():
                self.green_alarm_cond[btn] = not self.green_alarm_cond[btn]
                btn.setIcon(QtGui.QIcon(self.green_alarm_cond_lst[self.green_alarm_cond[btn]]))
                btn.setText(self.green_alarm_cond_text[self.green_alarm_cond[btn]])
            btn.clicked.connect(lambda: alarm_switch())

        for i,s in enumerate(files):
            green_alarm_create_scroll_btn_layout = QtWidgets.QHBoxLayout()
            green_alarm_switch_btn = QtWidgets.QPushButton()
            green_alarm_create_alarm_btn(green_alarm_switch_btn, i, s)

            green_alarm_main_btn = QtWidgets.QPushButton()
            green_alarm_main_btn.setFixedSize(240,60)
            green_alarm_main_btn.setText(files[i])
            #green_alarm_main_btn.setAlignment(QtCore.Qt.AlignCenter)
            green_alarm_main_btn.setStyleSheet(
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

            green_alarm_edit_btn = QtWidgets.QPushButton()   #39DFA2
            green_alarm_edit_btn.setIcon(QtGui.QIcon(r".\Asserts\images\edit_icon.png"))
            green_alarm_edit_btn.setIconSize(QtCore.QSize(28, 28))
            green_alarm_edit_btn.setFixedSize(30,60)
            green_alarm_edit_btn.setStyleSheet(
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
            green_alarm_edit_btn.clicked.connect(lambda : green_alarm_add_window("Edit"))

            green_alarm_del_btn = QtWidgets.QPushButton()
            green_alarm_del_btn.setIcon(QtGui.QIcon(r".\Asserts\images/del_icon.png"))
            green_alarm_del_btn.setIconSize(QtCore.QSize(28, 28))
            green_alarm_del_btn.setFixedSize(30,60)   #39DFA2
            green_alarm_del_btn.setStyleSheet(
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
            green_alarm_create_scroll_btn_layout.addWidget(green_alarm_switch_btn)
            green_alarm_create_scroll_btn_layout.addWidget(green_alarm_main_btn)
            green_alarm_create_scroll_btn_layout.addWidget(green_alarm_edit_btn)
            green_alarm_create_scroll_btn_layout.addWidget(green_alarm_del_btn)
            self.green_alarm_scrollArea_formLayout.addRow(green_alarm_create_scroll_btn_layout)

        def switch_theme(from_,to_):
            self.i = 0
            if from_ == "D":
                self.dark_setting_centralwidget.hide()
            elif from_ == "L":
                self.light_setting_centralwidget.hide()
            else:
                self.green_setting_centralwidget.hide()

            self.c_th = to_

            if self.c_th == "D":
                self.dark_setting_centralwidget.show()
            elif self.c_th == "L":
                self.light_setting_centralwidget.show()
            else:
                self.green_setting_centralwidget.show()



        self.dark_setting_dark_theme_btn.clicked.connect(lambda : switch_theme("D","D"))
        self.dark_setting_light_theme_btn.clicked.connect(lambda : switch_theme("D","L"))
        self.dark_setting_green_theme_btn.clicked.connect(lambda : switch_theme("D","L"))

        self.light_setting_dark_theme_btn.clicked.connect(lambda : switch_theme("L","D"))
        self.light_setting_light_theme_btn.clicked.connect(lambda : switch_theme("L","L"))
        self.light_setting_green_theme_btn.clicked.connect(lambda : switch_theme("L","G"))

        self.green_setting_dark_theme_btn.clicked.connect(lambda : switch_theme("G","D"))
        self.green_setting_light_theme_btn.clicked.connect(lambda : switch_theme("G","L"))
        self.green_setting_green_theme_btn.clicked.connect(lambda : switch_theme("G","G"))

        def switch_home(from_,c):
            #self.i = 0
            from_.hide()
            if c == "D":
                self.dark_main_central_widget.show()
            elif c == "L":
                self.light_main_central_widget.show()
            else:
                self.green_main_central_widget.show()

        self.dark_setting_home_btn.clicked.connect(lambda: switch_home(self.dark_setting_centralwidget, "D"))
        self.light_setting_home_btn.clicked.connect(lambda: switch_home(self.light_setting_centralwidget, "L"))
        self.green_setting_home_btn.clicked.connect(lambda: switch_home(self.green_setting_centralwidget, "G"))

        self.dark_code_home_btn.clicked.connect(lambda: switch_home(self.dark_code_centralwidget, "D"))
        self.light_code_home_btn.clicked.connect(lambda: switch_home(self.light_code_centralwidget, "L"))
        self.green_code_home_btn.clicked.connect(lambda: switch_home(self.green_code_centralwidget, "G"))

        self.dark_trans_home_btn.clicked.connect(lambda: switch_home(self.dark_trans_centralwidget, "D"))
        self.light_trans_home_btn.clicked.connect(lambda: switch_home(self.light_trans_centralwidget, "L"))
        self.green_trans_home_btn.clicked.connect(lambda: switch_home(self.green_trans_centralwidget, "G"))

        self.dark_task_home_btn.clicked.connect(lambda: switch_home(self.dark_task_centralwidget, "D"))
        self.light_task_home_btn.clicked.connect(lambda: switch_home(self.light_task_centralwidget, "L"))
        self.green_task_home_btn.clicked.connect(lambda: switch_home(self.green_task_centralwidget, "G"))

        self.dark_alarm_home_btn.clicked.connect(lambda: switch_home(self.dark_alarm_centralwidget, "D"))
        self.light_alarm_home_btn.clicked.connect(lambda: switch_home(self.light_alarm_centralwidget, "L"))
        self.green_alarm_home_btn.clicked.connect(lambda: switch_home(self.green_alarm_centralwidget, "G"))

        def switch_to(from_, to_, c_th):
            from_.hide()
            if to_ == "setting":
                self.to_combo_index = 0
                self.dark_trans_to_lang_combo.setCurrentIndex(self.to_combo_index)
                self.light_trans_to_lang_combo.setCurrentIndex(self.to_combo_index)
                self.light_trans_to_lang_combo.setCurrentIndex(self.to_combo_index)
                self.dark_trans_from_textedit.clear()
                self.dark_trans_to_textedit.clear()
                self.light_trans_from_textedit.clear()
                self.light_trans_to_textedit.clear()
                self.green_trans_from_textedit.clear()
                self.green_trans_to_textedit.clear()

                if self.c_th == "D":
                    self.dark_setting_centralwidget.show()
                elif self.c_th == "L":
                    self.light_setting_centralwidget.show()
                else:
                    self.green_setting_centralwidget.show()
            elif to_ == "Main":
                if self.c_th == "D":
                    self.dark_main_central_widget.show()
                elif self.c_th == "L":
                    self.light_main_central_widget.show()
                else:
                    self.green_main_central_widget.show()
            elif to_ == "Code":
                if self.c_th == "D":
                    self.dark_code_centralwidget.show()
                elif self.c_th == "L":
                    self.light_code_centralwidget.show()
                else:
                    self.green_code_centralwidget.show()
            elif to_ == "trans":
                if self.c_th == "D":
                    self.dark_trans_centralwidget.show()
                elif self.c_th == "L":
                    self.light_trans_centralwidget.show()
                else:
                    self.green_trans_centralwidget.show()
            elif to_ == "task":
                if self.c_th == "D":
                    self.dark_task_centralwidget.show()
                elif self.c_th == "L":
                    self.light_task_centralwidget.show()
                else:
                    self.green_task_centralwidget.show()
            else:
                if self.c_th == "D":
                    self.dark_alarm_centralwidget.show()
                elif self.c_th == "L":
                    self.light_alarm_centralwidget.show()
                else:
                    self.green_alarm_centralwidget.show()

        self.dark_main_setting_btn.clicked.connect(lambda: switch_to(self.dark_main_central_widget, "setting", self.c_th))
        self.dark_main_code_page.clicked.connect(lambda: switch_to(self.dark_main_central_widget, "Code", self.c_th))
        self.dark_main_trans_page.clicked.connect(lambda: switch_to(self.dark_main_central_widget, "trans", self.c_th))
        self.dark_main_task_page.clicked.connect(lambda: switch_to(self.dark_main_central_widget, "task", self.c_th))
        self.dark_main_alarm_page.clicked.connect(lambda: switch_to(self.dark_main_central_widget, "alarm", self.c_th))

        self.light_main_setting_btn.clicked.connect(lambda: switch_to(self.light_main_central_widget, "setting", self.c_th))
        self.light_main_code_page.clicked.connect(lambda: switch_to(self.light_main_central_widget, "Code", self.c_th))
        self.light_main_trans_page.clicked.connect(lambda: switch_to(self.light_main_central_widget, "trans", self.c_th))
        self.light_main_task_page.clicked.connect(lambda: switch_to(self.light_main_central_widget, "task", self.c_th))
        self.light_main_alarm_page.clicked.connect(lambda: switch_to(self.light_main_central_widget, "alarm", self.c_th))

        self.green_main_setting_btn.clicked.connect(lambda: switch_to(self.green_main_central_widget, "setting", self.c_th))
        self.green_main_code_page.clicked.connect(lambda: switch_to(self.green_main_central_widget, "Code", self.c_th))
        self.green_main_trans_page.clicked.connect(lambda: switch_to(self.green_main_central_widget, "trans", self.c_th))
        self.green_main_task_page.clicked.connect(lambda: switch_to(self.green_main_central_widget, "task", self.c_th))
        self.green_main_alarm_page.clicked.connect(lambda: switch_to(self.green_main_central_widget, "alarm", self.c_th))

        self.dark_main_central_widget.show()
        self.light_main_central_widget.hide()
        self.green_main_central_widget.hide()

        self.dark_setting_centralwidget.hide()
        self.light_setting_centralwidget.hide()
        self.green_setting_centralwidget.hide()

        self.dark_code_centralwidget.hide()
        self.light_code_centralwidget.hide()
        self.green_code_centralwidget.hide()

        self.dark_trans_centralwidget.hide()
        self.light_trans_centralwidget.hide()
        self.green_trans_centralwidget.hide()

        self.green_task_centralwidget.hide()
        self.dark_task_centralwidget.hide()
        self.light_task_centralwidget.hide()

        self.dark_alarm_centralwidget.hide()
        self.light_alarm_centralwidget.hide()
        self.green_alarm_centralwidget.hide()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

current_theme = "D"
files = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow, current_theme, files)
    MainWindow.show()
    sys.exit(app.exec_())

