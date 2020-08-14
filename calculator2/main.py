import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Button:
    def __init__(self, text, results):
        self.b = QPushButton(str(text))
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda: self.handleInput(self.text))

    def handleInput(self, v):
        print("clicked", v)


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.CreateApp()

    def CreateApp(self):
        grid = QGridLayout()
        results = QLineEdit()

        buttons = ["AC", "C", "CE", "/",
                   7, 8, 9, "*",
                   4, 5, 6, "-",
                   1, 2, 3, "+",
                   0, ".", "="]

        row = 1
        col = 0

        grid.addWidget(results, 0, 0, 1, 4)

        for button in buttons:
            if col > 3:
                col = 0
                row += 1

            buttonObject = Button(button, results)

            if button == 0:
                grid.addWidget(buttonObject.b, row, col, 1, 2)
                col += 1
            else:
                grid.addWidget(buttonObject.b, row, col, 1, 1 )
            col += 1

        self.setLayout(grid)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())
