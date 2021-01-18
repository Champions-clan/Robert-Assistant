from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QInputDialog, QMenu, QLabel, QAction, QLineEdit, QDialog, QApplication, QSplashScreen, QSystemTrayIcon, QWidget
import sys
import time

class LoadingScreen(QWidget):
	def __init__(self):
		super().__init__()
		self.setFixedSize(800, 590)
		self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

		self.label_animation = QLabel(self)

		self.movie = QMovie('test.gif')
		self.label_animation.setMovie(self.movie)

		timer = QTimer(self)
		self.startAnimation()
		timer.singleShot(8600, self.stopAnimation)

		self.show()

	def startAnimation(self):
		self.movie.start()

	def stopAnimation(self):
		self.movie.stop()
		self.close()

class AppDemo(QWidget):
	def __init__(self):
		super().__init__()

		self.loading_screen = LoadingScreen()

		self.show()


app = QApplication(sys.argv)

demo = AppDemo()



demo.show()

app.exec_()