#!coding:utf-8


import sys

from PySide.QtCore import *
from PySide.QtGui import *

from Ui_Dialog import Ui_Dialog


# ====================
# 臨時フォルダ経由のパスに変更
# ====================
def resource_path(relative):
  if hasattr(sys, "_MEIPASS"):
      return os.path.join(sys._MEIPASS, relative)
  return os.path.join(relative)


class SimpleDialog(QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super().__init__(parent) #python3.x
        self.setupUi(self)

    @Slot()
    def your_slot(self, value):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = SimpleDialog()
    dialog.show()
    sys.exit(app.exec_())