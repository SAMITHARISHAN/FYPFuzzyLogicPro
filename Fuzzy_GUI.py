#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we receive data from
a QInputDialog dialog.

Aauthor: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication, QFileDialog, QLabel)
import sys
import os
import csv

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Vehicle Count', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.openFileNameDialog)


        self.btn5 = QPushButton('Start', self)
        self.btn5.move(20, 160)
        self.btn5.clicked.connect(self.exe_another)



        # self.lbl1 = QLabel('Vehicle', self)
        # self.lbl1.move(80, 80)
        #
        # self.lbl2 = QLabel('Pedestrians', self)
        # self.lbl2.move(80, 100)
        #
        # self.lbl3 = QLabel('Pedestrians', self)
        # self.lbl3.move(80, 100)
        #
        # self.lbl4 = QLabel('Pedestrians', self)
        # self.lbl4.move(80, 100)

        self.setGeometry(400, 400, 300, 200)
        self.setWindowTitle('Control Center')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')

        if ok:
            self.le.setText(str(text))

    def exe_another(self):

        comnd = "python Real-time.py " + "-i1 " + self.le.text() + " -i2 " + self.le2.text() + " -i3 " + self.le3.text() + " -i4 " + self.le4.text() + " -i5 "
        print(comnd)
        os.system(comnd)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            self.le.setText(str(fileName))
            

    def test(self):
        print("")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())