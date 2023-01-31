import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

"""
    The Splitter is an organiser class widget, which provides a way to insert child itmes which can then
be given varying amounts of space. The amount of space allowed is adjusted by the user using a handle
on the Splitter. 
    The widget is commonly seen in File Managers and Web Browser where the main content may also need 
to share space with a side panel such as tree view of bookmark list.

    Có thể điểu chỉnh vị trí các widgets con trong Spltter bằng tay

"""


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Splitter")

        layout = QGridLayout()
        self.setLayout(layout)

        splitter = QSplitter()
        splitter.setOrientation(Qt.Horizontal)
        layout.addWidget(splitter)

        label = QLabel(str(splitter.count))
        splitter.addWidget(label)
        checkbox = QCheckBox()
        splitter.addWidget(checkbox)
        lineedit = QLineEdit()
        lineedit.setPlaceholderText("Nhập ở đây")
        splitter.insertWidget(3, lineedit)


        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(QApplication.instance().quit)  # self.button_exit
        layout.addWidget(exitButton)

    def button_exit(self):
        exit(0)


def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()