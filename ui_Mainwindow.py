# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 538)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(560, 310, 201, 111))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.search = QtWidgets.QLineEdit(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(20, 20, 551, 22))
        self.search.setObjectName("search")
        self.pushButtonSearch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearch.setGeometry(QtCore.QRect(590, 20, 131, 28))
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(10, 90, 120, 121))
        self.groupBox.setObjectName("groupBox")
        self.fastfood = QtWidgets.QCheckBox(self.groupBox)
        self.fastfood.setGeometry(QtCore.QRect(10, 30, 81, 20))
        self.fastfood.setObjectName("fastfood")
        self.meat = QtWidgets.QCheckBox(self.groupBox)
        self.meat.setGeometry(QtCore.QRect(10, 60, 101, 20))
        self.meat.setObjectName("meat")
        self.forchildren = QtWidgets.QCheckBox(self.groupBox)
        self.forchildren.setGeometry(QtCore.QRect(10, 90, 91, 20))
        self.forchildren.setObjectName("forchildren")
        self.labelname = QtWidgets.QLabel(self.centralwidget)
        self.labelname.setGeometry(QtCore.QRect(150, 140, 131, 31))
        self.labelname.setObjectName("labelname")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(150, 90, 101, 21))
        self.name.setObjectName("name")
        self.nameN = QtWidgets.QLabel(self.centralwidget)
        self.nameN.setGeometry(QtCore.QRect(320, 90, 91, 21))
        self.nameN.setObjectName("nameN")
        self.labelnameN = QtWidgets.QLabel(self.centralwidget)
        self.labelnameN.setGeometry(QtCore.QRect(310, 130, 151, 51))
        self.labelnameN.setObjectName("labelnameN")
        self.similar_name = QtWidgets.QLabel(self.centralwidget)
        self.similar_name.setGeometry(QtCore.QRect(20, 60, 371, 21))
        self.similar_name.setMouseTracking(True)
        self.similar_name.setObjectName("similar_name")
        self.popular_lable = QtWidgets.QLabel(self.centralwidget)
        self.popular_lable.setGeometry(QtCore.QRect(150, 220, 121, 21))
        self.popular_lable.setObjectName("popular_lable")
        self.strukture = QtWidgets.QPushButton(self.centralwidget)
        self.strukture.setGeometry(QtCore.QRect(610, 100, 101, 28))
        self.strukture.setObjectName("strukture")
        self.prise_value = QtWidgets.QPushButton(self.centralwidget)
        self.prise_value.setGeometry(QtCore.QRect(610, 140, 101, 28))
        self.prise_value.setObjectName("prise_value")
        self.popular = QtWidgets.QLineEdit(self.centralwidget)
        self.popular.setGeometry(QtCore.QRect(160, 260, 311, 151))
        self.popular.setObjectName("popular")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.menu_2.addAction(self.action_4)
        self.menu_2.addAction(self.action_5)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Фильтры\n"
"Состав\n"
"Озывы\n"
"Цена\n"
"Разделы\n"
"Персонализация(из анкеты)"))
        self.pushButtonSearch.setText(_translate("MainWindow", "Искать продукты"))
        self.groupBox.setTitle(_translate("MainWindow", "Фильтры"))
        self.fastfood.setText(_translate("MainWindow", "Фастфуд"))
        self.meat.setText(_translate("MainWindow", "Мясо, птица"))
        self.forchildren.setText(_translate("MainWindow", "Для детей"))
        self.labelname.setText(_translate("MainWindow", "Тут будет название"))
        self.name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Назавание</span></p></body></html>"))
        self.nameN.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Похожие</span></p></body></html>"))
        self.labelnameN.setText(_translate("MainWindow", "Тут будут похожие"))
        self.similar_name.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.popular_lable.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Популярные</span></p></body></html>"))
        self.strukture.setText(_translate("MainWindow", "Узнать состав"))
        self.prise_value.setText(_translate("MainWindow", "Узнать цену"))
        self.menu_2.setTitle(_translate("MainWindow", "Заказы"))
        self.menu_3.setTitle(_translate("MainWindow", "Корзина"))
        self.menu.setTitle(_translate("MainWindow", "Главная"))
        self.action.setText(_translate("MainWindow", "Регион"))
        self.action_2.setText(_translate("MainWindow", "Каталог"))
        self.action_4.setText(_translate("MainWindow", "Недавние"))
        self.action_5.setText(_translate("MainWindow", "Любимые"))
