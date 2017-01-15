#! coding:utf-8
"""
PySideを使ったスピード測定

"""

import sys
import os
import time
from PySide.QtGui import *
from PySide.QtCore import *
import numpy as np

from lib.basedMainWindow import BasedMainWindow
from figpyqtgraphs import FigWave, FigSpectrum, FigSpectrogram


class YourMainWindow(BasedMainWindow):

    """ BaseMainWindwの使いかた その2
    ウィジェットのレイアウトの方法
    """

    MAINLOOP_FPS=30

    
    def __init__(self):
        super().__init__()

        # おまじない
        self.main_widget = QWidget(self)
        self.main_layout = QGridLayout(self.main_widget)
        self.setCentralWidget(self.main_widget)

        # 子供UI
        self.fig_wave = FigWave()
        self.fig_spectrum = FigSpectrum()
        self.fig_spectrogram = FigSpectrogram()

        # figureの一覧をリスト管理
        self.figs=[ self.fig_wave,
                    self.fig_spectrum, 
                    self.fig_spectrogram]

        # サイズの統一
        for fig in self.figs:
            # fig.setFixedWidth(320)
            fig.setFixedHeight(240)

        # レイアウトをセット
        self.main_layout.addWidget(self.fig_wave, 0, 0)
        self.main_layout.addWidget(self.fig_spectrum, 0, 1)
        self.main_layout.addWidget(self.fig_spectrogram, 1, 0, 1, 2)

        self.cnt = 1
        self.CHUNKSZ = 2048
        self.FS=48000

        self.specgram_buffer = np.zeros((200, self.CHUNKSZ/2+1))

        freq = np.arange((self.CHUNKSZ/2)+1)/(float(self.CHUNKSZ)/self.FS)
        yscale = 1.0/(self.specgram_buffer.shape[1]/freq[-1]) # 軸作成のおまじない
        xscale = (1./self.FS)*self.CHUNKSZ #x軸[s]
        self.fig_spectrogram.set_scale(xscale,yscale)
        self.freq = freq


    def mainLoop(self):
        super().mainLoop()

        N=self.CHUNKSZ
        # 時間更新
        df = 10
        self.cnt = self.cnt + df
        f0 = self.cnt
        if self.cnt > N: self.cnt=1

        # ステータスバー
        self.putStatusbar("f0:{}".format(f0))

        # 計算
        t = np.linspace(0,1,N)
        data = np.sin(2*np.pi*f0*t) + np.random.rand(t.size)
        win = np.hanning(N)
        spec = np.fft.rfft(data*win)/N
        psd = np.abs(spec)
        psd[0]=psd[2]
        psd[1]=psd[2]
        psd = 20*np.log10(psd)

        self.specgram_buffer=np.roll(self.specgram_buffer, -1, 0)
        self.specgram_buffer[-1:] = psd

        # Average
        average_spec = np.mean(self.specgram_buffer[-5:], axis=0)

        # 信号表示
        self.fig_wave.plot(t, data)

        # # スペクトル表示
        self.fig_spectrum.plot(self.freq, psd, clear=True)
        self.fig_spectrum.plot(self.freq, average_spec, pen=(0,255,0), clear=False)

        # # スペクトログラム表示
        self.fig_spectrogram.plot(self.specgram_buffer, True)
        # self.fig_spectrogram.seek(pos=f0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.lastWindowClosed.connect(app.quit)

    win = YourMainWindow()
    win.show()
    sys.exit(app.exec_())