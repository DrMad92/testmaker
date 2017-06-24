import settings as s

filename = 'word_database'


def search_word(key):
    for word in s.word_list:
        print('Comparing', word)
        if key in word:
            s.word_list = [d for d in s.word_list if d.get(key) != list(word.values())[0]]
            print('Found and Deleted!!!')
            return True
    return False


def read_file():
    try:
        db = s.shelve.open(filename)
        for k, v in db.items():
            word = {k: v}
            if word not in s.word_list:
                s.word_list.append(word)
        db.close()
    except Exception as e:
        print('Error in read_file() -', e)
        return
    return


def write_file():
    try:
        db = s.shelve.open(filename, writeback=True)
        word = {input('Original: '): input('Translation: ')}
        if word not in s.word_list:
            k, v = list(word.items())[0]
            db[k] = v
        else:
            print('Word already exists')
        db.sync()
        db.close()
    except Exception as e:
        print('Error in write_file() -', e)
        return


def delete_file():
    try:
        db = s.shelve.open(filename)
        print('All words:')
        for word in db:
            print(word, '-', db[word])
        user_choice = input('Enter original to delete:')
        if search_word(user_choice):
            db.pop(user_choice)
            print('Success')
        else:
            print('Does not exist')
        db.close()
    except Exception as e:
        print('Error in delete_file -', e)
        return


def show_file():
    try:
        print('All words:')
        for word in s.word_list:
            print(list(word.keys())[0], '-', list(word.values())[0])
    except Exception as e:
        print('Error in show_file() -', e)
        return
