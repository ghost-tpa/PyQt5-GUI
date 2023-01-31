import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

"""

"""


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Học Checkbook")
        self.setMinimumHeight(400)
        self.setMinimumHeight(500)

        layout = QGridLayout()
        self.setLayout(layout)

        self.checkbox = QCheckBox("Box 1")
        # self.checkbox.setChecked(True)
        self.checkbox.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox, 0, 0)

        self.checkbox = QCheckBox("Box 2")
        # self.checkbox.setChecked(True)
        self.checkbox.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox, 1, 0)

        self.checkbox = QCheckBox("Box 3")
        # self.checkbox.setChecked(True)
        self.checkbox.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox, 2, 0)

        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(QApplication.instance().quit)  # self.button_exit
        layout.addWidget(exitButton, 3, 1)

    def checkbox_toggled(self):
        selected = []
        if self.checkbox.isChecked():
            selected.append("Box 1")
        if self.checkbox.isChecked():
            selected.append("Box 2")
        if self.checkbox.isChecked():
            selected.append("Box 3")

        print("Selected: %s " % "".join(selected))

    def button_exit(self):
        exit(0)

def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
