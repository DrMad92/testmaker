import quiz as q
import settings as s
import fileoperation as fileop


def main():
    print('Hello. This is Testmaker\n')

    fileop.read_file()
    print('Total number of questions:', len(s.word_list))
    user_input = 0
    while user_input > 2 or user_input < 1:
        try:
            print('\n1)Start quiz\n2)Add new translations')
            user_input = int(input('\n' + s.color.BOLD + 'Choose an option:' + s.color.END))
        except:
            print('Enter valid option')

    if user_input == 1:
        q.quiz()
    elif user_input == 2:
        fileop.write_file()

    return

if __name__ == '__main__':
    main()
