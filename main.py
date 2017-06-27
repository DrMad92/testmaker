import quiz as q
import settings as s
import fileoperation as fileop


def main():
    print('Hello. This is Testmaker\n')

    while True:
        main_input = 0
        while main_input > 4 or main_input < 1:
            try:
                print('\n1) Start quiz'
                      '\n2) Manage dictionary'
                      '\n3) Statistics'
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
                q.start_quiz('category')  # Fix this
            elif quiz_input == 2:
                q.start_quiz('all') # Fix this
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
                    fileop.edit_word()  # Fix this
                elif cat_input == 4:
                    fileop.delete_word()  # Fix this
                else:
                    pass  # Go to manage dictionary menu
            elif dict_input == 4:
                fileop.delete_category()
            else:
                pass  # Go to main menu
        elif main_input == 3:
            pass  # Fix this - Statistics
        else:
            s.conn.close()
            return


if __name__ == '__main__':
    main()
