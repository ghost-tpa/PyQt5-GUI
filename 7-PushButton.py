import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

"""
Pushbutton:  pbutton = QPushButton(Label)
method 
    .
    

"""

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Bây giờ chúng ta làm việc với Button")
        self.setMinimumHeight(400)
        self.setMinimumHeight(500)


        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel("Đây là label ở dòng 1")
        layout.addWidget(label, 0, 0)

        pbutton = QPushButton("Nút này để bấm cho vui")
        pbutton.clicked.connect(self.on_button_clicked)
        layout.addWidget(pbutton, 1, 0)
        pbuttontop = QPushButton("Nút này ở trên")
        layout.addWidget(pbuttontop, 2, 0)
        exitbutton = QPushButton("Exit")
        exitbutton.clicked.connect(self.exit_button)
        layout.addWidget(exitbutton, 3, 1)

    def exit_button(self):
        exit("Exiting program...")

    def on_button_clicked(self):
        box = QMessageBox()
        box.setText("Bạn đã bấm")
        print("The button was pressed! ")


def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
