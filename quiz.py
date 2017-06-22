import settings as s


def quiz():
    s.random.seed()
    question_list = s.random.sample(s.word_list, s.max_questions)
    i = 1
    while len(question_list) > 0:
        print('\n' + s.color.BOLD + s.color.UNDERLINE + s.color.BLUE + str(i) + ': ', end='')
        question, correct_answer = list(question_list.pop().items())[0]
        choices = [correct_answer]
        while len(choices) < s.max_choices:
            wrong_question_list = s.random.sample(s.word_list, s.max_choices - 1)
            wrong_answer_list = [list(v.values())[0] for v in wrong_question_list]
            if correct_answer not in wrong_answer_list:
                choices = choices + wrong_answer_list

        s.random.shuffle(choices)
        print(question + s.color.END + '\n')
        for j in range(s.max_choices):
            print(str(j + 1) + ')', choices[j])
        user_input = 0
        while user_input > s.max_choices or user_input < 1:
            try:
                user_input = int(input('\n' + s.color.BOLD + 'Choose an answer:' + s.color.END))
            except:
                print('Enter valid answer')

        user_answer = {'question': question,
                       'correct_answer': correct_answer,
                       'user_choice': choices[user_input - 1]}
        if correct_answer == choices[user_input - 1]:
            user_answer['correct'] = True
        else:
            user_answer['correct'] = False
        s.answer_list.append(user_answer)
        i += 1

    true_answers = 0
    wrong_answers = 0
    for x in s.answer_list:
        if x['correct']:
            true_answers += 1
        else:
            wrong_answers += 1

    print('\nResult: True', true_answers, 'False', wrong_answers, '\n')

    for x in s.answer_list:
        if not x['correct']:
            print(x['question'], s.color.RED + s.color.BOLD + 'WRONG!' + s.color.END, 'Correct answer:',
                  x['correct_answer'])
    return
