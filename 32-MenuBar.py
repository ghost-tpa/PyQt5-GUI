import sys
from PyQt5.QtWidgets import *

"""
Menubar
Constructor:  menubar = QMenuBar()
Methods 
    .addAction(label) - Actions, which perfrom an associated function when clicked can be added to the MenuBar with a simple text label
    .addMenu(label)
    .removeAction(action)
    .addSeparator() - Thêm dấu cách
"""


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QGridLayout()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MenuBar")
        self.setMinimumWidth(900)
        self.setMinimumHeight(700)
        self.setLayout(self.layout)

        menubar = QMenuBar()
        menubar.setNativeMenuBar(False)
        self.layout.addWidget(menubar, 0, 0)
        self.actionFile = menubar.addMenu("File")
        self.actionFile.addAction("New")
        self.actionFile.addSeparator()
        self.actionFile.addAction("Quit")
        menubar.addMenu("Edit")
        menubar.addMenu("View")
        menubar.addMenu("Help")


        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(QApplication.instance().quit)  # self.button_exit
        self.layout.addWidget(exitButton, 0, 9)


def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()