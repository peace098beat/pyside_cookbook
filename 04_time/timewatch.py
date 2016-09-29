#! coding:utf-8
"""
timewatch

Created by 0160929 on 2016/05/18 15:42
"""

# ***********************************************************
# 時間計測用デコレータ
# ***********************************************************
# :使い方:
#
# from timewatch import timewatch
#
# @timewatch
# def analys(*args, **kwargs):
#     import time
#     time.sleep(10)
#     pass

THR_MS = 0.1 # THR_MS以上の場合だけ表示

def timewatch(func):
    def wrapper(*args, **kwargs):
        import time

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        dt = (end - start) * 1000.
        if dt  > THR_MS:
            # print("@Time Watch -- %-20s : %-5.2f[ms]" % (func.__name__, dt))
            pass
        return result

    return wrapper

