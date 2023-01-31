import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

"""

"""


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.initUI()
        self.inputProduct()
        self.dataafterchoose()


    def initUI(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.setWindowTitle("Test chơi")
        self.setMinimumWidth(900)
        self.setMinimumHeight(700)
        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(QApplication.instance().quit)  # self.button_exit
        self.layout.addWidget(exitButton, 5, 0)

    def inputProduct(self):
        self.dataproduct = QComboBox()
        self.dataproduct.setDuplicatesEnabled(True)
        self.dataproduct.activated[int].connect(self.import_data_to_FormLayout())
        self.layout.addWidget(self.dataproduct, 0, 0)
        fopen = open("ChoViet/spkhonggia.txt", "r")
        while fopen.tell() != os.fstat(fopen.fileno()).st_size:
            self.dataproduct.insertItem(2, fopen.readline())
        fopen.close()

    def dataafterchoose(self):
        self.groupBoxData = QGroupBox()
        self.layout.addWidget(self.groupBoxData, 1, 0)
        self.dataproductafterchoose = QFormLayout()
        self.groupBoxData.setLayout(self.dataproductafterchoose)

    def import_data_to_FormLayout(self):
        self.dataproductafterchoose.addRow(self.dataproduct.currentText(), QLabel())


def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()