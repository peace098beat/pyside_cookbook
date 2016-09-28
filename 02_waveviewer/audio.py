#! -*- coding: utf-8 -*-
import pyaudio
import wave
import time
import numpy as np



## UTILITY
def byteToPCM(data, sample_width):
    d_type = 'float'
    if sample_width == 2:
        d_type = 'short'
    return np.frombuffer(data, dtype=d_type)


def pcmToFloat(sig, type='float32'):
    sig = np.asarray(sig)
    if sig.dtype.kind != 'i':
        raise TypeError('signal must be integer')
    type = np.dtype(type)
    if type.kind != 'f':
        raise TypeError('type must be float')

    return sig.astype(type) / type.type(-np.iinfo(sig.dtype).min)


def floatToPCM(sig, dtype='int16'):
    return (sig * np.iinfo(dtype).max).astype(dtype)


p = pyaudio.PyAudio()
wf = wave.open("audio2.wav")
sampwidth = wf.getsampwidth()

# サンプルサイズ[byte]
sampwidth = wf.getsampwidth()
# チャンネル数(モノラル:1,ステレオ:2)
channels = wf.getnchannels()
# サンプリングレート
fs = wf.getframerate()
# オーディオフレーム数
framsize = wf.getnframes()



def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    sig = pcmToFloat(byteToPCM(data, sampwidth))

    return (data, pyaudio.paContinue)

stream = p.open(
    format = p.get_format_from_width(sampwidth),
    channels = channels,
    rate = fs,
    output = True,
    stream_callback = callback)


print('>>Audio Play  ')
stream.start_stream()
# while stream.is_active():
#     time.sleep(0.1)
time.sleep(1)

stream.stop_stream()
stream.close()
p.terminate()

print '== Audio:play ..end =='

# ファイルポインタをオーディオストリームの先頭に戻す
wf.rewind()

