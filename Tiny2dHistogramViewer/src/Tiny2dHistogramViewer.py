#! coding:utf-8
"""
Tiny2dHistogramViewer.py

Created by 0160929 on 2016/10/24 14:46
"""
__version__ = '0.1'
import os
import sys
import logging
# **************************************
# Logger
logging.basicConfig(filename='error.log', format='[%(asctime)s] %(levelname)s : %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger = logging.debug("app start")
# **************************************

import traceback

from PySide.QtGui import QWidget, QHBoxLayout, QGraphicsView, QGraphicsScene, QMessageBox, QImage, QPixmap, \
    QGraphicsPixmapItem, QApplication
from PySide.QtCore import Qt, QSize

from mpl_images import Image2DHistogram


class MyWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("2D Histogram Viewer ver" + __version__)
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setAcceptDrops(True)  # D&D Flag
        self.setFixedSize(QSize(720, 320))
        # self.resize(720, 320)

        self.layout = QHBoxLayout()

        self.pic_view = QGraphicsView()
        self.pic_scene = QGraphicsScene()
        self.pic_view.setScene(self.pic_scene)
        self.layout.addWidget(self.pic_view)

        self.image2dhistogram = Image2DHistogram()
        self.layout.addWidget(self.image2dhistogram)

        self.setLayout(self.layout)

    def read_image(self, image_path):
        if not os.path.exists(image_path):
            QMessageBox.warning(self, self.tr("Warning!"),
                                self.tr("Image File is not exists.\n"),
                                QMessageBox.Ok)

        self.image2dhistogram.plot(image_path)

        qimage = QImage(image_path)
        _pixmap = QPixmap.fromImage(qimage)
        pixmap = _pixmap.scaled(250, 250, Qt.KeepAspectRatio, Qt.FastTransformation)
        pic_Item = QGraphicsPixmapItem(pixmap)
        self.pic_scene.clear()
        self.pic_scene.addItem(pic_Item)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        objs = [str(u.toLocalFile()) for u in event.mimeData().urls()]

        if len(objs) == 1:
            p = os.path.abspath(objs[0])
            self.read_image(p)
        else:
            ret = QMessageBox.warning(self, self.tr("Warning"),
                                      self.tr("Please DragDrop only one file.\n"),
                                      QMessageBox.Ok)


def main():
    try:
        app = QApplication(sys.argv)
        app.setStyle('plastique')
        win = MyWindow()
        win.show()
    except:
        logger.error(traceback.format_exc())

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
