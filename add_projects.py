import sys
from PyQt5 import QtWidgets
from check_db import *
from ui_add_sth import *


class Adding(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.add_objects = Ui_objects_add()
        self.add_objects.setupUi(self)

        self.add_objects.add_2.clicked.connect(self.db_add)

        self.check_db = CheckThread()

        self.add_objects.structure_n.setPlaceholderText("Введите состав")
        self.add_objects.structure_a.setPlaceholderText("Введите состав")

        self.add_objects.add_picture.clicked.connect(self.add_photo)
        self.ans = ""

        self.message = QtWidgets.QMessageBox()

    def db_add(self):
        name = self.add_objects.name.text().lower()
        analogue = self.add_objects.analogue.text().lower()
        price_name = self.add_objects.price_n.text().lower()
        price_analogue = self.add_objects.price_a.text().lower()
        structure_name = self.add_objects.structure_n.toPlainText()
        structure_analogue = self.add_objects.structure_a.toPlainText()
        photo = self.ans

        self.message.show()

        ans = self.check_db.thr_add_sth(
            name,
            analogue,
            price_name,
            price_analogue,
            structure_name,
            structure_analogue,
            photo,
        )

        if ans == "Введите название и аналог":
            self.message.setIcon(QtWidgets.QMessageBox.Warning)
            self.message.setWindowTitle("Ошибка")
            self.message.setText("Введите название и аналог")
        elif ans == "Введите название":
            self.message.setIcon(QtWidgets.QMessageBox.Warning)
            self.message.setWindowTitle("Ошибка")
            self.message.setText("Введите название")
        elif ans == "Введите аналог":
            self.message.setIcon(QtWidgets.QMessageBox.Warning)
            self.message.setWindowTitle("Ошибка")
            self.message.setText("Введите аналог")
        else:
            self.message.setIcon(QtWidgets.QMessageBox.Information)
            self.message.setWindowTitle("Добавлено")
            self.message.setText("Изменения сохранены!")
            self.close()

    def add_photo(self):
        self.ans = QtWidgets.QFileDialog.getOpenFileName(self, "Выбрать картинку", "")[
            0
        ].__str__()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Adding()
    mywin.setWindowTitle("Форма")
    mywin.show()
    sys.exit(app.exec_())
