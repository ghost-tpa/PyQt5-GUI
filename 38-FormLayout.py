import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

"""
    The FormLayout provides a class layout to handle input widgets and their associated labels. The
children are laid out in two columns, with the label column handling the label and the right column providing
space for the input widgets such as text entries or spin boxes
Constructor: formlayout = QFromLayout()
Methods
    -
"""


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QGridLayout()
        self.setWindowTitle("")
        self.setMinimumWidth(900)
        self.setMinimumHeight(700)
        self.setLayout(self.layout)
        self.initUI()
        self.formlayoutcreater()
        self.groupboxcreater()
        self.scrollareacreater()

    def initUI(self):
        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(QApplication.instance().quit)  # self.button_exit
        self.layout.addWidget(exitButton)

    def formlayoutcreater(self):

        self.formlayout = QFormLayout()
        self.formlayout.addRow("Name :", QLineEdit())

    def groupboxcreater(self):
        self.groupbox = QGroupBox()
        self.groupbox.setLayout(self.formlayout)
        self.layout.addWidget(self.groupbox)


    def scrollareacreater(self):
        self.scrollarea = QScrollArea()
        self.scrollarea.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.scrollarea)
        self.scrollarea.setWidgetResizable(True)
        self.formlayout1 = QFormLayout()
        self.scrollarea.setLayout(self.formlayout1)
        self.scrollarea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        fopen = open("ChoViet/sanpham.txt", "r")
        while fopen.tell() != os.fstat(fopen.fileno()).st_size:
            self.labelNameProduct = QLabel(fopen.readline())
            self.lineeditPriceofProduct = QLineEdit()
            self.lineeditPriceofProduct.setPlaceholderText(str(fopen.readline()))
            self.formlayout1.addRow(self.labelNameProduct, self.lineeditPriceofProduct)
        fopen.close()


def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()