import settings as s


def get_categories():
    for x in s.cur.execute("select name from sqlite_master where type = 'table'"):
        if x[0] not in s.category_list:
            s.category_list.append(x[0])


def view_dict():
    get_categories()
    for cat in s.category_list:
        print('\nCategory: ' + cat + ':')
        print('\nId----Original----Translation\n')
        for row in s.cur.execute('SELECT * FROM ' + cat):
            print(row[0], row[1], row[2])


def add_category():
    get_categories()
    print('Categories:')
    for x in s.category_list:
        print(x)

    new_category = input('Enter new category name to add: ')
    if new_category in s.category_list:
        print('Already exists. Going back to menu.')
        return

    s.cur.execute("CREATE TABLE " + new_category + "(Id, Original, Translation)")
    s.conn.commit()


def delete_category():
    get_categories()
    print('Categories:')
    for x in s.category_list:
        print(x)

    category2delete = input('Enter the name of category to delete: ')
    if category2delete not in s.category_list:
        print('Not found. Going back to menu.')
        return

    s.cur.execute('DROP TABLE IF EXISTS ' + category2delete)
    s.category_list = [c for c in s.category_list if c != category2delete]


def rename_category():
    get_categories()
    print('Categories:')
    for x in s.category_list:
        print(x)

    old_name = input('Choose category: ')
    if old_name not in s.category_list:
        print("Doesn't exist. Going back to menu")
        return

    new_name = input('Input new name (case-insensitive): ')
    if new_name.lower() in map(str.lower, s.category_list):
        print("Already exists. Going back to menu")
        return

    s.cur.execute('ALTER TABLE ' + old_name + ' RENAME TO ' + new_name)
    s.conn.commit()


def add_word():
    get_categories()
    print('Categories:')
    for x in s.category_list:
        print(x)

    name = input('Choose category: ')
    if name not in s.category_list:
        print("Doesn't exist. Going back to menu")
        return

    print('\nCategory: ' + name + ':')
    print('\nId----Original----Translation\n')
    for row in s.cur.execute('SELECT * FROM ' + name):
        print(row[0], row[1], row[2])

    new_original = input('\nEnter original: ')
    s.cur.execute('SELECT * FROM ' + name + ' WHERE Original = \"' + new_original + '\"')
    temp_list = s.cur.fetchall()
    if len(temp_list) != 0:
        print('Word already exists. Going back to menu')
        return

    new_translation = input('Enter translation: ')
    s.cur.execute('SELECT id FROM ' + name)
    id_list = [int(x[0]) for x in s.cur.fetchall()]

    new_id = None
    for i in range(1, max(id_list)):
        if i not in id_list:
            new_id = i
            break
    if new_id is None:
        new_id = max(id_list) + 1

    values = (new_id, new_original, new_translation)
    s.cur.execute('INSERT INTO ' + name + ' VALUES (?,?,?)', values)
    s.conn.commit()
