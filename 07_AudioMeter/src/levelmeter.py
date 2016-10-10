import sys
from PySide.QtCore import *
from PySide.QtGui import *
import numpy as np


class LevelItem(QGraphicsItem):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.DefaultViewWidth = kw["w"]
        self.DefaultViewHeight = kw["h"]

        self.item_bg_color = QColor(0, 0, 0)
        self.fig_bg_color = QColor("#222222")
        self.border_color = QColor(0, 0, 0)
        self.series_line_colors = [QColor(150, 0, 0), QColor(0, 100, 0), QColor(0, 0, 1)]

        self.spacing = 0
        self.bounding = QRectF(
            0, 0, self.DefaultViewWidth, self.DefaultViewHeight)
        self.figure_bound = QRectF(
            self.spacing, self.spacing,
            self.DefaultViewWidth - (self.spacing * 2), self.DefaultViewHeight - (self.spacing * 2))

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.timeout)
        self.timer.start()

        self.pool = None
        self.series = QPointF(0, 0)

    def paint(self, painter, option, widget):
        # paint to background
        painter.fillRect(self.bounding, self.item_bg_color)
        painter.fillRect(self.figure_bound, self.fig_bg_color)
        painter.setPen(self.border_color)
        painter.drawRect(self.figure_bound)
        # paint axis line
        painter.drawLine(0, self.DefaultViewHeight / 2, self.DefaultViewWidth, self.DefaultViewHeight / 2)
        # painter.setPen(self.series_line_colors[0])
        # painter.drawPolyline(self.series)
        painter.fillRect(self.series, self.series_line_colors[0])

    def timeout(self):
        if self.pool == None:
            return
        _pcm = self.pool.get_data()

        dec_pcm = np.log2(_pcm.size)
        dec_lim = np.log2(512)
        skip = (dec_pcm - dec_lim) * 2

        pcm = _pcm[::skip]

        # lin
        _rms = np.sqrt(np.dot(pcm, pcm) / pcm.size)
        rms = (self.DefaultViewHeight) - (_rms * self.DefaultViewHeight)

        # log
        # logrms = 10*np.log10(_rms)
        # logrms = np.clip(logrms, -60,0) / 60. * (-1)
        # rms =  (logrms * self.DefaultViewHeight)

        self.series = QRectF(QPointF(0,rms),QPointF(self.DefaultViewWidth,self.DefaultViewHeight))
        self.update()

    def boundingRect(self):
        return self.bounding

    def set_pool(self, p):
        self.pool = p


class LevelMeter(QGraphicsView):
    DefaultViewWidth = 50
    DefaultViewHeight = 150

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.setFixedSize(QSize(self.DefaultViewWidth, self.DefaultViewHeight))

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush(Qt.blue)
        self.scene.setSceneRect(
            0, 0,
            LevelMeter.DefaultViewWidth, LevelMeter.DefaultViewHeight)
        self.setScene(self.scene)
        self.setCacheMode(QGraphicsView.CacheBackground)

        self.waveviewer_item = LevelItem(w=self.DefaultViewWidth, h=self.DefaultViewHeight)
        self.scene.addItem(self.waveviewer_item)

    def set_pool(self, p):
        self.waveviewer_item.set_pool(p)


def testmain():
    app = QApplication(sys.argv)
    wave_figure = LevelMeter()
    wave_figure.show()
    app.exec_()


if __name__ == '__main__':
    testmain()
