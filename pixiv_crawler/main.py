import sys
import asyncio
import main_design
import pixivpy3

from pixivpy3 import AppPixivAPI
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


class LoginScreen(QMainWindow, main_design.Ui_login_form):
    def __init__(self, parent=None):
        super(LoginScreen, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login_push)

    def login_push(self):
        self.ID = self.lineEdit.text()
        self.PW = self.lineEdit_2.text()
        try:
            api = AppPixivAPI()
            api.login(self.ID, self.PW)
            print('connected')
        except pixivpy3.utils.PixivError:
            msgbox = QMessageBox
            msgbox.critical(self, "Error", "Invaild ID or Password", msgbox.Ok)


if __name__ == "__main__":
    main = QApplication(sys.argv)
    app = LoginScreen()
    app.show()
    sys.exit(main.exec_())