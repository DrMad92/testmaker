from settings import *

def read_file():
    try:
        fname = 'french phrases.csv'
        with open(fname, 'r') as csvfile:
            f = csv.reader(csvfile)
            for k, v in f:
                word = {k: v}
                word_list.append(word)
    except Exception as e:
        print(e)
        exit(2)