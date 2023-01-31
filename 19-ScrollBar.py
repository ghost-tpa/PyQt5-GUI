import sys
from PyQt5.QtWidgets import *

"""
A ScrollBar provides a way to move horizontally or vertically within a frame where the content is too larger
to fit. The ScrollBar typically includes a bar with arrows buttons to move the view. A bar is also provided 
within to drag-and-drop into a new position
"""


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("ScrollBar")

        layout = QGridLayout()
        self.setLayout(layout)

        scrollbar = QScrollBar()
        layout_scrollBar = QVBoxLayout()
        scrollbar.setLayout(layout_scrollBar)
        layout_scrollBar.addWidget(QLabel("1"))
        layout_scrollBar.addWidget(QLabel("2"))
        layout_scrollBar.addWidget(QLabel("3"))
        scrollbar.setWindowTitle("Cuộn cho vui")
        scrollbar.setValue(50
                           )

        layout.addWidget(scrollbar)


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