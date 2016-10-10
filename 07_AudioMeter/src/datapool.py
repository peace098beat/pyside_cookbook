#! coding:utf-8
"""
課題:
二つのオブジェクトから参照されているとき、
pool内のデータがなくなる...
"""

from collections import deque
import numpy as np

__all__ = ["DataPool"]
class DataPool:
    def __init__(self ):
        self.maxsize = 10
        self.pool = deque(maxlen=self.maxsize)

    def get_data(self):
        try:
            d=b''
            for i in range(4):
                d += self.pool.pop()
            amp = ((2**16)/2)-1
            return np.fromstring(d, dtype=np.dtype('int16'))/ float(amp)
        except IndexError:
            return None

    def add_data(self, d):
        return self.pool.appendleft(d)


if __name__ == '__main__':
    p = DataPool()
    import numpy as np

    for i in range(20):
        p.add_data(np.random.random((i,1)))

    for i in range(20):
        print(p.get_data())

