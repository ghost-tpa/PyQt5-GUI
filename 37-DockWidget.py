import sys
from PyQt5.QtWidgets import *

"""
    A DockWidget provides a widget which is able to be docked inside the main window,
or placed in it own separate window. The widget is useful for holding widgets where it would be useful to 
separate them from the main interface
Constructor: dockwidget = QDockWidget()
Methods:
    .setWidget()
    .widget()  - return child widget
    .setFloating(float) -  The palette can be set to floating programmatically required
    .isFloating() - return floating status
    .setFeatures(features)
        .QDockWidget.DockWidgetClosable
        .QDockWidget.DockWidgetMoveable
        .QDockWidget.DockWidgetFloatable
        .QDockWidget.
    .setTitleBarWidget(widget)
        
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
        self.dockwidgetcreater()

    def initUI(self):
        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(QApplication.instance().quit)  # self.button_exit
        self.layout.addWidget(exitButton)

    def dockwidgetcreater(self):
        self.dockwidget = QDockWidget("Something")
        self.treewidget = QTreeWidget()
        self.dockwidget.setWidget(self.treewidget)
        self.dockwidget.setFloating(True)
        self.dockwidget.setTitleBarWidget(self.treewidget)
        label = QLabel("Dockwidget is docked")
        self.layout.addWidget(label)
        self.layout.addWidget(self.dockwidget)



def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()