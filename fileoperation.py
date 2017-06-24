import settings as s


def search_word(key):
    for word in s.word_list:
        print('Comparing', word)
        if key in word:
            s.word_list = [d for d in s.word_list if d.get(key) != list(word.values())[0]]
            print('found and deleted')
            return True
    return False


def read_file():
    pass


def write_file():
    pass


def delete_file():
   pass


def show_file():
    try:
        print('All words:')
        for word in s.word_list:
            print(list(word.keys())[0], '-', list(word.values())[0])
    except Exception as e:
        print('Error in show_file() -', e)
        return
