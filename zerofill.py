#coding: utf-8
import wave
import sys
import os
import numpy as np


DURATION_MS = 500 # ms
ZERO_PAD_FRONT_MS = 50 # ms


# ルートディレクトリ
DIRNAME = os.path.dirname(sys.argv[0]) 

import glob
# パス内の全ての"指定パス+ファイル名"と"指定パス+ディレクトリ名"を要素とするリストを返す
files = glob.glob(os.path.join(DIRNAME, '*.wav'))



def triming_wave(_file_name):
	# ----------------------
	TRIMED_DIRNAME = "Trimed"
	try:
		os.mkdir(os.path.join(DIRNAME, TRIMED_DIRNAME))
	except:
		pass

	out_filename = os.path.join(TRIMED_DIRNAME, _file_name)


	"""読み込み作業"""
	wave_file = wave.open(os.path.join(DIRNAME, _file_name),"r") #Open
	fs = wave_file.getframerate()

	# データの読み出し
	x = wave_file.readframes(wave_file.getnframes()) #frameの読み込み
	x = np.frombuffer(x, dtype= "int16") #numpy.arrayに変換

	# ----------------------
	# フェードインアウトウィンドウ
	# ----------------------
	window = np.zeros(x.size, dtype=np.float)
	fade_front_len_samp = int(x.size * 0.01)
	fade_end_len_samp = int(x.size * 0.01)

	for i in range(window.size):
		if i < fade_front_len_samp:
			window[i] = (1./fade_front_len_samp) * i
		elif (x.size - fade_end_len_samp) < i:
			window[i] = 1 - (1./fade_end_len_samp)* (i-(x.size - fade_end_len_samp))
		else:
			window[i] = 1

	assert x.size == window.size

	x = x * window
	print("X.size {}".format(x.size))

	# ----------------------
	# 先頭にゼロフィル
	# ----------------------
	total_length = int(DURATION_MS/1000 * fs)
	y = np.zeros(total_length, dtype="int16")
	assert y.size > x.size, "ysize{} > xsize{}".format(y.size, x.size)

	zeropadding_front_smp = int(ZERO_PAD_FRONT_MS/1000 * fs)

	y[zeropadding_front_smp:zeropadding_front_smp+x.size] = x


	"""書き込み作業"""
	write_wave = wave.Wave_write(os.path.join(DIRNAME, out_filename))
	write_wave.setparams(wave_file.getparams())
	write_wave.writeframes(y)
	write_wave.close()
	print("Trimed {}".format(_file_name))





if __name__ == '__main__':
	for file in files:

		try:
			triming_wave(file)
		except Exception as e:
			print("Error : {}".format(os.path.basename(file)))
			print("Error {}".format(e))
		else:
			print("Success : {}".format(os.path.basename(file)))
			pass
		finally:
			pass
