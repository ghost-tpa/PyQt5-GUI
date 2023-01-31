import sys
from PyQt5.QtWidgets import *

"""
Dial là con quay có thể thay đổi giá trị
Methods
    .setMinnimum()
    .setMaximum()
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

        dial = QDial()
        dial.setMinimum(1)
        dial.setMaximum(10)
        dial.setValue(5)
        dial.setMaximumWidth(200)
        dial.setMaximumHeight(200)
        dial.setWrapping(False)  # từ thấp tới cao ? ? ? ?

        self.layout.addWidget(dial)


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