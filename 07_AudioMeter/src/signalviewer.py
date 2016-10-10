import sys
from PySide.QtCore import *
from PySide.QtGui import *
import numpy as np

class SignalItem(QGraphicsItem):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.DefaultViewWidth = kw["w"]
        self.DefaultViewHeight = kw["h"]

        self.item_bg_color = QColor(0,0,0)
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
        self.series=QPointF(0,0)

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

    def timeout(self):
        if self.pool == None:
            return
        _pcm = self.pool.get_data()
        t=range(self.DefaultViewWidth)

        dec_pcm = np.log2(_pcm.shape[0])
        dec_lim = np.log2(self.DefaultViewWidth)
        skip = (dec_pcm-dec_lim) * 2
        pcm = _pcm[::skip]
        pcm = (self.DefaultViewHeight*pcm) + (self.DefaultViewHeight/2)

        self.series = [QPointF(x, y) for x, y in zip(t, pcm)]

        self.update()

    def boundingRect(self):
        return self.bounding

    def set_pool(self, p):
        self.pool = p


class SignalViewer(QGraphicsView):
    DefaultViewWidth = 512
    DefaultViewHeight = 150

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush(Qt.blue)
        self.scene.setSceneRect(
            0, 0,
            SignalViewer.DefaultViewWidth, SignalViewer.DefaultViewHeight)
        self.setScene(self.scene)
        self.setCacheMode(QGraphicsView.CacheBackground)

        self.waveviewer_item = SignalItem(w=self.DefaultViewWidth, h=self.DefaultViewHeight)
        self.scene.addItem(self.waveviewer_item)

    def set_pool(self, p):
        self.waveviewer_item.set_pool(p)


def testmain():
    app = QApplication(sys.argv)
    wave_figure = SignalViewer()
    wave_figure.show()
    app.exec_()


if __name__ == '__main__':
    testmain()
