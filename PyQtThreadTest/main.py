from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, QThread, QObject

import main_design
import sys
import time


class MyApp(QMainWindow, main_design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.startProgressBar)
            
    def startProgressBar(self):
        self.thread = ThreadClass()
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()

    def setProgressVal(self, val):
        self.progressBar.setValue(val)


class ThreadClass(QThread):
    change_value = pyqtSignal(int)
    
    def run(self):
        cnt = 0
        while cnt < 100:
            cnt += 1
            time.sleep(0.01)
            self.change_value.emit(cnt)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    app = MyApp()
    app.show()
    sys.exit(a.exec_())
