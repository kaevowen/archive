from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtGui import QPixmap

import sys
import urllib.request

import main_gui
import core


class MainWindow(QMainWindow, main_gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.pushButton.clicked.connect(self.Push_Button)
        self.lineEdit.textChanged.connect(self.LineEdit_Text_Changed)


    def LineEdit_Text_Changed(self):
        try:
            url = core.Get_YT_Thumbnail(self.lineEdit.text())
            data = urllib.request.urlopen(url).read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            self.thumbnail.setPixmap(pixmap)
            print("load thumbnail")
            self.thread = ThreadClass(self.lineEdit.text())
        except AttributeError:
            pass
        except:
            print("Invalid URL")
                
    def Push_Button(self):
        self.thread.start()


class ThreadClass(QThread):
    def __init__(self, value, parent=None):
        super(ThreadClass, self).__init__(parent)
        self.value = value

    def run(self):
        core.Download(self.value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MW = MainWindow()
    MW.show()
    sys.exit(app.exec_())