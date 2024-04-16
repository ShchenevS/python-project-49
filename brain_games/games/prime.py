import random


def task():
    return('Answer "yes" if given number is prime. Otherwise answer "no".')


def exercise():
    start = 0
    stop = 100
    number = random.randint(start, stop)
    question = f'Question: {number}'
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (question, correct_answer)


def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        return True
