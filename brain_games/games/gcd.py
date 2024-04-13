import random


def task():
    print('Find the greatest common divisor of given numbers.')


def exercise():
    num_start = 0
    num_stop = 100
    number1 = random.randint(num_start, num_stop)
    number2 = random.randint(num_start, num_stop)
    print(f'Question: {number1} {number2}')
    if min(abs(number1), abs(number2)) == 0:
        divisor = 1
    else:
        divisor = min(abs(number1), abs(number2))
        while divisor > 1:
            if number1 % divisor == 0 and number2 % divisor == 0:
                break
            divisor -= 1
    correct_answer = divisor
    return (correct_answer)
