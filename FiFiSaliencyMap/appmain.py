#! coding:utf-8
"""
Saliency


opencsv, pyqt で画像表示
http://code.tiblab.net/python/opencv/pyside_window
"""

import sys
import os
import time

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

Signal = pyqtSignal
Slot = pyqtSlot

from base_mainwindow import BasedMainWindow
from image_viewer import ImageViewer
from pySaliencyMain import Saliency

def error_log(msg):
    with open("error.log", "a", encoding="utf-8") as fp:
        fp.write(msg + "\n")
        print(msg)

class YourMainWindow(BasedMainWindow):
    """ BaseMainWindwの使いかた その2
    ウィジェットのレイアウトの方法
    """

    MAINLOOP_FPS = 30

    def __init__(self):
        super().__init__()

        self.resize(1024, 720)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # おまじない
        self.main_widget = QWidget(self)
        self.main_layout = QGridLayout(self.main_widget)
        self.setCentralWidget(self.main_widget)

        # 子供UI

        # window setup
        self.view_origin = ImageViewer()
        #self.view_origin.setFixedSize(512, 512)
        self.view_salient = ImageViewer()
        self.view3= ImageViewer()
        self.view4= ImageViewer()
        #self.view_salient.setFixedSize(512, 512)

        label1 =QLabel("Original")
        label1.setAlignment(Qt.AlignCenter)
        label1.setFont(QFont("Helvetica", 18, 2))
        
        label2 =QLabel("Saliency")
        label2.setAlignment(Qt.AlignCenter)
        label2.setFont(QFont("Helvetica", 18, 2))

        # レイアウトをセット
        self.main_layout.addWidget(label1, 0, 0)
        self.main_layout.addWidget(label2, 0, 1)
        self.main_layout.addWidget(self.view_origin, 1, 0)
        self.main_layout.addWidget(self.view_salient, 1, 1)
        self.main_layout.addWidget(self.view3, 2, 0)
        self.main_layout.addWidget(self.view4, 2, 1)
        #self.main_layout.addWidget(, 2, 0, 2,2 )
        #self.main_layout.addWidget(label4, 1, 1)

        # イベント
        self.fileLoaded.connect(self.draw_origin_image)


    @Slot()
    def draw_origin_image(self):

        self.putStatusbar("draw_origin_image")

        self.origin_image_file = img_file = self.loaded_filepath

        self.putStatusbar(img_file)

        self.view_origin.setFile(img_file)
        # self.view_salient.setFile(img_file)

        # =======================================================================================
        self.putStatusbar("saliency calc start ..." + self.origin_image_file)

        # VIEW1
        self.salinecy = Saliency(self.origin_image_file)



        # VIEW 2
        self.view_salient.setFile(self.salinecy.output_file)

        # VIEW 3
        self.view3.setFile(self.salinecy.region_file)

        self.view4.setFile(self.salinecy.slgray_file)

        # =======================================================================================
        self.putStatusbar("saliency calc end ...")






if __name__ == '__main__':
    app = QApplication(sys.argv)
    # setup stylesheet
    import css
    app.setStyleSheet(css.orange_style)

    app.lastWindowClosed.connect(app.quit)
    
    try:

        win = YourMainWindow()
        win.show()

        app.exec_()
    except Exception as e:
        error_log(str(e))

    sys.exit()