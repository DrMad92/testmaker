from settings import *

fname = 'french phrases.csv'


def read_file():
    try:
        with open(fname, 'r') as csvfile:
            f = csv.reader(csvfile)
            for k, v in f:
                word = {k: v}
                if word not in word_list:
                    word_list.append(word)
    except Exception as e:
        print(e)
        exit(2)
    return


def write_file():
    try:
        with open(fname, 'a', newline='') as csvfile:
            f = csv.writer(csvfile)
            f.writerow([input('Original: '), input('Translation: ')])
    except Exception as e:
        print(e)
        exit(2)

def delete_file():
    pass