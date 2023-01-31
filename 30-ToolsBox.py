import sys
from PyQt5.QtWidgets import *

"""
    The ToolBox widget is a container which displays groups of items separated by tabs, with the items
consisting of the text identifying the item, and an optional icon. The ToolBox is commonly used in applications
where there are too many items to place in a ToolBar
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

        toolbox = QToolBox()
        self.layout.addWidget(toolbox, 0, 0)

        label = QPushButton()
        toolbox.addItem(label, "Honda")
        label = QPushButton()
        toolbox.addItem(label, "Honda")
        label = QPushButton()
        toolbox.addItem(label, "Honda")

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