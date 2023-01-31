import sys
from PyQt5.QtWidgets import *

"""
The ProgressDialog is similar to the ProgressBar, with the ProgressBar portion of the widget placed in 
the dialog window. It's often used when the running process will require the user to wait, with the rest 
of application being unavailable to use
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

        progressDialog = QProgressDialog()
        progressDialog.setValue(5)
        self.layout.addWidget(progressDialog, 0, 0)
        label = QLabel()
        label.setText(str(progressDialog.value()))
        self.layout.addWidget(label, 1, 0)




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