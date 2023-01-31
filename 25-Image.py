import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

"""
Image widget provides a way to displays images within a Qt application

QImage - optimised for input/output
QPixmap - designed for showing images on screen
QBitmap - inherits from QPixmap with a depth of 1
QPicture - paint device to record and replay QPainter commands
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("")
        self.setMinimumWidth(900)
        self.setMinimumHeight(700)
        self.setLayout(self.layout)

        imgObject = QPixmap("bg.jpeg")
        label = QLabel()
        label.setPixmap(imgObject)
        self.layout.addWidget(label)


        srcollarea = QScrollArea()
        self.layout.addWidget(srcollarea, 1, 1)


        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(QApplication.instance().quit)  # self.button_exit
        self.layout.addWidget(exitButton)

    def button_exit(self):
        exit(0)


def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()