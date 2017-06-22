from quiz import *
from settings import *
from fileoperation import *

def main():
    print('Hello. This is Testmaker\n')

    read_file()

    random.seed()

    question_list = random.sample(word_list, max_questions)

    quiz(question_list)
    true_answers = 0
    wrong_answers = 0
    for x in answer_list:
        if x['correct']:
            true_answers += 1
        else:
            wrong_answers += 1

    print('\nResult: True', true_answers, 'False', wrong_answers + '\n')

    for x in answer_list:
        if not x['correct']:
            print(x['question'], color.RED + color.BOLD + 'WRONG!' + color.END, 'Correct answer:', x['correct_answer'])

if __name__ == '__main__':
    main()