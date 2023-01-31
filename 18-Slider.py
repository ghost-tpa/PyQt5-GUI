import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

"""
Slider là thanh trượt có thể set được giá trị
Constructor  - slider = QSlider()
Methods
    .setMinimum()
"""


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Slider")

        layout = QGridLayout()
        self.setLayout(layout)

        grBox1 = QGroupBox()
        grBox2 = QGroupBox()
        layout.addWidget(grBox1)
        layout.addWidget(grBox2)
        vBox1 = QVBoxLayout()
        vBox2 = QVBoxLayout()
        grBox1.setLayout(vBox1)
        grBox2.setLayout(vBox2)

        slider = QSlider(Qt.Horizontal)
        slider.setValue(50)
        value = slider.value()
        slider.setTracking(True)
        label = QLabel(str(value))
        vBox1.addWidget(slider)
        vBox1.addWidget(label)

        slider = QSlider(Qt.Horizontal)
        slider.setValue(50)
        vBox2.addWidget(slider)
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