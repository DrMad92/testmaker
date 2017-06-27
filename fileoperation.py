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
            print(row[0],row[1],row[2])


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
