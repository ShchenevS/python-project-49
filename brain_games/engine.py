import prompt
import brain_games.games.even
import brain_games.games.calc
import brain_games.games.gcd
import brain_games.games.progr
import brain_games.games.prime


def engine(purpose):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    match purpose:
        case 'even':
            brain_games.games.even.task()
        case 'calc':
            brain_games.games.calc.task()
        case 'gcd':
            brain_games.games.gcd.task()
        case 'progr':
            brain_games.games.progr.task()
        case 'prime':
            brain_games.games.prime.task()
    count = 0
    amount_of_try = 3
    while count < amount_of_try:
        match purpose:
            case 'even':
                correct_answer = brain_games.games.even.exercise()
            case 'calc':
                correct_answer = brain_games.games.calc.exercise()
            case 'gcd':
                correct_answer = brain_games.games.gcd.exercise()
            case 'progr':
                correct_answer = brain_games.games.progr.exercise()
            case 'prime':
                correct_answer = brain_games.games.prime.exercise()
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
