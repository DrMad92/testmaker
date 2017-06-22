import csv
import random

# Constants
max_questions = 10  # must be less than total dictionary size
max_choices = 5  # number of choices in one question

print('Hello. This is Testmaker')

word_list = []
try:
    fname = 'wordlist.csv'
    with open(fname, 'r') as csvfile:
        f = csv.reader(csvfile)
        for k, v in f:
            word = {k: v}
            word_list.append(word)
except Exception as e:
    print(e)
    exit(2)

random.seed()

question_list = random.sample(word_list, max_questions)
answer_list = []

i = 1
while len(question_list) > 0:
    print('Question ' + str(i) + ':')
    question, correct_answer = list(question_list.pop().items())[0]
    choices = [correct_answer]
    while len(choices) < max_choices:
        wrong_question_list = random.sample(word_list, max_choices - 1)
        wrong_answer_list = [list(v.values())[0] for v in wrong_question_list]
        if correct_answer not in wrong_answer_list:
            choices = choices + wrong_answer_list

    random.shuffle(choices)
    print(question)
    for j in range(max_choices):
        print(str(j + 1) + ')', choices[j])
    user_input = 0
    while user_input > max_choices or user_input < 1:
        try:
            user_input = int(input('Choose an answer:'))
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

print('Results:')
true_answers = 0
wrong_answers = 0
for x in answer_list:
    if x['correct']:
        print('Question', x['question'], 'correct!')
        true_answers += 1
    else:
        print('Question', x['question'], 'wrong!', 'Correct answer was', x['correct_answer'])
        wrong_answers += 1

print('Overall: True', true_answers, 'False', wrong_answers)
