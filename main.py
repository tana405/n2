import sys

from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QPushButton


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 600, 400, 400)
        self.setWindowTitle('Random')
        self.btn = QPushButton('Сгенерировать', self)
        self.btn.setGeometry(300, 200, 30, 30)
        self.btn.clicked.connect(self.on_click)

    def on_click(self):
        QMainWindow.setBrush(QColor(randint(1, 255), randint(1, 255), randint(1, 255)))
        r = randint(1, 150)
        x = randint(1, 150)
        y = randint(1, 150)
        QMainWindow.drawEllipse(x, y, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
