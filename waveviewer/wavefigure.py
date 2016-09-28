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


class WaveViewItem(QGraphicsItem):
    DefaultViewWidth = 44100 * 10
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

        if self.series is not None:
            for index, linedata in enumerate(self.series):
                painter.setPen(self.series_line_colors[index])
                painter.drawPolyline(linedata)

        # paint series line
        import math

        xs = range(0, self.DefaultViewWidth)
        Y = self.DefaultViewHeight / 2
        painter.setPen(self.series_line_colors[0])
        qpoints1 = [QPointF(x, Y * math.sin(2 * math.pi * x /205. ) + self.DefaultViewHeight / 2)
                    for x in xs]
        painter.drawPolyline(qpoints1)


    def set_series(self, index, data):
        def encode(xmin, xmax, ymin, ymax):
            pass

    def wheelEvent(self, event):
        # delta = event.delta()
        # if 0 < delta:
        #    self.moveBy(100,0)
        #    print(">pos: {}".format(self.pos()))
        # else:
        #     # self.scale(0.8, 1.0)
        #     # self.scroll(-10,0)
        #     self.moveBy(-100,0)
        #     print(">pos: {}".format(self.pos()))
        pass

    def mouseReleaseEvent(self, event):
        print(event)

    def mousePressEvent(self, event):
        pos = event.pos()
        print(">mouserPressEvent",pos)
        self.update()

class WaveViewer(QGraphicsView):
    DefaultViewWidth = 320
    DefaultViewHeight = 150

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush(Qt.blue)
        self.scene.setSceneRect(
            20, 0,
            WaveViewer.DefaultViewWidth, WaveViewer.DefaultViewHeight)
        self.setScene(self.scene)
        self.setCacheMode(QGraphicsView.CacheBackground)

        waveviewer_item = WaveViewItem()
        self.scene.addItem(waveviewer_item)


    def wheelEvent(self, event):
        delta = event.delta()
        r = self.scene.sceneRect()
        if 0 < delta:
            r.setLeft(r.left() + 100)
            self.scene.setSceneRect(r)
        else:
            r.setLeft(r.left()- 100)
            self.scene.setSceneRect(r)

def testmain():
    app = QApplication(sys.argv)
    wave_figure = WaveViewer()
    wave_figure.show()
    app.exec_()


if __name__ == '__main__':
    testmain()
