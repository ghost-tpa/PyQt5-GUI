import sys
from PyQt5.QtWidgets import *

"""
The SizeGrip widget provides a way to resize a parent Window.
It commonly appears as a triangle in the bottom right corner of the window and allows the user
to increase or decreate the window width and height
"""


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("SizeGrip")

        layout = QGridLayout()
        self.setLayout(layout)

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