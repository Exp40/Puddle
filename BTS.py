import string, sys, time, random
from PyQt6.QtWidgets import *
def name_upper(name):
    name_fixer = [firstL for firstL in name]
    name_fixer[0] = name_fixer[0].upper()
    name_compiler = ''
    for letters in name_fixer:
        name_compiler += letters
    name = name_compiler
    return name



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