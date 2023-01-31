import sys
from PyQt5.QtWidgets import *
"""
Constructor BoxLayout : boxlayout = QBoxLayout()
boxlayout.
    .addWidget()
    .insertWidget()
"""

# QWidget from PyQt5.QtWidgets


class Window(QWidget):   # QWindows from PyQt5.Qt.Gui
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Hôm nay học về Label")
        self.setMinimumWidth(300)
        self.setMinimumHeight(400)
        # constructor QBoxLayout
        layout = QBoxLayout(QBoxLayout.LeftToRight)  # xuất các label từ trái qua phải
        self.setLayout(layout)

        label1 = QLabel("Đây là Label 1")  # from PyQt5.QtWidgets
        layout.addWidget(label1, 0)
        label1 = QLabel("Đây là Label 2")  # from PyQt5.QtWidgets
        layout.addWidget(label1, 0)
        label1 = QLabel("Đây là Label 3")  # from PyQt5.QtWidgets
        layout.addWidget(label1, 0)
        label1 = QLabel("Đây là Label 4")  # from PyQt5.QtWidgets
        layout.addWidget(label1, 0)


def main():

    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()