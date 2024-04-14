import random


def task():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def exercise():
    start = 0
    stop = 100
    number = random.randint(start, stop)
    print(f'Question: {number}')
    correct_answer = is_prime(number)
    return (correct_answer)


def is_prime(num):
    if num < 2:
        answer = "no"
    else:
        answer = "yes"
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                answer = "no"
                break
    return (answer)
