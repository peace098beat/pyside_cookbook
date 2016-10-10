#! coding:utf-8

import sys
import os

from PySide.QtCore import *
from PySide.QtGui import *

from applogger import logger
from signalviewer import SignalViewer

from src.levelmeter import LevelMeter
from src.recorder import Recorder


class MyWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.signal_viewer = SignalViewer()
        self.layout.addWidget(self.signal_viewer)

        self.level_viewer = LevelMeter()
        self.layout.addWidget(self.level_viewer)
        # Recorder
        self.recorder = Recorder()

        self.level_viewer.set_pool(self.recorder.get_pool())
        # self.signal_viewer.set_pool(self.recorder.get_pool())


if __name__ == '__main__':
    import traceback
    try:
        app = QApplication(sys.argv)
        dialog = MyWidget()
        dialog.show()
        sys.exit(app.exec_())
    except:
       logger.error(traceback.format_exc(0))
       raise