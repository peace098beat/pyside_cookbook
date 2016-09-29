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
import time

from PySide.QtCore import *
from PySide.QtGui import *
import numpy as np

from player import Player


class WaveViewItem(QGraphicsItem):
    DefaultViewWidth = 512
    DefaultViewHeight = 150

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.item_bg_color = QColor(255, 255, 255)
        self.fig_bg_color = QColor(200, 200, 200)
        self.border_color = QColor(0, 0, 0)
        self.series_line_colors = [
            QColor(100, 0, 0), QColor(0, 100, 0), QColor(0, 0, 1)]

        self.spacing = 0
        self.bounding = QRectF(
            0, 0, self.DefaultViewWidth, self.DefaultViewHeight)

        self.figure_bound = QRectF(
            self.spacing, self.spacing,
            self.DefaultViewWidth - (self.spacing * 2), self.DefaultViewHeight - (self.spacing * 2))

        self.series = []

        self.auto()

    def auto(self):
        """audio plot"""

        import wave

        wf = wave.open("audio2.wav", 'rb')
        wf.rewind()
        wbuffer = wf.readframes(wf.getnframes())
        x = np.frombuffer(wbuffer, dtype="int16")
        x = x / x.max()

        rate = wf.getframerate()
        chunk_size = 512*2

        buffer_size = wf.getnframes()
        buffer = np.zeros(buffer_size, dtype=np.float32)
        buffer[:] = x

        self.p = Player(buffer, chunk_size=chunk_size, rate=rate, live=True)
        self.buffer = self.p.get_audio()
        self.p.play()

        self.timer = QTimer()
        self.timer.setInterval(80)
        self.timer.timeout.connect(self.timeout)
        self.timer.start()

        self.fps_oldtime = time.clock()
        self.fps = 0

        self.scale_number = 1
        self.scale_maxnum = 10
        self.scale_minnum = 1
        self.scale_delta = 1

    def timeout(self):
        """update timer"""
        frame = self.p.get_nowframe()
        # print("frame {}".format(frame))
        nstep = 2**self.scale_number
        chunk_size = self.DefaultViewWidth

        # シフト
        amp = self.DefaultViewHeight / 2.

        # エンベローブ
        if self.scale_number > 6:
            time = range(chunk_size)
            dreshape = self.buffer[
                frame:frame+chunk_size*nstep].reshape((chunk_size, nstep))
            data_max = np.atleast_1d(np.max(dreshape, axis=1))
            data_min = np.atleast_1d(np.min(dreshape, axis=1))
            data = [-1 * d * amp + amp for d in data_max] + \
                [-1 * d * amp + amp for d in data_min[::-1]]
            time = list(time) + list(time[::-1])
        else:
            data = -1. * amp * \
                self.buffer[frame:frame+chunk_size*nstep:nstep] + amp
            time = range(chunk_size)

        self.set_series(time, data)
        self.update()

    def calc_fps(self):
        fps_newtime = time.clock()
        self.fps = 1.0 / (fps_newtime - self.fps_oldtime)  # [s]
        self.fps_oldtime = fps_newtime
        print("FPS :{:0.1f}[fps]".format(self.fps))

    def paint_wave(self, painter):
        # paint series
        painter.setPen(self.series_line_colors[0])
        if self.scale_number > 6:
            painter.setBrush(
                QBrush(self.series_line_colors[0], Qt.SolidPattern))
            painter.drawPolygon(QPolygonF(self.series))
        else:
            painter.drawPolyline(self.series)
        # test scale
        # painter.drawText(0,0,100,50,Qt.AlignCenter, "scale:{}".format(self.scale_number))
        
    def boundingRect(self):
        return self.bounding

    def paint(self, painter, option, widget):
        self.calc_fps()
        # paint to background
        painter.fillRect(self.bounding, self.item_bg_color)
        painter.fillRect(self.figure_bound, self.fig_bg_color)
        painter.setPen(self.border_color)
        painter.drawRect(self.figure_bound)
        # paint axis line
        painter.drawLine(0, self.DefaultViewHeight / 2,
                         self.DefaultViewWidth, self.DefaultViewHeight / 2)
        # paint wave
        self.paint_wave(painter)

    def set_series(self, t, pcm):
        qpoints = [QPointF(x, y) for x, y in zip(t, pcm)]
        self.series = qpoints

    def wheelEvent(self, event):
        delta = event.delta()
        if 0 < delta:
            if not (self.scale_number < self.scale_minnum):
                self.scale_number -= self.scale_delta
        else:
            if not (self.scale_maxnum < self.scale_number):
                self.scale_number += self.scale_delta


class WaveViewer(QGraphicsView):
    DefaultViewWidth = 512
    DefaultViewHeight = 150

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush(Qt.blue)
        self.scene.setSceneRect(
            0, 0, WaveViewer.DefaultViewWidth, WaveViewer.DefaultViewHeight)
        self.setScene(self.scene)
        self.setCacheMode(QGraphicsView.CacheBackground)

        waveviewer_item = WaveViewItem()
        self.scene.addItem(waveviewer_item)


def testmain():
    app = QApplication(sys.argv)
    wave_figure = WaveViewer()
    wave_figure.show()
    app.exec_()


if __name__ == '__main__':
    testmain()
