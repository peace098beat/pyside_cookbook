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
	
	MAINLOOP_FPS=30 # MainLoopのFPSを上書き

	def __init__(self):
		super().__init__()
		self.pros=0
		self._cnt=0

	def mainLoop(self, *args, **kw):
		super().mainLoop()

		# ステータスバーのメッセージを更新
		self._cnt+=1
		self.putStatusbar("YourMainWindowTest"+str(self._cnt))

		# プログレスバーを更新
		self.pros += self.fps/100
		self.putProgressbar(self.pros)
		if self.pros >100:
			self.pros = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.lastWindowClosed.connect(app.quit)

    win = YourMainWindow()
    win.show()
    sys.exit(app.exec_())