# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'local_alarm_main_design.ui',
# licensing of 'local_alarm_main_design.ui' applies.
#
# Created: Mon Nov 18 01:17:59 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(168, 186)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 10, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(10, 50, 141, 111))
        self.label2.setObjectName("label2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "로컬알람기", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "대기중...", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "클라 선택", None, -1))
        self.label2.setText(QtWidgets.QApplication.translate("MainWindow", " ", None, -1))

