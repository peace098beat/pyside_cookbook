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
pg.setConfigOption('background', (255, 255, 255, 0)) # 背景＝白
pg.setConfigOption('foreground', (0, 0, 0))       # 前景＝黒


class BasePyQtGraph(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        # layout
        self.layout = QVBoxLayout(self)
        self.plot_widget = pg.PlotWidget(name="spectrum")
        # グラフウィジェット
        self.plot_item =  self.plot_widget.getPlotItem()
        self.layout.addWidget(self.plot_widget)
        # シークバーウィジェット
        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        self.plot_widget.addItem(self.vLine, ignoreBounds=True)
        self.vLine.hide()

        # =============================================
        # Options
        # =============================================
        self.plot_widget.setTitle('-')
        self.plot_widget.setLabel('left', '-', units='-')
        self.plot_widget.setLabel('bottom', '-', units='-')
        self.plot_widget.showGrid(x=True,y=True, alpha=0.5)
        self.plot_widget.setLogMode(x=False, y=False)
        self.plot_widget.showButtons()
        # self.plot_widget.setDownsampling(ds=None, auto=True, mode=None)
        # self.plot_widget.addLegend()

    def get_plotItem(self):
        return self.plot_item
    def get_plotWidget(self):
        return self.plot_widget

    def plot(self, xdata, ydata, pen=(0,0,0), clear=True, name="fig"):
        self.plot_item.plot(xdata, ydata, pen=pen, clear=clear, name=name)

    def seek(self):
        pass

class FigWave(BasePyQtGraph):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.get_plotWidget().setTitle('signal')
        self.get_plotWidget().setLabel('left', 'Signal', units='-')
        self.get_plotWidget().setLabel('bottom', 'Time', units='Sec')
        self.get_plotWidget().setLogMode(x=False, y=False)
        self.get_plotWidget().setDownsampling(ds=None, auto=True, mode=None)
        self.get_plotWidget().setYRange(-1,1)

    def plot(self, xdata, ydata, pen=(0,0,0), clear=True, name="fig"):
        self.get_plotItem().plot(xdata, ydata, pen=pen, clear=clear, name=name)

class FigSpectrum(BasePyQtGraph):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.get_plotWidget().setTitle('spectrum')
        self.get_plotWidget().setLabel('left', 'Spectrum Power', units='db')
        self.get_plotWidget().setLabel('bottom', 'Frequency', units='Hz')
        self.get_plotWidget().setLogMode(x=True, y=False)
        self.get_plotWidget().setYRange(-120,0)

    def plot(self, xdata, ydata, pen=(0,0,0), clear=True, name="fig"):
        self.get_plotItem().plot(xdata, ydata, pen=pen, clear=clear, name=name)

class FigSpectrogram(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout(self)

        # pyqtgraphウィジェット
        self.specWid = pg.PlotWidget(name="spectrogram")
        self.layout.addWidget(self.specWid)

        # イメージ描画ウィジェット
        self.img_item = pg.ImageItem()
        self.specWid.addItem(self.img_item)
        
        # シークバーウィジェット
        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        self.specWid.addItem(self.vLine, ignoreBounds=True)

        # コンターカラー(おまじない)
        pos=np.array([0.,0.25,0.5,0.75,1.])
        color = np.array([
            [0,0,0,255], 
            [0,0,255,255], 
            [0,255,0,255], 
            [255,255,0,255], 
            [255,0,0,255],
            ], dtype=np.ubyte)
        cmap = pg.ColorMap(pos, color)
        lut = cmap.getLookupTable(0.0, 1.0, 256)
        self.img_item.setLookupTable(lut)
        self.img_item.setLevels([-120,0])

        # ラベル
        self.specWid.setTitle('spectrogram')
        self.specWid.setLabel('left', 'Frequency', units='Hz')
        self.specWid.setLabel('bottom', 'Time', units='Sec')
        self.specWid.setTitle('signal')
        self.specWid.showGrid(x=False,y=False)

    def get_plotWidget(self):
        return self.specWid

    def set_scale(self, xscale, yscale):

        """軸のラベル配列を渡す
        :xscale: 時間配列
        :yscale: 周波数配列 [Hz]
        """
        self.img_item.scale(xscale, yscale)

    def plot(self, img_array, autoLevels=False):

        self.img_item.setImage(img_array, autoLevels=autoLevels)

    def seek(self,pos):
        self.vLine.setPos(pos)