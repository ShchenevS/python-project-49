import prompt
from brain_games.constant import AMOUNT_OF_TRY


def run_games(purpose):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    purpose.task()
    count = 0
    while count < AMOUNT_OF_TRY:
        correct_answer = purpose.exercise()
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(correct_answer):
            print("Correct!")
            count += 1
        else:
            text = 'is wrong answer ;(. Correct answer was'
            print(f"'{user_answer}' {text} '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
