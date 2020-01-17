import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt, QThread

import main_design
import process_select_code
import time


class MainWindow(QMainWindow, main_design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.Select_Eve_Client = process_select_code.MyApp()

        self.setupUi(self)
        self.pushButton.clicked.connect(self.Push_Button)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.thread = ThreadClass(self.label)

    def Push_Button(self):
        self.Select_Eve_Client.show()
        self.thread.start()


class ThreadClass(QThread):
    def __init__(self, label, parent=None):
        super(ThreadClass, self).__init__(parent)
        self.label = label

    def run(self):
        while True:
            for i in range(4):
                self.label.setText('작동중'+'.'*i)
                time.sleep(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MW = MainWindow()
    MW.show()
    sys.exit(app.exec_())