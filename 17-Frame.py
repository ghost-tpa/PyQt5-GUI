import sys

import PyQt5.QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

"""
docutmentation: https://doc.qt.io/qt-5/qframe.html#details
http://qtdocs.narod.ru/4.1.0/doc/html/qframe.html#Shape-enum
http://qtdocs.narod.ru/4.1.0/doc/html/qframe.html
"""


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("WhatsThis")

        layout = QGridLayout()
        self.setLayout(layout)

        frame = QFrame()
        frame1 = QFrame()
        frame.setFrameShadow(QFrame.Raised)
        frame.setFrameShape(QFrame.Box)
        layout.addWidget(frame, 0, 0)
        layout.addWidget(frame1, 1, 0)

        frame.showNormal()
        vbox = QVBoxLayout()
        label = QLabel("Dòng 1")
        vbox.addWidget(label)
        label = QLabel("Dòng 2")
        vbox.addWidget(label)
        label = QLabel("Dòng 3")
        vbox.addWidget(label)
        label = QLabel("Dòng 4")
        vbox.addWidget(label)

        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(QApplication.instance().quit)  # self.button_exit
        layout.addWidget(exitButton)

    def button_exit(self):
        exit(0)


def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()