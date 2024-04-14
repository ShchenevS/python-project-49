import random


def task():
    print('Find the greatest common divisor of given numbers.')


def exercise():
    num_start = 0
    num_stop = 100
    number1 = random.randint(num_start, num_stop)
    number2 = random.randint(num_start, num_stop)
    print(f'Question: {number1} {number2}')
    correct_answer = gcd_calc(number1, number2)
    return (correct_answer)


def gcd_calc(num1, num2):
    if min(abs(num1), abs(num2)) == 0:
        divisor = 1
    else:
        divisor = min(abs(num1), abs(num2))
        while divisor > 1:
            if num1 % divisor == 0 and num2 % divisor == 0:
                break
            divisor -= 1
    return divisor
