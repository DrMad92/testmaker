import random
import sqlite3
import os
import colorama as col

col.init()

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
