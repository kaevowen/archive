import sys
import cv2

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QThread

from time import sleep


import numpy as np

import process_select
import image_cord
import select_design

PROCNAME = "exefile.exe"

client = []
PyHandle = []


class MyApp(QMainWindow, select_design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.setupUi(self)

        for i in process_select.get_processes(PROCNAME):
            text = f"{process_select.get_window_text(process_select.get_hwnds(i.pid)[0])}"
            if text in client:
                pass
            else:
                client.append(text)
            PyHandle.append(i)

        self.listWidget.addItems(client)
        self.listWidget.itemClicked.connect(self.Clicked)
        self.listWidget.itemDoubleClicked.connect(self.DoubleClicked)
    
    # create thumbnail when client selected
    def Clicked(self, qmodelindex):

        item = self.listWidget.currentItem()
        process = PyHandle[client.index(item.text())]
        cs = image_cord.capture_screen(process_select.get_hwnds(process.pid)[0])
        buf = image_cord.ThumbFromBuffer(cs, (196, 196))
        buf = buf.convert("RGBA")
        data = buf.tobytes("raw", "RGBA")
        qim = QImage(data, buf.size[0], buf.size[1], QImage.Format_ARGB32)
        pix = QPixmap.fromImage(qim)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setPixmap(pix)
        self.verticalLayout_2.addWidget(self.label2)

    # create ROI window
    def DoubleClicked(self):
        item = self.listWidget.currentItem()

        print("Selected Client : ", item.text())

        process = PyHandle[client.index(item.text())]
        cs = image_cord.capture_screen(process_select.get_hwnds(process.pid)[0])
        hwnd = process_select.get_hwnds(process.pid)[0]

        nparr = np.frombuffer(cs, dtype='uint8')
        img_np = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)
        r = cv2.selectROI("Press Enter to continue...", img_np, False, False)
        cv2.destroyAllWindows()

        self.thread = ThreadClass(item, hwnd, r)
        self.thread.start()
        self.hide()


class ThreadClass(QThread):
    def __init__(self, item, hwnd, r, parent=None):
        super(ThreadClass, self).__init__(parent)
        self.item = item
        self.h = hwnd
        self.r = r

    def run(self):
        while True:
            process = PyHandle[client.index(self.item.text())]
            cs = image_cord.capture_screen(self.h)
            nparr = np.frombuffer(cs, dtype='uint8')
            img_np = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)
            self.imCrop = img_np[int(self.r[1]):int(self.r[1] + self.r[3]),
            int(self.r[0]):int(self.r[0] + self.r[2])]
            image_cord.Image_search(self.imCrop)
            sleep(1)


if __name__ == "__main__":
    a = QApplication(sys.argv)
    app = MyApp()
    app.show()

    sys.exit(a.exec_())
