#! coding:utf-8
"""
app2.py

Created by 0160929 on 2016/10/24 14:46
"""
import os
from PySide.QtCore import Qt

__version__ = '0.0'

import sys

from PySide.QtGui import *

from mpl_images import Image2DHistogram


class MyWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("2D Histogram Viewer")
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setAcceptDrops(True)  # D&D Flag
        self.resize(720, 320)

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
            QMessageBox.warning(self, self.tr("My Application"),
                                self.tr("Please DragDrop only one file.\n"),
                                QMessageBox.Ok)

        self.image2dhistogram.plot(image_path)

        qimage = QImage(image_path)
        _pixmap = QPixmap.fromImage(qimage)
        pixmap = _pixmap.scaled(250,250, Qt.KeepAspectRatio, Qt.FastTransformation)
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
        print(objs)
        if len(objs) == 1:
            p = os.path.abspath(objs[0])
            self.read_image(p)
        else:
            ret = QMessageBox.warning(self, self.tr("My Application"),
                                      self.tr("Please DragDrop only one file.\n"),
                                      QMessageBox.Ok)


def main():
    app = QApplication(sys.argv)
    app.setStyle('plastique')
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
