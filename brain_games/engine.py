import prompt


def engine(purpose):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    purpose.task()
    count = 0
    amount_of_try = 3
    while count < amount_of_try:
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
