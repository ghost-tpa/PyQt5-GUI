import os
import sys
from PyQt5.QtWidgets import *

"""
    A CommboBox provides a dropdown menu attached to a button, providing a list of options of which one
can be selected by the user
Constructor: combobox = QComboBox()
Methods: 
    .addItem(text)
    .insertItem(index, text)
    .addItems(text, text,...., text) -  add multiple items with a single method
    .insertItem(index, text, text,...., text) - 
    .insertSeparator(intvar)
    .removeItem(index)
    .currentIndex()
    .currentText()
    .count()
    .setMaxCount(intvar)
    .setMaxVisibleItems(intvar)
    .showPopup()
    .hiddenPopup()
    .setCompleter(completer)
    .setDuplicatesEnabled(enable=boolvar)
    .setEditable(editable=boolvar)
    .setLineedit(lineedit)
    .lineedit() - call the Lineedit
    .setInsertPolicy(policy)
        .QComboBox.
            .NoInsert
            .InsertAtTop
            .InsertAtCurrent
            .InsertAtBottom
            .InsertAfterCurrent
            .InsertBeforeCurrent
            .InsertAlphabetically
    .setModel(model)
    .setModelColumn(column)
    .activated() - When the user chooses an item
    .currentIndexChanged() - Whenever the current index is changed either by the user or programmatically
    .highlighted() - When an item in the list is highlighted
    
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
        self.commboboxcreater()
        self.combinComboBoxandLineedit()

    def initUI(self):

        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(QApplication.instance().quit)  # self.button_exit
        self.layout.addWidget(exitButton)

    def commboboxcreater(self):
        self.commboBox = QComboBox()
        self.commboBox.setToolTip("Danh sách sản phẩm")
        self.commboBox.setWindowTitle("Danh sách sản phẩm")
        self.layout.addWidget(self.commboBox)
        self.commboBox.setEditable(False)
        self.displaylabel = QLabel()
        self.displaylabel.setText(self.commboBox.currentText())
        self.layout.addWidget(self.displaylabel)
        self.commboBox.insertSeparator(1)
        fopen = open("ChoViet/spkhonggia.txt", "r")
        while fopen.tell() != os.fstat(fopen.fileno()).st_size:
            self.commboBox.insertItem(2, fopen.readline())
        fopen.close()


    def combinComboBoxandLineedit(self):
        self.input = QLineEdit()
        self.input.setPlaceholderText("Nhập tên muốn thêm: ")
        self.layout.addWidget(self.input)
        self.input.returnPressed.connect(self.someaction)


    def someaction(self):
        self.commboBox.insertItem(1, self.input.text())
        self.input.setText("")





def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()