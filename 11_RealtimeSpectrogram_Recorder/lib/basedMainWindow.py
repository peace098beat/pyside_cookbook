#! coding:utf-8
import sys
import os
import time
from PySide.QtGui import *
from PySide.QtCore import *


class BasedMainWindow(QMainWindow):

	MAINLOOP_FPS=120

	fileLoaded = Signal(str)
	

	def __init__(self):
		super().__init__()

		self.resize(680, 480)

		# メニューバーを作成
		self.__setupMenuUI()
		self.__setupStatusBarUI()

		# メインループ
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.mainLoop)
		self.timer.start(1000/self.MAINLOOP_FPS) # [ms]
		# self.timer.start(0) # [ms]
		self.oldtime=time.clock()

	def setMainLoopFPS(self,fps):
		self.MAINLOOP_FPS=fps
		self.timer.setInterval(1000/self.MAINLOOP_FPS)


	# =====================================================
	#
	# [UI] メニューバー
	#
	# =====================================================
	def __setupMenuUI(self):

		""" メニュ-バーのUIを生成 """

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
		self.action_exit = menu_file.addAction('閉じる')
		self.action_exit.setShortcut('Ctrl+Q')
		self.action_exit.triggered.connect(self.close)

		# アクションを作成
		self.action_open = menu_file.addAction('読み込み')
		self.action_open.setShortcut('Ctrl+O')
		self.action_open.triggered.connect(self._runFileLoad)

		# アクションを作成
		self.action_pref = menu_edit.addAction('環境設定')
		self.action_pref.setShortcut('Ctrl+,')
		self.action_pref.triggered.connect(self._runPreference)

		# アクションを作成
		self.action_about = menu_help.addAction('about')
		self.action_about.triggered.connect(self._runAbout)

		# メニューに追加
		for menu in menus:
			menubar.addMenu(menu)


	@Slot()
	def _runFileLoad(self):

		"""
		ファイルを開く方法を選んで.
		https://srinikom.github.io/pyside-docs/PySide/QtGui/QFileDialog.html
		"""
		fileName, selectedFilter = QFileDialog.getOpenFileName(self, caption='Open File', dir=os.path.expanduser('~')+'/Desktop')
		# fileName, selectedFilter = QFileDialog.getSaveFileName (self, caption='Open File', dir=os.path.expanduser('~')+'/Desktop', filter='', selectedFilter='', options=0)
		# fileNames, selectedFilter = QFileDialog.getOpenFileNames (self, caption='Open File', dir=os.path.expanduser('~')+'/Desktop', filter='', selectedFilter='', options=0)
		# foldername = QFileDialog.getExistingDirectory (self, caption='Open File', dir=os.path.expanduser('~')+'/Desktop', options=QFileDialog.ShowDirsOnly)

		if os.path.exists(fileName):
			self.loaded_filepath = fileName
			msg = "File Load : {}".format(self.loaded_filepath)
			self.putStatusbar(msg, 5000)

			self.fileLoaded.emit(fileName)

	@Slot()
	def _runPreference(self):
		msg="Not Implemented"
		QMessageBox.information(self, "Preference", msg)

	@Slot()
	def _runAbout(self):
		msg="BasedMainWindow ver 1.0"
		QMessageBox.information(self, "About", msg)


	# =====================================================
	#
	# [UI] ステータスバー
	#
	# =====================================================
	def __setupStatusBarUI(self):

		"""ステータスバーを生成"""

		self.statusbar = QStatusBar()
		self.setStatusBar(self.statusbar)

		# プログレスバーを追加
		self.progressbar = QProgressBar()
		self.statusbar.addPermanentWidget(self.progressbar)
		self.progressbar.setTextVisible(True)
		self.progressbar.setRange(0,100)
		self.progressbar.hide()

		# ステータスバーにFPS表示用のレベルを追加
		self.label_fps = QLabel("fps")
		self.statusbar.addPermanentWidget(self.label_fps)

	def putStatusbar(self, msg, timeout=0):

		"""ステータスバーを表示するメソッド"""

		self.statusBar().showMessage(msg, timeout)

	def putFPS(self, fps):
		msg = "FPS:{:.0f}".format(fps)
		self.label_fps.setText(msg)

	def putProgressbar(self, value):

		"""プログレスバーを使う場合に呼び出すメソッド
		0: 非表示, 100:3秒だけ表示
		"""
		self.progressbar.setValue(value)

		if value <= 0:
			self.progressbar.hide()
		elif 100 <= value:
			self.progressbar.setValue(100)
			self.progressbar.show()
			QTimer.singleShot(3000, self.progressbar, SLOT('hide()'))
		else:
			self.progressbar.show()

	# =====================================================
	#
	# メインループ
	#
	# =====================================================
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
		self.fps = 1/dt
		# FPSをステータスバーに表示
		self.putFPS(self.fps)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.lastWindowClosed.connect(app.quit)

    win = BasedMainWindow()
    win.show()
    sys.exit(app.exec_())