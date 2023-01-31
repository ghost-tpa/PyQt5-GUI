import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QMainWindow):  # from QtWidgets
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Windows nè")
        label = QLabel("Dòng này hình như ở chính giữa")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
        buttonAction = QAction("Button Action", self)
        buttonAction.setStatusTip("This is my button")
        toolBar = QToolBar("ToolBar")
        toolBar.addAction(buttonAction)
        self.menubar = QMenuBar()
        self.action = self.menubar.addMenu("File")
        self.action.addAction("Open")
def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()