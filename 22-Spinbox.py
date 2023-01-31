import sys
from PyQt5.QtWidgets import *

"""
The SpinBox widget proviides a way to enter numerical data. The widget provides integrated adjustment 
button which allow the user to adjust the number by clicking the arrows, while also allowing adjustment
by typing into a text entry.  
spinbox 
Constructor spbox = QSpinBox() 
Methods
    .setMinimumSize()
    .setValue()
    .setMinimum()
    .setMaximum()
    .setRange(min, max)  -  set min max cho spinbox  
    .setSuffix()
    .setPrefix()
    .setSingleStep()
    
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

        spinBox = QSpinBox()
        spinBox.setMinimumSize(10, 30)
        spinBox.setRange(5, 10)
        spinBox.setSuffix(" .cm")
        spinBox.setPrefix("Loài ")
        spinBox.setSingleStep(2)  # bước nhảy

        self.layout.addWidget(spinBox)



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