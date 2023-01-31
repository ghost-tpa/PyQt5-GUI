import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
"""
Constructor windows : window = QWindow()
window.
    .showMinimized()  # auto bé nhất khi mở
    .showMaximized()  # tương tự
    .showFullScreen()  # auto toàn màn hình khi mở
    .showNormal()
    .screen.setMinimumWidth()   # mini dài
    .screen.setMinimumHeight()  # mini rộng
    .setWidth()
    .setHeight()
"""


class Window(QWindow):
    def __init__(self):
        QWindow.__init__(self)
        self.setTitle("We learn about method")
        self.resize(400, 300)   # (rộng,dài)


def main():
    app = QApplication(sys.argv)

    screen = Window()
    screen.setMinimumWidth(400)
    screen.setMinimumHeight(300)
    screen.setWidth(600)
    screen.setHeight(600)
    screen.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()