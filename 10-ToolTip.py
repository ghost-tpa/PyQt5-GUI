import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

"""
ToolTip widgets are attached to other widgets and appear when the users hovers over the widget, 
displaying hints about the purpose of the widget
ToolTip đưa ra hướng dẫn khi bạn di chuột tới button
"""


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Học Checkbook")
        self.setMinimumHeight(400)
        self.setMinimumHeight(500)

        layout = QGridLayout()
        self.setLayout(layout)

        button = QPushButton("Simple ToolTip")
        button.setToolTip("This toolTip simply displays text. ")
        button.setMaximumWidth(200)
        button.setMinimumHeight(50)
        layout.addWidget(button, 0, 0)

        button1 = QPushButton("Formatted ToolTip")
        button1.setToolTip("<b> Formated text </b> can also be displayed. ")
        layout.addWidget(button1, 1, 0)

        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(QApplication.instance().quit)  # self.button_exit
        layout.addWidget(exitButton, 3, 1)

    def button_exit(self):
        exit(0)

def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
