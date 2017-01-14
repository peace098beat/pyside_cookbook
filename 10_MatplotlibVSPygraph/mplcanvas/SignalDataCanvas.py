#! coding:utf-8
"""
SignalDataCanvas

Created by 0160929 on 2016/03/24 12:23
"""

from .BaseCanvas import BaseMplCanvas
import numpy as np

class SignalDataCanvas(BaseMplCanvas):
    def __init__(self, parent=None):
        # super(SignalDataCanvas, self).__init__(parent)
        super().__init__(parent)
        pass

    # ***************************************
    # Abstruct
    # ***************************************
    def plot(self, data):
        self.axes.plot(data)
        self.canvas_update()



class SignalDataCanvasFast(BaseMplCanvas):
    def __init__(self, parent=None):
        # super(SignalDataCanvas, self).__init__(parent)
        super().__init__(parent)

    # ***************************************
    # Abstruct
    # ***************************************
    def plot(self, data):

        _ydata = self.line.get_ydata()
        _ydata = np.array(_ydata)

        if _ydata.size != data.size:
            lines = self.axes.plot(data)
            self.line = lines[0]

        self.line.set_ydata(data)
        
        # self.axes.plot(data)
        self.canvas_update()
