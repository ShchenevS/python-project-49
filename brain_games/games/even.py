import random


def task():
    return ('Answer "yes" if the number is even, otherwise answer "no".')


def exercise():
    num_start = 0
    num_stop = 100
    number = random.randint(num_start, num_stop)
    question = f'Question: {number}'
    if number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return (question, correct_answer)
