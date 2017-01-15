

# PySideを使ってスペクトログラム描画(高速)

PyAudioを使ってリアルタイムレコーディングをしながら描画

PySideを使って音声処理をしているとどうしてもリアルタイムでグラフをヌメヌメ動かさないといけない。実装の手軽さからMatplotlibを使ってこれまでやっていたが、遅い。遅い。遅い。10FPSぐらいしかでない。高速化する方法が和歌来。そこで、pyqtgraphとQGraphicsを使って速度を比較してみる。QPainerとPyOpenGLは次回に追加予定

![demo](demo/demo1.gif)


# 構成
- Python3.3
- PySide
- PyQtGraph
- PyQudio

## 環境構築メモ
matplotlibはpython3.4だとエラーなので、3.3でいれる
```
conda create --name pyside33 python=3.3 pyside matplotlib numpy pyqtgraph
```


# 参考

- PyQtgraph Spectrogram

http://amyboyle.ninja/Pyqtgraph-live-spectrogram
