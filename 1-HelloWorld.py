#! python 3.9
import sys
# from PyQt5 import QtCore
from PyQt5.QtWidgets import *
# from PyQt5 import QtGui
import PyQt5


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Hello")

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel("Hello World")
        label2 = QLabel("Hello World 2")
        label3 = QLabel("Hello World 3")
        layout.addWidget(label, 0, 0)  # tọa độ của lưới  (cột, hàng)
        layout.addWidget(label2, 0, 1)
        layout.addWidget(label3, 0, 2)


def main():
    app = QApplication(sys.argv)
    screen = Window()
    screen.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



