import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
"""
Học về Label
các method của label 
    .setWordWrap(BoolVar)  # bọc chữ lại
    .setAlignment(alignment)  # căn chỉnh
        Qt.AlignLeft()
        Qt.AlignHCenter()  #  hightCenter
        Qt.AlignRight()
        Qt.AlignJustify()
        
    set the vertical alignment possion:
        Qt.AlignTop
        Qt.AlignVCenter   # Chính giữa
        Qt.AlighnBottom
        Qt.AlignBaseLine 
        
"""

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Chúng ta học về Label")
        self.setMinimumWidth(400)
        self.setMinimumHeight(300)

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel("Đây là 1 label")
        layout.addWidget(label, 0, 0)

        label = QLabel("Đây là label thứ 2 của tôi")
        label.setWordWrap(True)  # bọc chữ lại đẹp hơn
        label.setAlignment(Qt.AlignBottom)  # Class Qt from QtCore
        layout.addWidget(label, 0, 1)

        label = QLabel("Đây là label thứ 3 của tôi")
        label.setIndent(8)
        layout.addWidget(label, 1, 1)



def main():
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()