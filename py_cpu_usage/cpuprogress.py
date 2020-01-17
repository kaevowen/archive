from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal

import progress
import sysInfo
import sys


class MyApp(QtWidgets.QMainWindow, progress.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.setupUi(self)

        self.threadclass = ThreadClass()
        self.threadclass.finished.connect(self.update_progress_bar)
        self.threadclass.start()

    @pyqtSlot(float)
    def update_progress_bar(self, val):
        self.progressBar.setValue(val)


class ThreadClass(QtCore.QThread):
    finished = pyqtSignal(float)

    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)

    def run(self):
        while True:
            val = sysInfo.getCPU()
            self.finished.emit(val)


if __name__ == "__main__":
    a = QtWidgets.QApplication(sys.argv)
    app = MyApp()
    app.show()
    sys.exit(a.exec_())
