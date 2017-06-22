from settings import *


def quiz(question_list):
    i = 1
    while len(question_list) > 0:
        print('\n'+ color.BOLD + color.UNDERLINE + color.BLUE + str(i) + ': ', end='')
        question, correct_answer = list(question_list.pop().items())[0]
        choices = [correct_answer]
        while len(choices) < max_choices:
            wrong_question_list = random.sample(word_list, max_choices - 1)
            wrong_answer_list = [list(v.values())[0] for v in wrong_question_list]
            if correct_answer not in wrong_answer_list:
                choices = choices + wrong_answer_list

        random.shuffle(choices)
        print(question + color.END + '\n')
        for j in range(max_choices):
            print(str(j + 1) + ')', choices[j])
        user_input = 0
        while user_input > max_choices or user_input < 1:
            try:
                user_input = int(input('\n'+ color.BOLD + 'Choose an answer:' + color.END))
            except:
                print('Enter valid answer')

        user_answer = {'question': question,
                       'correct_answer': correct_answer,
                       'user_choice': choices[user_input - 1]}
        if correct_answer == choices[user_input - 1]:
            user_answer['correct'] = True
        else:
            user_answer['correct'] = False
        answer_list.append(user_answer)
        i += 1
