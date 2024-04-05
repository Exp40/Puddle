import sys, time, random, string
import BTS
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


def main():
    puddle_response = 1
    chat_log = ""
    running = True
    app = QApplication([])  # Create the application
    figure = BTS.Form
    figure.show()
    app.exec()


if __name__ == "__main__":
    main()
