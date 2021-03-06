import settings as s


def start_quiz(choice='all'):
    s.random.seed()
    if choice == 'category':
        print('Categories:\n')
        for x in s.category_list:
            print(x)

        user_cat = input('\nChoose category: ')
        if user_cat.lower() not in s.category_list:
            print('Does not exist: Going back to menu')
            return

        s.cur.execute("SELECT Original,Translation FROM '" + user_cat + "'")
        temp_list = s.cur.fetchall()
        for x in temp_list:
            word = {x[0]: x[1]}
            if word not in s.word_list:
                s.word_list.append(word)
    elif choice == 'all':
        for cat in s.category_list:
            s.cur.execute("SELECT Original,Translation FROM '" + cat + "'")
            temp_list = s.cur.fetchall()
            for x in temp_list:
                word = {x[0]: x[1]}
                if word not in s.word_list:
                    s.word_list.append(word)

    question_list = s.random.sample(s.word_list, s.max_questions)
    i = 1
    while len(question_list) > 0:
        print('\n' + s.col.Fore.YELLOW + s.col.Style.BRIGHT + str(i) + ': ', end='')
        question, correct_answer = list(question_list.pop().items())[0]
        choices = [correct_answer]
        while len(choices) < s.max_choices:
            wrong_question_list = s.random.sample(s.word_list, s.max_choices - 1)
            wrong_answer_list = [list(v.values())[0] for v in wrong_question_list]
            if correct_answer not in wrong_answer_list:
                choices = choices + wrong_answer_list

        s.random.shuffle(choices)
        print(question + s.col.Style.RESET_ALL + '\n')
        for j in range(s.max_choices):
            print(str(j + 1) + ')', choices[j])
        user_input = 0
        while user_input > s.max_choices or user_input < 1:
            try:
                print('\n' + s.col.Style.BRIGHT)
                user_input = int(input('Choose an answer:'))
                print(s.col.Style.RESET_ALL)
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

    print('\nResult: True', s.col.Style.BRIGHT + s.col.Fore.GREEN + str(true_answers) + s.col.Style.RESET_ALL,
          'False', s.col.Style.BRIGHT + s.col.Fore.RED + str(wrong_answers) + s.col.Style.RESET_ALL, '\n')

    for x in s.answer_list:
        if not x['correct']:
            print(s.col.Style.BRIGHT, x['question'], s.col.Fore.RED + 'WRONG!' + s.col.Style.RESET_ALL,
                  'Correct answer:', s.col.Style.BRIGHT, x['correct_answer'], s.col.Style.RESET_ALL)

    del s.word_list[:]
    del s.answer_list[:]
    return
