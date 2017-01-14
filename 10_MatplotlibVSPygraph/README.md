

# PySideを使ったスピード測定

PySideを使って音声処理をしているとどうしてもリアルタイムでグラフをヌメヌメ動かさないといけない。実装の手軽さからMatplotlibを使ってこれまでやっていたが、遅い。遅い。遅い。10FPSぐらいしかでない。高速化する方法が和歌来。そこで、pyqtgraphとQGraphicsを使って速度を比較してみる。QPainerとPyOpenGLは次回に追加予定

## 対戦表

- Matplotlib pyplot.plot
- Matplotlib pyplot.axex.set_ydata()
- PyQtGraph pg.plot
- QGraphics 独自実装


## 対戦方式

1. QMainWindow内部で120FPSでメインループを呼び出す。

2. メインループ内でsin波形を生成しプロット <= このときのFPSを比較する。

## 結果

### 結果1  N=2048
- グラフなし : 120FPS
- Matplotlib pyplot.plot : 9FPS
- Matplotlib pyplot.axex.set_ydata() : 15FPS
- PyQtGraph pg.plot : 120FPS
- QGraphics 独自実装 : 70～120FPS (なぜか変動する)

### 結果2  N=10240
- グラフなし : 120 fps
- Matplotlib pyplot.plot : 4fps
- Matplotlib pyplot.axex.set_ydata() : 5fps
- PyQtGraph pg.plot : 60fps
- QGraphics 独自実装 : 40～100FPS (なぜか変動する)


QGraphicsを使った実装は安定して早い。また、PyQtGraphも早い。PyQtGraphはウラでQGraphicsを使って、いろいろ高速化の工夫がされているので両方とも同じような速度がでているのはよい。また、PyQtGraphは高速化の工夫からか、fpsが変動し、たまにかなり高い値をだすのも面白い。

![demo](demo/demo1.gif)


