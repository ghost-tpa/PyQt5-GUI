import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
"""
là 1 cái nút có thể thêm được vào ToolBar hoặc ToolBox
    The ToolButton widget provides a button which can be added to a Toolbar or ToolBox container. They are
used commonly for quick access to common functions such ass saving a document, or finding a string of text
Constructor: toolbutton = QToolButton()
Methods
    .setText(sometext)
    .setIcon(icon) - icon from QIcon <- QtGui
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
        toolbutton = QToolButton()
        toolbutton.setText("Save")
        icon = QIcon("data/saveicon.png")
        toolbutton.setIcon(icon)
        toolbutton.setMinimumHeight(50)
        toolbutton.setMinimumWidth(50)
        toolbutton.setCheckable(False)  # nút sẽ hiển thị đã chọn nếu đặt về True

        self.layout.addWidget(toolbutton)


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