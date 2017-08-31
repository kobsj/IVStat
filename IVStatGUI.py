from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MainWindow(QMainWindow):


	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)


		self.setWindowTitle("IVStat")

		label = QLabel("Delete me, probably")
		label.setAlignment(Qt.AlignCenter)

		self.setCentralWidget(label)

		toolbar = QToolBar("Toolbar")
		toolbar.setIconSize(QSize(16, 16))
		self.addToolBar(toolbar)

		button_action = QAction(QIcon( os.path.join('icons',"bug.png"), "Your button", self)
		button_action.setStatusTip("This is your button")
		button_action.triggered.connect(self.onMyToolBarButtonClick)
		button_action.setCheckable(True)
		toolbar.addAction(button_action)

		toolbar.addSeparator()

		button_action2 = QAction(QIcon( os.path.join('icons',"bug.png"), "Your Button2", self)
		button_action2.setStatusTip("This is your button too")
		button_action2.triggered.connect(self.onMyToolBarButtonClick)
		button_action2.setCheckable(True)
		toolbar.addAction(button_action2)

		toolbar.addWidget(QLabel("Hello"))
		toolbar.addWidget(QCheckBox())

		self.setStatusBar(QStatusBar(self))

		menu = self.menuBar()
		menu.setNativeMenuBar(False) #disables the global menu on MacOS

		file_menu = menu.addMenu("&File")
		file_menu.addAction(button_action)

		file_menu.addSeparator()

		file_menu.addAction(button_action2)

	def onMyToolBarButtonClick(self, s):
		print("click", s)

app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!! so see anything

app.exec_()


# QToolBar = Toolbar
# QLabel = Text in screen
# setStatusTip declares what the mouse is hovering over
# QIcon after QAction to choose icon art file
