import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

"""
    The Tabwidget provides a container with multiple pages which are switchable via tabs. Each page can contain
a single widget or other containers. The TabWidget is commonly found in multi-document applications such as
web browsers or word processors
"""


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QGridLayout()
        self.setWindowTitle("")
        self.setMinimumWidth(900)
        self.setMinimumHeight(700)
        self.setLayout(self.layout)
        self.initUI()
        self.tabWidget()

    def initUI(self):


        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(QApplication.instance().quit)  # self.button_exit
        self.layout.addWidget(exitButton)

    def tabWidget(self):
        self.tabwidget = QTabWidget()
        self.layout.addWidget(self.tabwidget)
        label1 = QLabel("Example")
        label2 = QLabel("More example")
        self.tabwidget.addTab(label1, " Tab 1")
        self.tabwidget.addTab(label2, " Tab 2")

def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()