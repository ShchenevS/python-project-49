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
                result = brain_games.games.even.exercise()
            case 'calc':
                result = brain_games.games.calc.exercise()
            case 'gcd':
                result = brain_games.games.gcd.exercise()
            case 'progr':
                result = brain_games.games.progr.exercise()
            case 'prime':
                result = brain_games.games.prime.exercise()
        if result[0]:
            print("Correct!")
            count += 1
        else:
            text = 'is wrong answer ;(. Correct answer was'
            print(f"'{result[2]}' {text} '{result[1]}'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
