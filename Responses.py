import sys, time, random

def name_upper(name):
    name_fixer = [firstL for firstL in name]
    name_fixer[0] = name_fixer[0].upper()
    name_compiler = ''
    for letters in name_fixer:
        name_compiler += letters
    name = name_compiler
    return name
