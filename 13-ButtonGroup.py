import sys
from PyQt5.QtWidgets import *

"""
self.buttonGroup: 
Constructor = self.buttonGroup = QButtonHG
Metods:
    .setExclusive(boolvar) 
"""


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Học lineedit")
        self.setMinimumHeight(700)
        self.setMinimumHeight(900)
        self.showMinimized()

        layout = QGridLayout()
        self.setLayout(layout)

        self.buttongroup = QButtonGroup()
        self.lineedit = QLineEdit()
        self.lineedit.setPlaceholderText("Nhập số lượng ở đây")
        self.buttongroup.setExclusive(False)
        self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)

        button = QPushButton("Button 1")
        self.buttongroup.addButton(button, 1)
        layout.addWidget(button, 0, 0)
        layout.addWidget(self.lineedit, 0, 1)
        button = QPushButton("Button 2")
        self.buttongroup.addButton(button, 2)
        layout.addWidget(button, 1, 0)
        self.lineedit = QLineEdit()
        self.lineedit.setPlaceholderText("Nhập số lượng ở đây")
        layout.addWidget(self.lineedit, 1, 1)
        button = QPushButton("Button 3")
        self.buttongroup.addButton(button, 3)
        layout.addWidget(button, 2, 0)
        self.lineedit = QLineEdit()
        self.lineedit.setPlaceholderText("Nhập số lượng ở đây")
        layout.addWidget(self.lineedit, 2, 1)

        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(QApplication.instance().quit)  # self.button_exit
        layout.addWidget(exitButton, 3, 1)

    def on_button_clicked(self, id):
        for button in self.buttongroup.buttons():  # list các button ở group
            if button is self.buttongroup.button(id):  # lấy id của button
                print("%s was clicked! " % button.text())

    def button_exit(self):
        exit(0)


def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
