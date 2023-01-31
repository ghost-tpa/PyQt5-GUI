import sys
from PyQt5.QtWidgets import *

"""
    The Menu item provides the base layer for the menu items which are displayed on it. 
This can include single-click items, check and radio items or additional menus. 
Constructor  - menu = QMenu()
Methods 
    .
"""


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QGridLayout()
        self.setWindowTitle("Menu")
        self.setMinimumWidth(900)
        self.setMinimumHeight(700)
        self.setLayout(self.layout)
        self.initUI()
        self.Menu()

    def initUI(self):
        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(QApplication.instance().quit)  # self.button_exit
        self.layout.addWidget(exitButton)

    def Menu(self):
        self.menu = QMenu()
        self.action = self.menu.addMenu(" &File")
        self.action .addAction(" &Open")

def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()