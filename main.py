import sys
from PyQt5 import QtWidgets
from check_db import *
from ui_WinRegLog import *
from MainWindow import Window


class RegLog(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.win = Window()

        self.ui.pushButton.clicked.connect(self.reg)

        self.ui.pushButton_2.clicked.connect(self.auth)

        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, "Оповещение", value)

    @check_input
    def auth(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()

        if self.check_db.thr_login(name, passw):
            self.win.setWindowTitle("Главная страница")
            self.win.show()
            self.close()

    @check_input
    def reg(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()

        if self.check_db.thr_register(name, passw):
            self.win.show()
            self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = RegLog()
    mywin.setWindowTitle("Регистрация/Авторизация")
    mywin.show()
    sys.exit(app.exec_())
