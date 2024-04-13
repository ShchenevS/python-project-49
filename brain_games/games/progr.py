import random
import prompt


def question():
    print('What number is missing in the progression?')


def function():
    start_1 = 0
    stop_1 = 100
    progr_start = random.randint(start_1, stop_1)
    progr_diff = random.randint(start_1, stop_1)
    start_2 = 5
    stop_2 = 15
    progr_size = random.randint(start_2, stop_2)
    progr = []
    for i in range(progr_size):
        progr.append(str(progr_start + i * progr_diff))
    hidden_index = random.randint(0, progr_size - 1)
    correct_answer = progr[hidden_index]
    progr[hidden_index] = ".."
    quest = ' '.join(progr)
    print(f'Question: {quest}')
    user_answer = prompt.string('Your answer: ')
    return (str(correct_answer) == user_answer, correct_answer, user_answer)
