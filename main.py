import sys, time, random, string
import BTS
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


def main():
    app = QApplication([])  # Create the application

    figure = BTS.Puddle()
    figure.show()
    app.exec()


if __name__ == "__main__":
    main()
