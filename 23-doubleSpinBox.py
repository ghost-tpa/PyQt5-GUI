import sys
from PyQt5.QtWidgets import *

"""
DoubleSpinBox giống spinbox nhưng điều chỉnh đc tới số thập phân luôn 
Methods
    .setSingleStep() - nhận giá trị float
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

        dbspinBox = QDoubleSpinBox()
        dbspinBox.setSingleStep(0.1)

        self.layout.addWidget(dbspinBox)


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