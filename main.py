import sys

from PyQt5 import uic
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QPushButton, QLabel, QSpinBox, QCheckBox


class FMain(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)  # Загружаем дизайн
        self.btn.clicked.connect(self.on_click)

    def on_click(self):
        QMainWindow.setBrush(QColor(255, 255, 0))
        r = randint(1, 150)
        x = randint(1, 150)
        y = randint(1, 150)
        QMainWindow.drawEllipse(x, y, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FMain()
    ex.show()
    sys.exit(app.exec_())
