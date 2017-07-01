import quiz as q
import settings as s
import file_operation as fileop
import database_operation as dataop


def main():
    print('Hello. This is Testmaker\n')
    dataop.get_databases()
    while True:
        if len(s.lang_list) == 0:
            print('Please add language')
            dataop.create_database()
        for lang in s.lang_list:
            print(lang)
        lang_choice = input("\nChoose language or type exit: ")
        if lang_choice.lower() == 'exit':
            exit()
        elif lang_choice.lower() not in s.lang_list:
            print('Does not exist.')
        else:
            dataop.connect_database(lang_choice + '.db')
            break

    while True:
        fileop.get_categories()
        main_input = 0
        while main_input > 4 or main_input < 1:
            try:
                print('\n1) Start quiz'
                      '\n2) Manage dictionary'
                      '\n3) Change language'
                      '\n4) Exit')
                main_input = int(input('\n' + s.color.BOLD + 'Choose an option:' + s.color.END))
            except:
                print('Enter valid option')

        if main_input == 1:
            quiz_input = 0
            while quiz_input > 3 or quiz_input < 1:
                try:
                    print('\n1) Choose category'
                          '\n2) All'
                          '\n3) Go back')
                    quiz_input = int(input('\n' + s.color.BOLD + 'Choose an option:' + s.color.END))
                except:
                    print('Enter valid option')
            if quiz_input == 1:
                q.start_quiz('category')
            elif quiz_input == 2:
                q.start_quiz()
            else:
                pass  # Go to main menu
        elif main_input == 2:
            dict_input = 0
            while dict_input > 5 or dict_input < 1:
                try:
                    print('\n1) View dictionary'
                          '\n2) Add new category'
                          '\n3) Edit category'
                          '\n4) Delete category'
                          '\n5) Go back')
                    dict_input = int(input('\n' + s.color.BOLD + 'Choose an option:' + s.color.END))
                except:
                    print('Enter valid option')
            if dict_input == 1:
                fileop.view_dict()  # Make it beautiful
            elif dict_input == 2:
                fileop.add_category()
            elif dict_input == 3:
                cat_input = 0
                while cat_input > 5 or cat_input < 1:
                    try:
                        print('\n1) Rename category'
                              '\n2) Add new word'
                              '\n3) Edit word'
                              '\n4) Delete word'
                              '\n5) Go back')
                        cat_input = int(input('\n' + s.color.BOLD + 'Choose an option:' + s.color.END))
                    except:
                        print('Enter valid option')
                if cat_input == 1:
                    fileop.rename_category()
                elif cat_input == 2:
                    fileop.add_word()
                elif cat_input == 3:
                    fileop.edit_word()
                elif cat_input == 4:
                    fileop.delete_word()
                else:
                    pass  # Go to manage dictionary menu
            elif dict_input == 4:
                fileop.delete_category()
            else:
                pass  # Go to main menu
        elif main_input == 3:
            lang_input = 0
            while lang_input > 3 or lang_input < 1:
                try:
                    print('\n1) Change language'
                          '\n2) Add new language'
                          '\n3) Go back')
                    lang_input = int(input('\n' + s.color.BOLD + 'Choose an option:' + s.color.END))
                except:
                    print('Enter valid option')
            if lang_input == 1:
                dataop.change_database()
            elif lang_input == 2:
                dataop.create_database()
            else:
                pass  # Go to main menu
        else:
            s.conn.close()
            return


if __name__ == '__main__':
    main()
