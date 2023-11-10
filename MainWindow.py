import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Mainwindow import *
from check_db import *

# import sqlite3


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.w = Ui_MainWindow()
        self.w.setupUi(self)

        self.check_db = CheckThread()

        self.w.pushButtonSearch.clicked.connect(self.search)

    def search(self):
        name = self.w.search.text()

        ans = self.check_db.thr_products(name)
        ans2 = self.check_db.thr_analogue(name)
        strans2 = ""

        if "Введите корректное значение" not in ans:
            self.w.labelname.setText("".join(*ans[0]))
        else:
            self.w.labelname.setText(ans)
        if "Не найдено" not in ans2:
            for i in ans2:
                strans2 += "".join(*i) + "\n"
            self.w.labelnameN.setText(strans2)
        else:
            self.w.labelnameN.setText(ans2)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Window()
    mywin.show()
    sys.exit(app.exec_())
