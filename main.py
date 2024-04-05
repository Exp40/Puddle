import sys, time, random, string
import BTS
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


def main():
    puddle_response = 0
    chat_log = ""
    running = True
    app = QApplication([])  # Create the application

    window = QWidget()
    top_window = QWidget()  # Creates the windows to put things into
    bottom_window = QWidget()

    layout = QVBoxLayout()
    top_layout = QHBoxLayout()
    bottom_layout = QVBoxLayout()

    window.setLayout(layout)
    top_window.setLayout(top_layout)
    bottom_window.setLayout(bottom_layout)

    cancel_button = QPushButton()
    puddle_speech = QLabel(str(puddle_response))
    speech_box = QLineEdit(bottom_window)
    top_layout.addWidget(cancel_button)
    top_layout.addWidget(puddle_speech)
    bottom_layout.addWidget(speech_box)
    cancel_button.clicked.connect(BTS.value_flipper(running))
    layout.addLayout(top_layout)
    layout.addLayout(bottom_layout)

    layout.addWidget(top_window)
    layout.addWidget(bottom_window)

    response_timer = QTimer()

    window.resize(600, 400)

    while running:
        puddle_response += 1
        puddle_speech.setText(str(puddle_response))

        response_timer.setInterval(1000)
        response_timer.start()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
