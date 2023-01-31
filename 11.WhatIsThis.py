import sys
from PyQt5.QtWidgets import *

"""
Constructor: widget.setWhatsThis(text)
The text string should be defined to explain the purpose the widget.

Kiểu hiện bảng trợ giúp .
"""


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("WhatsThis")

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel("Focus ComboBox and press SHIFT+F1")
        layout.addWidget(label, 0, 0)

        self.combobox = QComboBox()
        self.combobox.setWhatsThis("This is a 'WhatsThis' object description. ")
        layout.addWidget(self.combobox, 1, 0)

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