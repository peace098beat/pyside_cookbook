#! coding:utf-8
"""

PyQtgraph Spectrogram
http://amyboyle.ninja/Pyqtgraph-live-spectrogram

"""
import numpy as np
import pyaudio


class MicrophoneRecorder():

    def __init__(self, chunksize=1024, fs=44100):
        self.CHUNKSZ=chunksize
        self.FS = fs

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,
                            channels=1,
                            rate=self.FS,
                            input=True,
                            frames_per_buffer=self.CHUNKSZ)

    def read(self):
        data = self.stream.read(self.CHUNKSZ)
        y = np.fromstring(data, 'int16')/((2**15)-1)
        return y

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    def __del__(self):
        self.close()
        super().__del__(self)