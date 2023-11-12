from PyQt5 import QtCore, QtGui, QtWidgets
from handler.db_handler import *


class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    # thr - threshold threquiremen, порог требования

    def thr_login(self, name, passw):
        return login(name, passw, self.mysignal)

    def thr_register(self, name, passw):
        return register(name, passw, self.mysignal)

    def thr_products(self, name):
        return products(name)

    def thr_analogue(self, name):
        return analogue(name)

    def thr_check_name(self, name):
        return check(name)

    def thr_price(self, name):
        return price(name)

    def thr_struck(self, name):
        return struck(name)

    def thr_popular(self):
        return popular()
