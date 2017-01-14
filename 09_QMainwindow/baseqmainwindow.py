#! coding:utf-8
import sys
import time
from PySide.QtGui import *
from PySide.QtCore import *


class BasedMainWindow(QMainWindow):

	MAINLOOP_FPS=120

	def __init__(self):
		super().__init__()

		self.resize(680, 480)

		# メニューバーを作成
		self._setupMenuUI()
		self._setupStatusBarUI()

		# メインループ
		timer = QTimer(self)
		timer.timeout.connect(self.mainLoop)
		timer.start(1000/self.MAINLOOP_FPS) # [ms]
		self.oldtime=time.clock()

	def _setupMenuUI(self):

		# メニューバーを作成
		menubar = QMenuBar()
		self.setMenuBar(menubar)

		# ファイルメニューを作成
		menu_file = QMenu('ファイル',self)
		menu_edit = QMenu('編集',self)
		menu_help = QMenu('ヘルプ',self)
		# メニューを格納
		menus = [menu_file, menu_edit, menu_help]

		# アクションを作成
		action_exit = menu_file.addAction('閉じる')
		action_exit.setShortcut('Ctrl+Q')
		action_exit.triggered.connect(qApp.quit)

		# アクションを作成
		action_open = menu_file.addAction('読み込み')
		action_open.setShortcut('Ctrl+O')
		action_exit.triggered.connect(self.__dumySlot)

		# アクションを作成
		action_pref = menu_edit.addAction('環境設定')
		action_pref.setShortcut('Ctrl+,')
		action_pref.triggered.connect(self.__dumySlot)

		# アクションを作成
		action_about = menu_help.addAction('about')
		action_about.triggered.connect(self.__dumySlot)

		# メニューに追加
		for menu in menus:
			menubar.addMenu(menu)

	def _setupStatusBarUI(self):

		"""ステータスバーを生成"""

		statusbar = QStatusBar()
		self.setStatusBar(statusbar)

	def putStatusbar(self, msg, timeout=0):

		"""ステータスバーを表示するメソッド"""

		self.statusBar().showMessage(msg, timeout)


	@Slot()
	def __dumySlot(self, *args, **kw):
		print(args, kw)
		QMessageBox.information(self, "Message", "ダミースロット")
		self.putStatusbar("Load Dumy Slot",5000)


	@Slot()
	def mainLoop(self, *args, **kw):

		"""
		アプリのメインループ
	
		子供クラスで使う場合ははじめに呼び出しておく。
		これで、FPSを常に知ることができる。

		class ChildMainWindow(BasedMainWindow):
		 	def mainLoop(self, *args, **kw):
		 		super().__init__()
		 		...
		 		pass
		"""

		# FPSを計算
		newtime = time.clock()
		dt = newtime - self.oldtime
		self.oldtime = newtime

		# ステータスバーに表示
		msg = "MainLoop FPS : {:.1f}".format(1/dt)
		self.putStatusbar(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = BasedMainWindow()
    win.show()
    sys.exit(app.exec_())