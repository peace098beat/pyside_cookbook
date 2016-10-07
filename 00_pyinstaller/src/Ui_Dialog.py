# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/Ui_Dialog.ui'
#
# Created: Fri Oct  7 22:16:01 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 320)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(480, 320))
        Dialog.setStyleSheet("#Form{\n"
"background-color: #31363b;\n"
"}\n"
"")
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_header = QtGui.QLabel(Dialog)
        self.label_header.setMinimumSize(QtCore.QSize(0, 31))
        self.label_header.setStyleSheet("#label_header{\n"
"    background-color: rgb(170, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"    font: 90 12pt \"Oswald\";\n"
"\n"
"}")
        self.label_header.setObjectName("label_header")
        self.verticalLayout.addWidget(self.label_header)
        self.label_url = QtGui.QLabel(Dialog)
        self.label_url.setStyleSheet("#label_url{\n"
"    color: #eff0f1;\n"
"}")
        self.label_url.setObjectName("label_url")
        self.verticalLayout.addWidget(self.label_url)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_url = QtGui.QLineEdit(Dialog)
        self.lineEdit_url.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_url.setMouseTracking(True)
        self.lineEdit_url.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_url.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: #232629;\n"
"    padding: 5px;\n"
"    border-style: solid;\n"
"    border: 1px solid #76797C;\n"
"    border-radius: 2px;\n"
"    color: #eff0f1;\n"
"}")
        self.lineEdit_url.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineEdit_url.setDragEnabled(True)
        self.lineEdit_url.setReadOnly(False)
        self.lineEdit_url.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.horizontalLayout.addWidget(self.lineEdit_url)
        self.btn_download = QtGui.QPushButton(Dialog)
        self.btn_download.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btn_download.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #31363b;\n"
"    border-width: 1px;\n"
"    border-color: #76797C;\n"
"    border-style: solid;\n"
"    padding: 5px;\n"
"    border-radius: 2px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #31363b;\n"
"    border-width: 1px;\n"
"    border-color: #454545;\n"
"    border-style: solid;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 2px;\n"
"    color: #454545;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #3daee9;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #3daee9;\n"
"    padding-top: -15px;\n"
"    padding-bottom: -17px;\n"
"}")
        self.btn_download.setObjectName("btn_download")
        self.horizontalLayout.addWidget(self.btn_download)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_savedir = QtGui.QLabel(Dialog)
        self.label_savedir.setStyleSheet("#label_savedir{\n"
"    color: #eff0f1;\n"
"}")
        self.label_savedir.setObjectName("label_savedir")
        self.verticalLayout.addWidget(self.label_savedir)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_savedir = QtGui.QLineEdit(Dialog)
        self.lineEdit_savedir.setEnabled(True)
        self.lineEdit_savedir.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_savedir.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: #232629;\n"
"    padding: 5px;\n"
"    border-style: solid;\n"
"    border: 1px solid #76797C;\n"
"    border-radius: 2px;\n"
"    color: #aaa;\n"
"}")
        self.lineEdit_savedir.setReadOnly(True)
        self.lineEdit_savedir.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_savedir.setObjectName("lineEdit_savedir")
        self.horizontalLayout_2.addWidget(self.lineEdit_savedir)
        self.btn_opendir = QtGui.QPushButton(Dialog)
        self.btn_opendir.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btn_opendir.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #31363b;\n"
"    border-width: 1px;\n"
"    border-color: #76797C;\n"
"    border-style: solid;\n"
"    padding: 5px;\n"
"    border-radius: 2px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #31363b;\n"
"    border-width: 1px;\n"
"    border-color: #454545;\n"
"    border-style: solid;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 2px;\n"
"    color: #454545;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #3daee9;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #3daee9;\n"
"    padding-top: -15px;\n"
"    padding-bottom: -17px;\n"
"}")
        self.btn_opendir.setCheckable(False)
        self.btn_opendir.setObjectName("btn_opendir")
        self.horizontalLayout_2.addWidget(self.btn_opendir)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_header.setText(QtGui.QApplication.translate("Dialog", " FiApp", None, QtGui.QApplication.UnicodeUTF8))
        self.label_url.setText(QtGui.QApplication.translate("Dialog", "Youtube URL", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_url.setText(QtGui.QApplication.translate("Dialog", "https://www.youtube.com/watch?time_continue=233&v=spnjTzuVBO0", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_download.setText(QtGui.QApplication.translate("Dialog", "download", None, QtGui.QApplication.UnicodeUTF8))
        self.label_savedir.setText(QtGui.QApplication.translate("Dialog", "Save Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_savedir.setText(QtGui.QApplication.translate("Dialog", "Desktop", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_opendir.setText(QtGui.QApplication.translate("Dialog", "browe", None, QtGui.QApplication.UnicodeUTF8))

