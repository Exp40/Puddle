import sys, time, random, string
import BTS
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


def main():
    puddle_response = ""
    chat_log = ""
    app = QApplication([])  # Create the application

    window = QWidget()
    top_window = QWidget()  # Creates the windows to put things into
    bottom_window = QWidget()

    layout = QVBoxLayout()
    top_layout = QHBoxLayout()
    bottom_layout = QHBoxLayout()

    window.setLayout(layout)
    top_window.setLayout(top_layout)
    bottom_window.setLayout(bottom_layout)

    puddle_speech = QLabel(puddle_response)
    puddle_name = QLabel("Puddle")
    user_name = QLabel("User")
    top_layout.addWidget(puddle_speech)
    bottom_layout.addWidget(user_name)
    layout.addLayout(top_layout)
    layout.addLayout(bottom_layout)

    layout.addWidget(top_window)
    layout.addWidget(bottom_window)

    window.resize(600, 400)

    window.show()
    app.exec()


if __name__ == "__main__":
    main()
