import quiz as q
import settings as s
import fileoperation as fileop


def main():
    print('Hello. This is Testmaker\n')

    while True:
        fileop.read_file()
        print('Total number of questions:', len(s.word_list))
        user_input = 0
        while user_input > 4 or user_input < 1:
            try:
                print('\n1)Start quiz\n2)Manage dictionary\n3)Statistics\n4)Exit')
                user_input = int(input('\n' + s.color.BOLD + 'Choose an option:' + s.color.END))
            except:
                print('Enter valid option')

        if user_input == 1:
            q.quiz()
        elif user_input == 2:
            dict_input = 0
            while dict_input > 3 or dict_input < 1:
                try:
                    print('\n1)Add new word\n2)Delete word\n3)Show list\n4)Go back')
                    dict_input = int(input('\n' + s.color.BOLD + 'Choose an option:' + s.color.END))
                except:
                    print('Enter valid option')
            if dict_input == 1:
                fileop.write_file()
            elif dict_input == 2:
                fileop.delete_file()
            elif dict_input == 3:
                fileop.show_file()
            else: break
        elif user_input == 3:
            pass
        else: return

if __name__ == '__main__':
    main()
