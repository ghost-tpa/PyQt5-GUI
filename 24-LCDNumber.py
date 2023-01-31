import sys
from PyQt5.QtWidgets import *

"""

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

        lcdnumber = QLCDNumber()

        self.layout.addWidget(lcdnumber)
        lcdnumber.display(20)

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