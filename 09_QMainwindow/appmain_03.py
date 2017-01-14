#! coding:utf-8
"""
BasedMainWindowの使い方
"""

import sys
import os
import time
from PySide.QtGui import *
from PySide.QtCore import *

from baseqmainwindow import BasedMainWindow


class YourMainWindow(BasedMainWindow):

	""" BaseMainWindwの使いかた """
	
	def __init__(self):
		super().__init__()
		self.fileLoaded.connect(self.loadedfilename)

	@Slot()
	def loadedfilename(self, filename):
		print(filename)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.lastWindowClosed.connect(app.quit)

    win = YourMainWindow()
    win.show()
    sys.exit(app.exec_())