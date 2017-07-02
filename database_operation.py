import settings as s
import glob


def get_databases():
    s.os.chdir(s.root)
    print('List of available languages:\n')
    for filename in glob.glob('*.db'):
        if filename[:-3] not in s.lang_list:
            s.lang_list.append(filename[:-3])


def connect_database(database):
    del s.category_list[:]
    s.conn = s.sqlite3.connect(database)
    s.cur = s.conn.cursor()


def disconnect_database():
    try:
        s.conn.close()
    except AttributeError as e:
        pass


def change_database():
    for lang in s.lang_list:
        print(lang)
    lang_input = input("Choose language: ")
    if lang_input not in s.lang_list:
        print('Does not exist. Going back to menu')
        return

    disconnect_database()
    connect_database(lang_input + '.db')


def create_database():
    s.os.chdir(s.root)
    print('List of available languages to install:')
    s.os.chdir(s.path)
    temp_list = []
    for filename in s.os.listdir(s.os.getcwd()):
        if filename in s.lang_list:
            print(filename, 'Already installed')
        else:
            print(filename)
            temp_list.append(filename)

    print('Choose from:')
    for x in temp_list:
        print(x)
    user_choice = input('Choose language:')
    if user_choice not in temp_list:
        print('Does not exist. Going back to menu')
        return

    disconnect_database()
    s.os.chdir(s.root)
    connect_database(user_choice + '.db')
    s.os.chdir(s.path)
    s.os.chdir(user_choice)
    cat_list = glob.glob('*.txt')
    for category_name in cat_list:
        s.cur.execute("CREATE TABLE '" + category_name[:-4] + "' (Id, Original, Translation)")
        with open(category_name, 'r', encoding='utf-8') as f:
            word_temp_list = [line.rstrip().split(',') for line in f]
            i = 1
            for word in word_temp_list:
                s.cur.execute("INSERT INTO '" + category_name[:-4] + "' VALUES (?,?,?)", (str(i), word[0], word[1]))
                s.conn.commit()
                i += 1
    return


