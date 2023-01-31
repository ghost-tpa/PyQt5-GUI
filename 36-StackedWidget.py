import sys
from PyQt5.QtWidgets import *

"""
    The stackedwidget is a container which displays a single page at a time. A left-hand panel provides 
access to the pages which are then displayed to the right

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
        self.stackedwidgetcreate()

    def initUI(self):
        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(QApplication.instance().quit)  # self.button_exit
        self.layout.addWidget(exitButton, 3, 0)

    def stackedwidgetcreate(self):
        self.stackedwidget = QStackedWidget()
        self.layout.addWidget(self.stackedwidget, 0, 0)

        for x in range(1, 4):
            label = QLabel("Stack child %i" % x)
            self.stackedwidget.addWidget(label)

            button = QPushButton("Stack %i" % x)
            button.page = x
            button.clicked.connect(self.on_button_clicked)
            self.layout.addWidget(button, x, 0)
    
    def on_button_clicked(self):
        button = self.sender()
        self.stackedwidget.setCurrentIndex(button.page - 1)
        




def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()