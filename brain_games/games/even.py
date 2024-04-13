import random
import prompt


def question():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def function():
    num_start = 0
    num_stop = 100
    number = random.randint(num_start, num_stop)
    print(f'Question: {number}')
    if number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    user_answer = prompt.string('Your answer: ')
    return (correct_answer == user_answer, correct_answer, user_answer)
