import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QHBoxLayout, QVBoxLayout,
                             QPushButton, QLabel, QLineEdit
                             )


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label = QLabel("Name: ")
        name_input = QLineEdit()
        button = QPushButton("Set Name")

        h = QHBoxLayout()
        h.stretch(1)
        h.addWidget(label)
        h.addWidget(name_input)

        v = QVBoxLayout()
        v.addStretch(1)
        v.addLayout(h)
        v.addWidget(button)

        self.setLayout(v)

        self.setWindowTitle("Horizontal Layout")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
        
