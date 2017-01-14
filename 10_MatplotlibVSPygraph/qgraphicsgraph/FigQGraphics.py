# -*- coding: utf-8 -*-
"""
wavefigure.py
- 数列データを折れ線でプロット
- x軸ズーム
- y軸ズーム
- 再生イベント
- 途中再生
- カーソルバー
"""
import sys

from PySide.QtCore import *
from PySide.QtGui import *

import numpy as np

class WaveViewItem(QGraphicsItem):
    DefaultViewWidth = 256
    DefaultViewHeight = 150

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.wavfile_fullpath = None

        self.item_bg_color = QColor(255, 255, 255)
        self.fig_bg_color = QColor(200, 200, 200)
        self.border_color = QColor(0, 0, 0)
        self.series_line_colors = [QColor(100, 0, 0), QColor(0, 100, 0), QColor(0, 0, 1)]

        self.spacing = 0
        self.bounding = QRectF(
            0, 0, self.DefaultViewWidth, self.DefaultViewHeight)

        self.figure_bound = QRectF(
            self.spacing, self.spacing,
            self.DefaultViewWidth - (self.spacing * 2), self.DefaultViewHeight - (self.spacing * 2))

        self.series = []
    
    def timeout(self):
        frame = self.p.get_nowframe()
        time = range(256)
        data = self.buffer[frame:frame+256]
        self.set_series(time, data)
        self.update()

    def boundingRect(self):
        return self.bounding

    def paint(self, painter, option, widget):
        # paint to background
        painter.fillRect(self.bounding, self.item_bg_color)
        painter.fillRect(self.figure_bound, self.fig_bg_color)
        painter.setPen(self.border_color)
        painter.drawRect(self.figure_bound)
        # paint axis line
        painter.drawLine(0, self.DefaultViewHeight / 2, self.DefaultViewWidth, self.DefaultViewHeight / 2)

        painter.setPen(self.series_line_colors[0])
        painter.drawPolyline(self.series)


    def set_series(self, t, pcm):
        t = np.linspace(0,self.DefaultViewWidth, t.size)

        pcm = pcm - pcm.min()
        pcm = pcm / pcm.max() * self.DefaultViewHeight
        pcm = self.DefaultViewHeight - pcm

        
        qpoints = [QPointF(x, y) for x, y in zip(t, pcm)]
        self.series = qpoints


class WaveViewer(QGraphicsView):
    DefaultViewWidth = 256
    DefaultViewHeight = 150

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush(Qt.blue)
        self.scene.setSceneRect(
            0, 0,
            WaveViewer.DefaultViewWidth, WaveViewer.DefaultViewHeight)
        self.setScene(self.scene)
        self.setCacheMode(QGraphicsView.CacheBackground)

        self.waveviewer_item = WaveViewItem()
        self.scene.addItem(self.waveviewer_item)

    def plot(self, data):
        t = np.array(range(data.size))
        self.waveviewer_item.set_series(t,data)
        self.waveviewer_item.update()
        pass


def testmain():
    app = QApplication(sys.argv)
    wave_figure = WaveViewer()
    wave_figure.show()
    app.exec_()


if __name__ == '__main__':
    testmain()