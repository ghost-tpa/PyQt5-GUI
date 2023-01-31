import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

"""
The GroupBox provides a tidy way to group items, 
with the container featuring a tide label and bordering frame.
It should be noted that the GroupBox can only contain one widget itself,
with the intention of the other container such as a BoxLayout
.
Constructor groupbox = QGroupBox(title)
Methods 
    .setTitle
    .setLayout(child)
    .setAlignment(alignment)
        .Qt.AlignLeft
        .Qt.AlignCenter
        .Qt.AlignRight
    .setCheckable(checkable)
    .isChecked()
    .setChecked(boolvar)
"""


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Học GroupBox")

        layout = QGridLayout()
        self.setLayout(layout)

        grBox = QGroupBox("Ví dụ GroupBox")
        grBox.setMaximumWidth(400)
        grBox.setMinimumHeight(500)
        grBox.setToolTip("Chỗ này là GroupBox")
        grBox.setAlignment(Qt.AlignCenter)
        layout.addWidget(grBox)
        vbox = QVBoxLayout()
        grBox.setLayout(vbox)
        sizeGrip = QSizeGrip(grBox)
        layout.addWidget(sizeGrip)

        checkBox = QCheckBox("Nhấn ở đây")
        lineedit = QLineEdit()
        lineedit.setPlaceholderText("Nhập ở đây")
        vbox.addWidget(checkBox)
        vbox.addWidget(lineedit)

        checkBox = QCheckBox("Nhấn ở đây")
        lineedit = QLineEdit()
        lineedit.setPlaceholderText("Nhập ở đây")
        vbox.addWidget(checkBox)
        vbox.addWidget(lineedit)

        checkBox = QCheckBox("Nhấn ở đây")
        lineedit = QLineEdit()
        lineedit.setPlaceholderText("Nhập ở đây")
        vbox.addWidget(checkBox)
        vbox.addWidget(lineedit)

        checkBox = QCheckBox("Nhấn ở đây")
        lineedit = QLineEdit()
        lineedit.setPlaceholderText("Nhập ở đây")
        vbox.addWidget(checkBox)
        vbox.addWidget(lineedit)

        checkBox = QCheckBox("Nhấn ở đây")
        lineedit = QLineEdit()
        lineedit.setPlaceholderText("Nhập ở đây")
        vbox.addWidget(checkBox)
        vbox.addWidget(lineedit)

        checkBox = QCheckBox("Nhấn ở đây")
        lineedit = QLineEdit()
        lineedit.setPlaceholderText("Nhập ở đây")
        vbox.addWidget(checkBox)
        vbox.addWidget(lineedit)





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