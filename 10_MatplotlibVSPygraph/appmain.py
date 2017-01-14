#! coding:utf-8
"""
PySideを使ったスピード測定

"""

import sys
import os
import time
from PySide.QtGui import *
from PySide.QtCore import *

from lib.basedMainWindow import BasedMainWindow
from mplcanvas import SignalDataCanvas,SignalDataCanvasFast
from qgraphicsgraph.FigQGraphics import WaveViewer
from figpyqtgraphs import FigPyqtgraph

import numpy as np

class YourMainWindow(BasedMainWindow):

	""" BaseMainWindwの使いかた その2
	ウィジェットのレイアウトの方法
	"""

	MAINLOOP_FPS=60*2

	
	def __init__(self):
		super().__init__()

		# おまじない
		self.main_widget = QWidget(self)
		self.main_layout = QGridLayout(self.main_widget)
		self.setCentralWidget(self.main_widget)

		# 子供UI
		label1 = QLabel("Top - Left")
		label2 = QLabel("Top - Right")
		label3 = QLabel("Bottom - Left")
		label4 = QLabel("Bottom - right")

		self.fig_mpl = SignalDataCanvas()
		self.fig_fastmpl = SignalDataCanvasFast()
		self.fig_qgraphics = WaveViewer()
		self.fig_pyqtgraph = FigPyqtgraph()

		self.figs=[self.fig_mpl,self.fig_fastmpl,self.fig_qgraphics,self.fig_pyqtgraph]
		for fig in self.figs:
			fig.setFixedWidth(320)
			fig.setFixedHeight(240)

		# レイアウトをセット
		self.main_layout.addWidget(self.fig_mpl, 0, 0)
		self.main_layout.addWidget(self.fig_fastmpl, 0, 1)
		self.main_layout.addWidget(self.fig_qgraphics, 1, 0)
		self.main_layout.addWidget(self.fig_pyqtgraph, 1, 1)


		self.chkbox_layout = QHBoxLayout()
		self.main_layout.addLayout(self.chkbox_layout, 2,0)

		radios = [QCheckBox('A') for _ in range(4)]
		for radio in radios:
			self.chkbox_layout.addWidget(radio)
		self.radios = radios


		self.FFTSpinbox = QSpinBox()
		self.FFTSpinbox.setRange(0,1000000)
		self.FFTSpinbox.setSingleStep(1024)
		self.FFTSpinbox.setValue(1024)

		self.chkbox_layout.addWidget(self.FFTSpinbox)

		self.cnt=1

	def mainLoop(self):
		super().mainLoop()

		N=2048
		N = int(self.FFTSpinbox.value())

		df =10
		self.cnt = self.cnt + df
		f0 = self.cnt
		if self.cnt > N: self.cnt=1

		msg="f0:{}".format(f0)
		self.putStatusbar(msg)

		t = np.linspace(0,1,N)
		data = np.sin(2*np.pi*f0*t)
		# data = np.abs(np.fft.fft(data)) + 0.1
		# data = data/N
		# data=20*np.log10(data)

		assert data.size == N
		assert data.ndim == 1

		if self.radios[0].isChecked():
			self.fig_mpl.plot(data)
		if self.radios[1].isChecked():
			self.fig_fastmpl.plot(data)
		if self.radios[2].isChecked():
			self.fig_qgraphics.plot(data)
		if self.radios[3].isChecked():
			self.fig_pyqtgraph.plot(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.lastWindowClosed.connect(app.quit)

    win = YourMainWindow()
    win.show()
    sys.exit(app.exec_())