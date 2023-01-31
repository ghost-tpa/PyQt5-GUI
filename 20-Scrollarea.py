import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

"""

"""


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.groupBox = QGroupBox("")
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.widget.setMinimumWidth(900)
        self.widget.setMinimumHeight(700)
        # self.widget.resize(900, 700)
        self.vBox = QVBoxLayout()
        
        fopen = open("ChoViet/spkhonggia.txt", "r")
        while fopen.tell() != os.fstat(fopen.fileno()).st_size:  # khi chạy tới cuối file
            object = QLabel(fopen.readline())
            object.setMaximumWidth(200)
            object.setMinimumHeight(30)
            lineedit = QLineEdit()
            lineedit.setPlaceholderText("Nhập số lượng ở đây: ")
            lineedit.setMaximumWidth(200)
            self.vBox.addWidget(object)
            self.vBox.addWidget(lineedit)

        self.widget.setLayout(self.vBox)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(QApplication.instance().quit)  # self.button_exit
        self.vBox.addWidget(exitButton)

        self.setCentralWidget(self.scroll)
        self.setWindowTitle("Chương trình tính tiền chợ việt")
        self.show()




    def button_exit(self):
        exit(0)


def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()