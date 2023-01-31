import sys
from PyQt5.QtWidgets import *

"""
gridlayout là layout dạng lưới
layout = QGridLayout()
Methods 
    .

"""

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Bây giờ chúng ta học Grid layout")

        layout = QGridLayout()
        self.setLayout(layout)
        label = QLabel("Đây là 1 label 1")
        layout.addWidget(label, 0, 0)
        label = QLabel("Đây là 1 label 2")
        layout.addWidget(label, 0, 1)
        label = QLabel("Đây là 1 label 3")
        layout.addWidget(label, 0, 2)
        label = QLabel("Đây là 1 label 4")
        layout.addWidget(label, 0, 3)
        checkbook = QCheckBox("Check cho vui")
        layout.addWidget(checkbook, 1, 0)
        pushbutton = QPushButton("Bấm thử chơi")
        layout.addWidget(pushbutton, 2, 1)


def main():
    app = QApplication(sys.argv)
    window1 = Window()
    window1.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()