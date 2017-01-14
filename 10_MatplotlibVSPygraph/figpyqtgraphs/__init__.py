# -*- coding: utf-8 -*-
"""

"""
import sys

from PySide.QtCore import *
from PySide.QtGui import *
import numpy as np
import pyqtgraph as pg

# アンチエイリアスを指定するとプロットがより綺麗になる
pg.setConfigOptions(antialias=True)
pg.setConfigOption('background', (255, 255, 255)) # 背景＝白
pg.setConfigOption('foreground', (0, 0, 0))       # 前景＝黒

class FigPyqtgraph(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.layout = QVBoxLayout(self)

		self.specWid = pg.PlotWidget(name="spectrum")
		self.specItem =  self.specWid.getPlotItem()

		self.layout.addWidget(self.specWid)

	def plot(self, data):
		self.specItem.plot(data,pen=(0,0,0), clear = True)

