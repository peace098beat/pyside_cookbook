import cv2
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

img = cv2.imread('img/photo.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

channels = [0,1] #0:Hue, 1:Satu, 2:Value
hbin , sbin = 64,12
bins = [hbin,sbin] # H:180, S:256
ranges = [0,180, 0, 256] #Hue(0,180), Saturation(0,256)
hist = cv2.calcHist([hsv],channels,None, bins, ranges)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# ax = fig.add_subplot(111)

xsize, zsize = hist.shape #180, 256

colors = [cv2.cvtColor(np.uint8([[[int(i), 255, 1]]]), cv2.COLOR_HSV2RGB) for i in np.linspace(0,180, hbin)]

for c, i in zip(colors, range(xsize)):
    xs = np.arange(zsize)
    ys = hist[i]
    z = i
    cs = [c[0,0,:].tolist()] * len(xs)
    ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)

ax.set_xlabel('S : Saturation')
ax.set_ylabel('H : Hue')
ax.set_zlabel('P')
plt.show()