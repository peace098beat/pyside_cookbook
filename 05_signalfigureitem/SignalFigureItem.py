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


class SignalFigureItem(QGraphicsItem):
    DefaultViewWidth = 512
    DefaultViewHeight = 128

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.item_bg_color = QColor(255, 255, 255)
        self.fig_bg_color = QColor(200, 200, 200)
        self.border_color = QColor(0, 0, 0)
        self.series_colors = [
            QColor(100, 0, 0), QColor(0, 100, 0), QColor(0, 0, 1)]

        self.spacing = 0
        self.bounding = QRectF(
            0, 0, self.DefaultViewWidth, self.DefaultViewHeight)

        self.figure_bound = QRectF(
            self.spacing, self.spacing,
            self.DefaultViewWidth - (self.spacing * 2), self.DefaultViewHeight - (self.spacing * 2))

        self.series = [None] * 4

    def boundingRect(self):
        return self.bounding

    def paint(self, painter, option, widget):
        # paint to background
        painter.fillRect(self.bounding, self.item_bg_color)
        painter.fillRect(self.figure_bound, self.fig_bg_color)
        painter.setPen(self.border_color)
        painter.drawRect(self.figure_bound)
        # paint axis line
        painter.drawLine(0, self.DefaultViewHeight / 2,
                         self.DefaultViewWidth, self.DefaultViewHeight / 2)
        # # line plot
        # for index, series in enumerate(self.series):
        #     if series is None:
        #         continue
        #     painter.setPen(self.series_colors[index])
        #     painter.drawLine(series)

    def set_series(self, index, x_, y_):
        qpoints = [QPointF(x, y) for x, y in zip(x_, y_)]
        self.series[index] = qpoints

    def clear_series(self, index):
        self.series[index] = None


class WaveViewer(QGraphicsView):
    DefaultViewWidth = 512
    DefaultViewHeight = 128

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush(Qt.blue)
        self.scene.setSceneRect(
            0, 0, WaveViewer.DefaultViewWidth, WaveViewer.DefaultViewHeight)
        self.setScene(self.scene)
        self.setCacheMode(QGraphicsView.CacheBackground)

        waveviewer_item = SignalFigureItem()
        self.scene.addItem(waveviewer_item)


def testmain():
    app = QApplication(sys.argv)
    wave_figure = WaveViewer()
    wave_figure.show()
    app.exec_()


if __name__ == '__main__':
    testmain()
