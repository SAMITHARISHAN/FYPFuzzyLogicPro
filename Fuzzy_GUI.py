import csv
import pandas as pd

from fuzzy_decision.Decision import init_fuzzy_system, get_decision
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QWidget, QTableView, QPushButton, QLineEdit,
                             QInputDialog, QApplication, QFileDialog, QCheckBox, QLabel, QVBoxLayout)
import sys
import os

class Example(QWidget):

    # def __init__(self):
    #     super().__init__()
    #
    #     self.initUI()

    def __init__(self, fileName, parent=None):
        super(Example, self).__init__(parent)
        self.fileName = fileName

        self.model = QtGui.QStandardItemModel(self)

        self.tableView = QTableView(self)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.pushButtonLoad = QPushButton(self)
        self.pushButtonLoad.setText("Load Csv File!")
        self.pushButtonLoad.clicked.connect(self.on_pushButtonLoad_clicked)

        self.layoutVertical = QVBoxLayout(self)
        self.layoutVertical.addWidget(self.tableView)
        self.layoutVertical.addWidget(self.pushButtonLoad)

    sim = init_fuzzy_system()
    requirement_threshold = 4
    vCount = []
    pCount = []
    vSpeed = []
    wTime = []
    trafficdata = []
    arr = []
    @QtCore.pyqtSlot()
    def on_pushButtonLoad_clicked(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                          "All Files (*);;Python Files (*.py)", options=options)
        if fileName:

            print(fileName)

            # self.le.setText(str(fileName))
        # df = pd.read_csv("Dataset1.csv")
        with open('Dataset1.csv', 'r') as fileInput:
            csv_reader = csv.reader(fileInput)

            next(csv_reader)

            for row in csv_reader:
                self.vCount.append(row[0])
                self.pCount.append(row[1])
                self.vSpeed.append(row[2])
                self.wTime.append(row[3])
                # print(self.vCount)
                self.trafficdata = [(row[0], row[1], row[2], row[3])]
                # print(self.trafficdata)
                self.arr.append(self.trafficdata)
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)

                # get_decision(self.sim, row[0], row[1], row[2], row[3], self.requirement_threshold)

    # get_decision(self.sim, row[0], row[1], row[2], row[3], self.requirement_threshold)
        for i in self.arr:
            print(i)
if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example("Dataset1.csv")
    ex.show()
    sys.exit(app.exec_())
