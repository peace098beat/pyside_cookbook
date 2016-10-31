#! coding:utf-8
"""
PreferenceDialog.py

GUIでよくある設定項目選択用のダイアログ．
辞書型で選択肢を渡すと起動．

config = {
    'Exp': ('E001', 'E002', 'E003'),
    'Club': ('J715', 'PHYZ'),
    'Ball': ('P1', 'D1', 'F1'),
    'Mic': ('E100H160', 'S100H160'),
}

selected_config, ok = PreferenceDialog.run(parent=None, config=config)


"""
import logging
import traceback

from PySide.QtGui import QApplication, QDialog, QCheckBox, QHBoxLayout, QVBoxLayout, QGroupBox, QDialogButtonBox
from PySide.QtCore import Slot, QSettings, Qt

# logger
logging.basicConfig(
    filename='error.log', format='[%(asctime)s] %(levelname)s : %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("App Start")

__all__ = ["PreferenceDialog"]


class PreferenceDialog(QDialog):
    def __init__(self, config, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Preference Dialog")
        self.resize(400, 100)

        self.ui_config = config

        self.setUpUi()

        self.mySettings = QSettings("TomoyukiNohara", "PreferenceDialog")
        # self.mySettings = QSettings("setting.ini", QSettings.IniFormat)
        self.readSettings()

    def setUpUi(self):
        """
        config = {
            'Exp': ('E001', 'E002', 'E003'),
            'Club': ('J715', 'PHYZ'),
            'Ball': ('P1', 'D1', 'F1'),
            'Mic': ('E100H160', 'S100H160'),
        }
        """
        # Main Layout
        self.main_layout = QVBoxLayout(self)

        # CheckBoxes
        self.checkbox_ui = {}

        # チェックボックスを生成
        for key, names in self.ui_config.items():
            checkboxes = []
            for name in names:
                cb = QCheckBox(name, self)
                # 後で呼び出し元を調べるためにObjectNameに名前を格納
                cb.setObjectName(name)
                checkboxes.append(cb)
            # UIオブジェクトが格納された辞書
            self.checkbox_ui[key] = checkboxes


        # GUIをレイアウトで整列
        # 毎回辞書から呼ばれる順番が変わるのでソート(重要)
        for key, uiobjs in sorted(self.checkbox_ui.items(), key=lambda x: x[0]):

            groupBox = QGroupBox(key, self)

            layout = QHBoxLayout()

            for uiobj in uiobjs:
                layout.addWidget(uiobj)
            layout.addStretch(3)
            groupBox.setLayout(layout)

            self.main_layout.addWidget(groupBox)


        # Button Box
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.main_layout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def writeSettings(self):
        for key, uiobjes in self.checkbox_ui.items():
            for obj in uiobjes:
                self.mySettings.setValue(key + '/' + obj.objectName(), int(obj.isChecked()))

    def readSettings(self):
        for key, uiobjes in self.checkbox_ui.items():
            for obj in uiobjes:
                val = self.mySettings.value(key + '/' + obj.objectName(), 0)
                obj.setChecked(bool(int(val)))

    @Slot()
    def accept(self, *args, **kwargs):
        self.writeSettings()
        super().accept()

    def get_selected_preference(self):
        """
        チェックボックスで選択された要素を辞書で返す
        :return: selected_config:{'Club': ['PHYZ'], 'Mic': ['S100H160'], 'Ball': ['D1'], 'Exp': ['E002']}
        """
        checkboxes = self.checkbox_ui

        selected_config = {}

        for key, uiobjs in checkboxes.items():
            selected_config.setdefault(key, list())
            for uiobj in uiobjs:
                if uiobj.checkState():
                    # 該当する項目(key)のリストに追加する
                    selected_config[key].append(uiobj.objectName())

        return selected_config

    @staticmethod
    def run(parent=None, config=None):
        dialog = PreferenceDialog(config, parent)
        result = dialog.exec_()
        if result == QDialog.Accepted:
	        selected_config = dialog.get_selected_preference()
	    else:
	        selected_config = config
        return (selected_config, result == QDialog.Accepted)


def main():
    import sys

    try:
        app = QApplication(sys.argv)
        app.setStyle('plastique')

        config = {
            'Exp': ('E001', 'E002', 'E003'),
            'Club': ('J715', 'PHYZ'),
            'Ball': ('P1', 'D1', 'F1'),
            'Mic': ('E100H160', 'S100H160'),
        }
        selected_config, ok = PreferenceDialog.run(parent=None, config=config)

        print("selected_config:{}, ok:{}".format(selected_config, ok))

    except:
        print(traceback.format_exc())
        logger.error(traceback.format_exc())
        raise IOError("App run Error")
    finally:
        sys.exit(0)


if __name__ == '__main__':
    main()
