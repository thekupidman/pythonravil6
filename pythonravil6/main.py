#!/usr/bin/env python3
# coding=utf-8

import sys
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic,QtGui
import random
import math
from array import *

class Example(QWidget):

    def __init__(self):
        super().__init__()
        QWidget.__init__(self)
        self.initUI()

    def initUI(self):
        self.text = QTextEdit(self)
        self.btn1 = QPushButton("Загрузить исходные данные из файла", self)
        self.btn2 = QPushButton("Обработать данные", self)
        self.btn3 = QPushButton("Очистить", self)
        self.btn4 = QPushButton("Сохранить обработанные данные в файл", self)
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.label = QLabel(self)

        self.text.setGeometry(8, 8, 369, 329)
        self.btn1.setGeometry(8, 343, 369, 42)
        self.btn2.setGeometry(8, 391, 177, 42)
        self.btn3.setGeometry(200, 391, 177, 42)
        self.btn4.setGeometry(8, 439, 369, 42)
        self.label.setGeometry(8, 487, 369, 40)

        self.btn1.clicked.connect(self.btn1Click)
        self.btn2.clicked.connect(self.btn2Click)
        self.btn3.clicked.connect(self.btn3Click)
        self.btn4.clicked.connect(self.btn4Click)

        self.setGeometry(300, 300, 400, 576)
        self.setWindowTitle('Задание 6')
        self.show()

    def btn1Click(self):
        f = open('file_6.txt')
        data = f.read()
        self.aData = []
        for line in data.split("\n"):
            aLine = []
            for cell in line.split("\t"):
                aLine.append(int(cell))
            self.aData.append(aLine)

        self.text_data1 = "Полученные данные:\n" + data
        self.text.setText(self.text_data1)

    def btn2Click(self):
        is1 = True
        for c in self.aData[2]:
            if is1:
                max1_i = -1
                max1_v = -1000000000
                max2_i = -1
                max2_v = -1000000000
                i = 0
                for c in self.aData:
                    if c[0] > max1_v:
                        max1_v = c[0]
                        max1_i = i
                    if c[1] > max2_v:
                        max2_v = c[1]
                        max2_i = i
                        self.aData[0][0] = self.aData[0][0] * 2
                        self.aData[1][0] = self.aData[1][0] * 2
                        self.aData[2][0] = self.aData[2][0] * 2
                        self.aData[3][0] = self.aData[3][0] * 2
                        self.aData[4][0] = self.aData[4][0] * 2
                    i = i + 1
            textLines = []
            for aLines in self.aData:
                textLines.append("\t".join([str(c1) for c1 in aLines]))
            data = "\n".join([str(c2) for c2 in textLines])

            self.text.setText(self.text_data1 + data)

    def btn3Click(self):
        self.text.setText("")
        self.text_data1 = ""
        self.aData = []

    def btn4Click(self):
        f = open('file_6.txt', 'w')

        textLines = []
        for aLines in self.aData:
            textLines.append("\t".join([str(c1) for c1 in aLines]))
        data = "\n".join([str(c2) for c2 in textLines])

        f.write(data)
        f.close()

if __name__=='__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
