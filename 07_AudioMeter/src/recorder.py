#! coding:utf-8
from collections import namedtuple

import pyaudio
import numpy as np

from datapool import DataPool

# Setting
AudioConfig = namedtuple('AudioConfig', 'chunk rate channels')
audio_config = AudioConfig(1024, 44100, 1)


class Recorder(object):
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.pa.open(format=pyaudio.paInt16,
                                   channels=audio_config.channels,
                                   rate=audio_config.rate,
                                   frames_per_buffer=audio_config.chunk,
                                   input=True,
                                   stream_callback=self.recorde_callback,
                                   )
        self.pool = DataPool()

    def get_pool(self):
        return self.pool

    def recorde_callback(self, indata, framecount, time_info, status):
        # PCM = np.frombuffer(indata, dtype="int16")
        # print(framecount)
        self.pool.add_data(indata)
        return (None, pyaudio.paContinue)

    def start(self):
        self.stream.start_stream()

    def stop(self):
        self.stream.stop_stream()

    def close(self):
        self.stream.close()
        self.pa.terminate()

    def __del__(self):
        self.close()


if __name__ == '__main__':
    rec = Recorder()
    rec.start()

    import time

    while 1:
        time.sleep(1)
        d = rec.pool.get_data()
        print("que {}".format(d))
