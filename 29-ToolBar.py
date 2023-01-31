import sys
from PyQt5.QtWidgets import *

"""
A Toolbar tipically provides common shortcuts to features of an application (e.g open file, find, zoom) 
and is usually displayed the main content of application  
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

        toolbar = QToolBar()
        self.layout.addWidget(toolbar)
        addprdbutton = QPushButton("Thêm sản phẩm")
        toolbar.addWidget(addprdbutton)
        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(QApplication.instance().quit)  # self.button_exit
        toolbar.addWidget(exitButton)


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