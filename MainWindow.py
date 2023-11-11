import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Mainwindow import *
from check_db import *


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

        if "Введите корректно" not in ans:
            self.w.labelname.setText(*ans[0])
            self.w.similar_name.setText('')
        else:
            self.w.labelname.setText(ans)

            if self.check_db.thr_check_name(name) != None:
                self.w.similar_name.setText(
                    f"Может вы имели ввиду: {self.check_db.thr_check_name(name)}"
                )
            else:
                self.w.similar_name.setText('')

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
