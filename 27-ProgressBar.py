import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

"""
ProgressBar giống thanh trạng thái có thể hiển thị quá trình hd của process.
ProgressBar 
A ProgressBar is used to show the completion state of a process. 

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

        progressbar = QProgressBar()
        progressbar.setMinimumWidth(300)
        progressbar.setMinimumHeight(400)
        progressbar.setOrientation(Qt.Horizontal)

        self.layout.addWidget(progressbar)


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