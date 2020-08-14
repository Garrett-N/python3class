import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.CreateApp()

    def CreateApp(self):
        grid = QGridLayout()
        button1 = QPushButton("One")
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")
        button4 = QPushButton("My last button")

        grid.addWidget(button1, 0, 0, 1, 1)
        grid.addWidget(button2, 0, 1, 1, 1)
        grid.addWidget(button3, 0, 2, 1, 1)
        grid.addWidget(button4, 1, 0, 1, 2)

        self.setLayout(grid)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())
