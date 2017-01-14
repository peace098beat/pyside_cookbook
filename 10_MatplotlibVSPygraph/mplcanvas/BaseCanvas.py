#! coding:utf-8
"""
MplCanvas

(2015.11.18) atTimeスペクトルの補助軸線を追加
(2015.11.12) 時間平化機能追加, GWTグラフにatFreqシークバーを表示
(2015.11.12) グラフ線デザイン変更

"""

import sys

from PySide.QtGui import QApplication, QImage
from PySide.QtCore import Slot
from matplotlib import rcParams, use

rcParams['backend.qt4'] = 'PySide'
use('Qt4Agg')

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import matplotlib.pyplot as plt


###################################################
#
# Base
#
###################################################
class BaseMplCanvas(FigureCanvas):
    """ FigureCanvasウィジェット """

    def __init__(self, parent=None, width=5, height=4, dpi=72):
        # fiugrueの生成
        self.fig = Figure(figsize=(width, height), dpi=dpi,
                          facecolor=[1, 1, 1], edgecolor=[0, 0, 0],
                          linewidth=1.0,
                          frameon=False, tight_layout=True)
        # コンストラクタ
        FigureCanvas.__init__(self, self.fig)
        # 親のウィジェットを生成
        self.setParent(parent)
        # サイズの設定
        # FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding,  QtGui.QSizePolicy.Expanding)
        # サイズの更新
        FigureCanvas.updateGeometry(self)

        # axesハンドルの生成
        self.axes = self.fig.add_subplot(111)
        # 再描画では上書きしない
        self.axes.hold(False)
        # 画像の初期表示
        self.compute_initial_fiugre()

        # : プロパティ
        self.data = None
        self.xdata = None
        self.ydata = None
        self.title = None
        self.xlabel = None
        self.ylabel = None

        # : イベント接続
        self.axes.figure.canvas.mpl_connect('button_release_event', self.mouser_action)

    # ***************************************
    # 補助関数
    # ***************************************
    def copy_clipboard(self):
        from io import BytesIO

        buf = BytesIO()
        self.fig.savefig(buf)
        QApplication.clipboard().setImage(QImage.fromData(buf.getvalue()))
        buf.close()

    def canvas_update(self):
        self.draw()

    def compute_initial_fiugre(self):
        """グラフの軸の設定項目を書く"""
        lines = self.axes.plot([0, 1], [0, 1])
        self.line = lines[0]
        self.canvas_update()
        pass

    # ***************************************
    # ユーザーイベント
    # ***************************************
    @Slot()
    def mouser_action(self, event):
        # 右クリック
        if event.button == 3:
            self.copy_clipboard()
        # 左クリック
        if event.button == 1:
            pass

    # ***************************************
    # Abstruct
    # ***************************************
    def plot(self):
        self.axes.plot([0,1],[0,1])
        return self


    # ***************************************
    # Setter
    # ***************************************
    def set_xlabel(self, s):
        self.xlabel = s
        self.axes.set_xlabel(s)
        return self

    def set_ylabel(self, s):
        self.ylabel = s
        self.axes.set_ylabel(s)
        return self

    def set_title(self, title):
        # print 'set_title', title
        self.title = title
        self.axes.set_title(self.title)

    def set_xlim(self, lim):
        self.xlim = lim
        self.axes.set_xlim(self.xlim)

    def set_ylim(self, lim):
        self.ylim = [lim[0], lim[1]]
        self.axes.set_ylim(self.ylim)

    @Slot(int)
    def set_ylim_min(self, min):
        self.ylim[0] = min
        self.axes.set_ylim(self.ylim)

    @Slot(int)
    def set_ylim_max(self, max):
        self.ylim[1] = max
        self.axes.set_ylim(self.ylim)

    def set_zlim(self, lim):
        self.zlim = lim
        self.axes.set_zlim(self.zlim)

    def set_axis(self, axis):
        self.axes.axis(axis)


def main():
    app = QApplication(sys.argv)
    # app.setStyle('plastique')
    win = BaseMplCanvas()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
