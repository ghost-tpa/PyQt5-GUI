import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

"""
RadioButton - nút có hình tròn dạng checkbox
"""


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Bây giờ chúng ta làm việc với RadioButton")
        self.setMinimumHeight(400)
        self.setMinimumHeight(500)

        layout = QGridLayout()
        self.setLayout(layout)

        radioButton = QRadioButton("Brazil")
        # radioButton.setChecked(True)
        radioButton.country = "Brazil"
        radioButton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radioButton, 0, 0)

        radioButton = QRadioButton("VietNam")
        # radioButton.setChecked(True)
        radioButton.country = "VietNam"
        radioButton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radioButton, 1, 0)

        radioButton = QRadioButton("Russia")
        # radioButton.setChecked(True)
        radioButton.country = "Russia"
        radioButton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radioButton, 2, 0)

    def on_radio_button_toggled(self):
        radiobutton = self.sender()
        if radiobutton.isChecked():
            print("Selected country is %s " % radiobutton.country)

def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
