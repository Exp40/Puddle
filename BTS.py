import string, sys, time, random
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
def name_upper(name):
    name_fixer = [firstL for firstL in name]
    name_fixer[0] = name_fixer[0].upper()
    name_compiler = ''
    for letters in name_fixer:
        name_compiler += letters
    name = name_compiler
    return name

def running():
    run_game = True

def random_choice_from_list(phrase_list):
    rand_index = random.randint(0, (len(phrase_list)-1)) #Chooses a random number between 1 and the length of the file being input. The minus one is to make sure it doesn't overflow
    return rand_index
def make_list_from_file(file_name): #Creates a usable list from a file. Specifically, turns the greetings compilation and responses files into lists to be used later.
    lines = []
    for line in file_name:
        line = line.strip() #Gets rid of new lines
        lines.append(line) #adds the line to a list
    return lines

def make_response_dictionary(list_param):
    keys_and_responses = {}
    for items in list_param:
        split_items = items.split(",") #gets rid of the comma in the responses to make the first word a key.
        if split_items[0] not in keys_and_responses.keys():
            keys_and_responses[split_items[0]] = split_items[1 + (len(split_items) - 2)] #Makes the first word the key and assigns that key the rest of the string as a value.
    return keys_and_responses

def respond(self, human_text):
    human_text = human_text.lower()
    human_text = human_text.translate(str.maketrans('', '', string.punctuation)) #Removes all punctuation from the input so the computer doesn't get confused.
    human_text = human_text.split() #Removes spaces and such
    has_word = False
    more_than_one = []
    for key_search in human_text: #This whole thing checks whether one of the 'trigger' words are in the user input.
        has_word = False
        if key_search in self.keyword_and_response.keys(): #Checks if any words are a key in a dictionary.
            word_holder = key_search
            more_than_one.append(word_holder) #takes any extra words that have a response so there can be a random choice between the responses.
            has_word = True
    if has_word:
        if len(more_than_one) > 1: #This is what chooses that random response so long as there is "more than one".
            choice = random_choice_from_list(more_than_one)
            result = more_than_one[choice]
            return self.keyword_and_response[result] #Returns the result of the toss up.
        else:
            return self.keyword_and_response[word_holder] #Returns the response to the hot word.
    else:
        return self.default_response #Returns a default

def select_speaker(speaker, speech):
    processed_speech = f"{speaker}: {speech}"
    return

def converse(speech):
    response_timer = QTimer()

    changed = speech.setText("")
    response_timer.setInterval(1000)
    response_timer.start()
    return changed
class Puddle(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Starting...")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.counter = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_label)
        self.timer.start(1000)  # Update label every 1 second
        self.window = QWidget()
        self.top_window = QWidget()  # Creates the windows to put things into
        self.bottom_window = QWidget()

        layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        bottom_layout = QVBoxLayout()

        self.window.setLayout(layout)
        self.top_window.setLayout(top_layout)
        self.bottom_window.setLayout(bottom_layout)

        cancel_button = QPushButton()
        puddle_speech = QLabel()
        speech_box = QLineEdit(self.bottom_window)
        top_layout.addWidget(cancel_button)
        top_layout.addWidget(puddle_speech)
        bottom_layout.addWidget(speech_box)
        layout.addLayout(top_layout)
        layout.addLayout(bottom_layout)

        # Add the physical response element

        layout.addWidget(self.top_window)
        layout.addWidget(self.bottom_window)

        response_timer = QTimer()

        self.window.resize(600, 400)

    def update_label(self):
        self.label.setText(f"Counter: {self.counter}")
        self.counter += 1

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit("")
        self.button = QPushButton("Respond")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

    # Greets the user
    def greetings(self):
        print(f"Hello {self.edit.text()}")