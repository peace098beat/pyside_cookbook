
# Tiny2dHistgramViewer

Image(HSV) 2D Histogram Viewer

## Feature

- Add H vs V Figure
- Add Setting calcHistogram Parameter

## Version

- ver0.1 (2016/10/25) 
 - Image Preview
 - H vs S Figure
 - Figure Clipboard copy

## Requirement

- Python3.4

- PySide

```bash
# wheel download: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyside
pip install PySide-1.2.2-cp34-none-win_amd64.whl
```

- OpenCV

```bash
# wheel download: http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv
pip install opencv_python-3.1.0-cp34-cp34m-win_amd64.whl
```

- Numpy

## Author

tomoyuki_nohara@post.pioneer.co.jp


## ISSUE

- execute to matplotlib 

reinstall pyinstaller developer's branch

```bash
pip uninstall pyinstaller

pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip
```

