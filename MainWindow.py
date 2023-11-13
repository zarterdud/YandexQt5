import sys
from PyQt5 import QtWidgets
from ui_Mainwindow import *
from check_db import *
from add_projects import Adding


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self)

        self.check_db = CheckThread()

        self.main_window.pushButtonSearch.clicked.connect(self.search)

        self.main_window.prise_value.clicked.connect(self.more_detalied)

        self.main_window.popular.setEnabled(False)
        self.main_window.popular.appendPlainText(self.check_db.thr_popular())

        self.main_window.add.clicked.connect(self.add_sth)

        self.add_objects = Adding()

    def search(self):
        name = self.main_window.search.text().lower()

        ans = self.check_db.thr_products(name)
        ans2 = self.check_db.thr_analogue(name)
        strans2 = ""

        if "Введите корректно" not in ans:
            self.main_window.labelname.setText(*ans[0])
            self.main_window.similar_name.setText("")
        else:
            self.main_window.labelname.setText(ans)

            if self.check_db.thr_check_name(name) != None:
                self.main_window.similar_name.setText(
                    f"Может вы имели ввиду: {self.check_db.thr_check_name(name)}"
                )
            else:
                self.main_window.similar_name.setText("")

        if "Не найдено" not in ans2:
            for i in ans2:
                strans2 += "".join(*i) + "\n"
            self.main_window.labelnameN.setText(strans2)
        else:
            self.main_window.labelnameN.setText(ans2)

    def more_detalied(self):
        name = self.main_window.search.text().lower()

        mes = QtWidgets.QMessageBox()
        mes.setWindowTitle("Детали")

        photo = self.check_db.thr_picture(name)

        if name != "" and self.check_db.thr_products(name) != "Введите корректно":
            price = self.check_db.thr_price(name)
            detalied = self.check_db.thr_struck(name)
            mes.setText(price)
            mes.setStandardButtons(QtWidgets.QMessageBox.Close)
            mes.setDetailedText(detalied)
            mes.setIcon(QtWidgets.QMessageBox.Information)
            mes.setIconPixmap(QtGui.QPixmap(photo))
        elif name == "":
            mes.setText("Введите значение")
            mes.setIcon(QtWidgets.QMessageBox.Warning)
            mes.setIconPixmap(QtGui.QPixmap('photos/error.png'))
        else:
            mes.setText("Введите корректное значение")
            mes.setIcon(QtWidgets.QMessageBox.Warning)
            mes.setIconPixmap(QtGui.QPixmap('photos/error.png'))

        mes.exec_()

    def add_sth(self):
        self.add_objects.setWindowTitle("Форма")
        self.add_objects.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Window()
    mywin.setWindowTitle('Главная страница')
    mywin.show()
    sys.exit(app.exec_())
