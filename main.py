# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class Mainwindow(QWidget):
    def __init__(self):
        super(Mainwindow, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.ui.btn_sum.clicked.connect(self.sum)
        self.ui.btn_sub.clicked.connect(self.sub)
        self.ui.btn_div.clicked.connect(self.div)
        self.ui.btn_mul.clicked.connect(self.mul)
        self.ui.btn_neg.clicked.connect(self.neg)
        self.ui.btn_per.clicked.connect(self.per)
        self.ui.btn_clean.clicked.connect(self.clean)

        self.ui.btn_equal.clicked.connect(self.equal)
        self.ui.btn_0.clicked.connect(self.num0)
        self.ui.btn_1.clicked.connect(self.num1)
        self.ui.btn_2.clicked.connect(self.num2)
        self.ui.btn_3.clicked.connect(self.num3)
        self.ui.btn_4.clicked.connect(self.num4)
        self.ui.btn_5.clicked.connect(self.num5)
        self.ui.btn_6.clicked.connect(self.num6)
        self.ui.btn_7.clicked.connect(self.num7)
        self.ui.btn_8.clicked.connect(self.num8)
        self.ui.btn_9.clicked.connect(self.num9)

    def num1(self):
        t = self.ui.tb1.text()
        t = t + '1'
        self.ui.tb1.setText(t)
    def num2(self):
        self.ui.tb1.setText(self.ui.tb1.text() + '2')
    def num3(self):
        self.ui.tb1.setText(self.ui.tb1.text() + '3')
    def num4(self):
        self.ui.tb1.setText(self.ui.tb1.text() + '4')
    def num5(self):
        self.ui.tb1.setText(self.ui.tb1.text() + '5')
    def num6(self):
        self.ui.tb1.setText(self.ui.tb1.text() + '6')
    def num7(self):
        self.ui.tb1.setText(self.ui.tb1.text() + '7')
    def num8(self):
        self.ui.tb1.setText(self.ui.tb1.text() + '8')
    def num9(self):
        self.ui.tb1.setText(self.ui.tb1.text() + '9')
    def num0(self):
        self.ui.tb1.setText(self.ui.tb1.text() + '0')

    def sum(self):
        self.op = '+'
        self.a = int(self.ui.tb1.text())

    def sub(self):
        self.op = '-'
        self.a = int(self.ui.tb1.text())

    def mul(self):
        self.op = '*'
        self.a = int(self.ui.tb1.text())
    def div(self):
        self.op = '/'
        self.a = int(self.ui.tb1.text())
    def per(self):
        self.a = int(self.ui.tb1.text())
        # result = self.a / 100
        self.ui.tb1.setText(str(self.a/100))
    def neg(self):
        # self.op =
        self.a = int(self.ui.tb1.text())
        self.ui.tb1.setText(str(self.a * -1))
    def clean(self):
        self.ui.tb1.setText('0')

    def equal(self):

        self.b = int(self.ui.tb1.text())

        if self.op == '+':
            result = self.a + self.b
        elif self.op == '-':
            result = self.a - self.b
        elif self.op == '/':
            result = self.a / self.b
        elif self.op == '*':
            result = self.a * self.b

        self.ui.tb1.setText(str(result))

if __name__ == "__main__":
    app = QApplication([])
    window = Mainwindow()
    # setting_window = mainwindow()
    sys.exit(app.exec_())
