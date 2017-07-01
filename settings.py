import random
import sqlite3
import os


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
path = 'lang_files'  # name of directory for creating new database (see readme)
root = os.getcwd()

# Globals
conn = None  # connection handle
cur = None  # cursor

lang_list = []
category_list = []
word_list = []
answer_list = []
