#! coding:utf-8
"""
mpl_images.py

Created by 0160929 on 2016/10/24 16:04
"""
import sys

import numpy as np
from PySide.QtGui import QApplication

import cv2
from mpl_toolkits.mplot3d import Axes3D
tmp=Axes3D
from mpl import BaseMplCanvas


def clac_2dhist(img_path):
    # img = cv2.imread('img/photo.jpg')
    img = cv2.imread(img_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    channels = [0, 1]  # 0:Hue, 1:Satu, 2:Value
    hbin, sbin = 12, 12
    bins = [hbin, sbin]  # H:180, S:256
    ranges = [0, 180, 0, 256]  # Hue(0,180), Saturation(0,256)
    hist = cv2.calcHist([hsv], channels, None, bins, ranges)

    hsize, ssize = hist.shape  # 180, 256
    colors = [cv2.cvtColor(np.uint8([[[int(i), 255, 1]]]), cv2.COLOR_HSV2RGB) for i in np.linspace(0, 180, hbin)]

    return hist, hsize, ssize, colors




class Image2DHistogram(BaseMplCanvas):
    def __init__(self):
        BaseMplCanvas.__init__(self)
        self.axes = self.fig.add_subplot(111, projection='3d')

    # ***************************************
    # Abstruct
    # ***************************************
    def plot(self, img_path):
        self.axes.cla()

        hist, hsize, ssize, colors = clac_2dhist(img_path)

        assert hsize == hist.shape[0]
        assert ssize == hist.shape[1]
        ax = self.axes

        for c, i in zip(colors, range(hsize)):
            xs = np.arange(ssize)
            ys = hist[i]
            z = i
            cs = [c[0, 0, :].tolist()] * len(xs)
            ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)

        ax.set_ylabel('H : Hue')
        ax.set_xlabel('S : Saturation')
        ax.set_zlabel('P')
        # plt.show()
        self.canvas_update()

        return self


def main():
    app = QApplication(sys.argv)
    # app.setStyle('plastique')
    win = BaseMplCanvas()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
