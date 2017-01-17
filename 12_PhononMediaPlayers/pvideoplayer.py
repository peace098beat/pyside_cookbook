#! coding:utf-8
"""
pVideoplayer.py

Created by 0160929 on 2017/01/12 17:28
"""
import os
import sys

from PySide.QtGui import *
from PySide.QtCore import *
from PySide.phonon import Phonon


class PhononVideoPlayer(QWidget):
    def __init__(self, url=None, parent=None):
        QWidget.__init__(self)
        self.setWindowTitle('Video Player')

        # 再生ファイル
        self.url = url

        # Phonon Objects
        # ***************
        self.media = Phonon.MediaObject(self)
        self.video = Phonon.VideoWidget(self)
        # self.video.setMinimumSize(180, 280)
        self.audio = Phonon.AudioOutput(Phonon.VideoCategory, self)
        Phonon.createPath(self.media, self.audio)
        Phonon.createPath(self.media, self.video)

        # Timer
        # *****
        self.media.setTickInterval(1 / 30 * 1000)  # [ms]
        self.media.tick.connect(self.tock)
        self.time = 0

        # UI 生成
        # ***************
        self.setupUI()

    def setupUI(self):

        """UI生成シーケンス.
        可視性を高めるため別に記述
        """

        # Ctrl UI
        self.btn_start = QPushButton('PLAY', self)
        self.volume_slider = Phonon.VolumeSlider(self)
        self.volume_slider.setAudioOutput(self.audio)
        self.seek_slider = Phonon.SeekSlider(self.media, self)
        self.seek_slider.setSingleStep(1 / 30 * 1000)  # [ms]

        # Status Label
        self.status_label = QLabel(self)
        self.status_label.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        # Layout
        layout = QGridLayout(self)
        # 一段目
        layout.addWidget(self.video, 0, 0, 1, 3)
        # 二段目
        layout.addWidget(self.btn_start, 1, 0)
        layout.addWidget(self.volume_slider, 1, 1)
        layout.addWidget(self.status_label, 1, 2)
        layout.setRowStretch(1, 1)
        # 三段目
        layout.addWidget(self.seek_slider, 2, 0, 1, 3)

        # Signal
        self.media.stateChanged.connect(self._handle_StateChanged)
        self.media.finished.connect(self.restart)
        self.btn_start.clicked.connect(self._handle_BtnStart)

    def _handle_StateChanged(self, newstate, oldstate):

        """MediaPlayerの状態遷移時のコールバック
        ボタンの文字を変更している．
        """
        print(newstate)

        if newstate == Phonon.PlayingState:
            self.btn_start.setText('PAUSE')
        elif (newstate != Phonon.LoadingState and newstate != Phonon.BufferingState):
            self.btn_start.setText('PLAY')
            if newstate == Phonon.ErrorState:
                source = self.media.currentSource().fileName()
                print('ERROR: could not play: %s' % source)
                print('  %s' % self.media.errorString())

    def _handle_BtnStart(self):

        """再生/停止を行うボタンのコールバック"""

        if self.media.state() == Phonon.PlayingState:
            # self.media.stop()
            self.media.pause()
        else:
            self.media.play()

    def set_url(self, url):

        """外部から再生ファイルをセット.
        ファイルがセットされると状態遷移しStateChangedがコールされる"""

        self.url = url
        assert os.path.exists(url)
        self.media.setCurrentSource(Phonon.MediaSource(url))

    def tock(self, time):
        """一定時間ごとに呼び出される"""
        self.time = time
        time = time / 1000.
        h = int(time / 3600.)
        m = int((time - 3600 * h) / 60.)
        s = int(time - 3600 * h - m * 60)
        self.status_label.setText('%02d:%02d:%02d' % (h, m, s))

    @Slot()
    def restart(self):
        self.media.seek(0)
        self.media.play()
        self.media.play()


def main():
    VIDEO_PATH = "data/EXP001_09.avi"
    app = QApplication(sys.argv)
    window = PhononVideoPlayer(url=VIDEO_PATH)
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
