import sys
from PyQt5.QtWidgets import *

"""
Lineedit là chỗ để nhập thông tin
method 
    .setText()
    .insert()
    
    .setPlaceholderText(text)  # set text chìm ở box
    .setReadOnly(read_only = bool)
    
signals: Nếu bấm enter hoặc Return sau khi nhập văn bản, Lineedit có thể được làm để chạy hàm:
    .returnPressed.connect(some_function)
    .textChanged.connect(some_function)
"""


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Học lineedit")
        self.setMinimumHeight(400)
        self.setMinimumHeight(500)

        layout = QGridLayout()
        self.setLayout(layout)

        self.lineedit = QLineEdit()
        # self.lineedit.setText("Nhập vào đây")
        self.lineedit.setPlaceholderText("PlaceHolder Text")
        # self.lineedit.setReadOnly(True)
        self.lineedit.returnPressed.connect(self.return_Pressed)  # enter rồi mới thực hiện
        # self.lineedit.textChanged.connect(self.return_Pressed)  # thực hiện luôn trong khi gõ
        layout.addWidget(self.lineedit, 0, 0)

        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(QApplication.instance().quit)  # self.button_exit
        layout.addWidget(exitButton, 3, 1)

    def return_Pressed(self):
        print(self.lineedit.text())

    def button_exit(self):
        exit(0)

def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
