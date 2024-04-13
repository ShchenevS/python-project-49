import random


def task():
    print('What is the result of the expression?')


def exercise():
    num_start = 0
    num_stop = 100
    number1 = random.randint(num_start, num_stop)
    number2 = random.randint(num_start + 1, num_stop)
    op_range = '+-*'
    operator = random.choice(op_range * 10)
    print(f'Question: {number1} {operator} {number2}')
    match operator:
        case '+':
            correct_answer = number1 + number2
        case '-':
            correct_answer = number1 - number2
        case '*':
            correct_answer = number1 * number2
    return (correct_answer)
