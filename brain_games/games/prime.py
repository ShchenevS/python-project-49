import random
import prompt


def question():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def function():
    start = 0
    stop = 100
    number = random.randint(start, stop)
    print(f'Question: {number}')
    if number < 2:
        correct_answer = "no"
    else:
        correct_answer = "yes"
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                correct_answer = "no"
                break
    user_answer = prompt.string('Your answer: ')
    return (correct_answer == user_answer, correct_answer, user_answer)
