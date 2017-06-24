import random
import csv
import shelve
import sqlite3


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# Constants
max_questions = 5  # must be less than total dictionary size
max_choices = 5  # number of choices in one question
filename = 'dictionary.db'

# Globals

conn = sqlite3.connect(filename)
cur = conn.cursor()

conn.close()
word_list = []
answer_list = []
