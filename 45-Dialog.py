import sys
from PyQt5.QtWidgets import *

"""

"""


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QGridLayout()
        self.setWindowTitle("")
        self.setMinimumWidth(900)
        self.setMinimumHeight(700)
        self.setLayout(self.layout)
        self.initUI()
        self.dialogcreater()

    def initUI(self):
        button = QPushButton("Touch me")
        button.clicked.connect(self.dialogcreater)
        self.layout.addWidget(button, 0, 0)
        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(QApplication.instance().quit)  # self.button_exit
        self.layout.addWidget(exitButton, 1, 0)

    def dialogcreater(self):
        dialog = QDialog()
        layout_dialog = QVBoxLayout()
        dialog.setLayout(layout_dialog)
        label = QLabel("This is a dialog.")
        layout_dialog.addWidget(label)
        dialog1 = QInputDialog()
        dialog2 = QInputDialog()
        layout_dialog.addWidget(dialog1)
        layout_dialog.addWidget(dialog2)
        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout_dialog.addWidget(buttonbox)

        retval = dialog.exec_()
        # self.layout.addWidget(label, 0, 0)
        # self.layout.addWidget(dialog1, 3, 0)
        #self.layout.addWidget(dialog2, 4, 0)
        #self.layout.addWidget(buttonbox, 2, 0)



def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()