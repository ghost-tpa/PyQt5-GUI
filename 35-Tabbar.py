import sys
from PyQt5.QtWidgets import *

"""
    A TabBar provides the drawing of tabs, with common usage in tabbed dialogs. It is similar to the 
TabWidget which is a ready made solution, whereas provides more configuration for layout and style
Constructor : tabbar =  QTabBar()
Methods
    .addTab(text)
    .addTab(icon, text)
    .insertTab(index, text)
    .insertTab(index, icon, text)
    .removeTab(index)
    .setMovable()  # True, False - Tab có thể di chuyển và tự đổi chỗ cho nhau
    .moveTab(from, to)  # index 
    .setTabEnabled(index, enabled = bool)
    .setTabText(index, text)
    .setTabIcon(index, text)
    .setTabCloseable(closeable= bool)
    .count() -  return the number of tab
    .currentIndex()
    .setCurrentIndex(index)

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
        self.tabbarcreater()

    def initUI(self):
        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(QApplication.instance().quit)  # self.button_exit
        self.layout.addWidget(exitButton)
        self.pushbutton = QPushButton("Bấm để thêm tabbar")
        self.pushbutton.clicked.connect(self.someaction)
        self.layout.addWidget(self.pushbutton)

    def tabbarcreater(self):
        self.tabbar = QTabBar()
        self.tabbar.addTab("Something")
        self.tabbar.setMovable(True)
        self.tabbar.setTabsClosable(True)

        self.layout.addWidget(self.tabbar)
    def someaction(self):
        self.tabbar.insertTab(1, "One more tab")

def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()