import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

"""
khi nhập sẽ nhảy ra các lựa chọn kiểu gợi ý
    The Complater object is used to provide auto completions when text is entered into some widgets such as
LineEdit or CommboBox. When a user begins to type, the model content is matched and suggestions are provided
Constructor: completer = QCompleter()
            completer = QCompleter(model)
Methods:
    .model() - return the model
    .setCompletionColumn()
    .setCompletionMode()
        .QCompleter.
            .PopupCompletion - default
            .InlineCompletion - ra luôn gợi ý trong dòng gõ
            .UnfilteredPopupCompletion -  gõ gì thì cũng có thể ra được gợi ý
    .setMaxVisibleItems(intvar)
    .setCaseSensitivity(sensitivity)
        Qt.CaseInsensitive
        Qt.CaseSensitive

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
        self.complettercreater()

    def initUI(self):


        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(QApplication.instance().quit)  # self.button_exit
        self.layout.addWidget(exitButton)

    def complettercreater(self):
        names = ["name1", "name2", "name3", "name4", "name5"]
        self.completter = QCompleter(names)
        self.completter.setCompletionMode(QCompleter.InlineCompletion)
        self.completter.setCaseSensitivity(Qt.CaseSensitive)
        self.lineedit = QLineEdit()
        self.lineedit.setCompleter(self.completter)
        self.layout.addWidget(self.lineedit)
        self.commboBox  = QComboBox()
        self.commboBox.setEditable(True)
        self.commboBox.setCompleter(self.completter)
        self.layout.addWidget(self.commboBox)



def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()