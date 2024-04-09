import prompt
import brain_games.even
import brain_games.calc
import brain_games.gcd
import brain_games.progr
import brain_games.prime


def engine(purpose):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    match purpose:
        case 'even':
            brain_games.even.question()
        case 'calc':
            brain_games.calc.question()
        case 'gcd':
            brain_games.gcd.question()
        case 'progr':
            brain_games.progr.question()
        case 'prime':
            brain_games.prime.question()
    count = 0
    while count < 3:
        match purpose:
            case 'even':
                result = brain_games.even.function()
            case 'calc':
                result = brain_games.calc.function()
            case 'gcd':
                result = brain_games.gcd.function()
            case 'progr':
                result = brain_games.progr.function()
            case 'prime':
                result = brain_games.prime.function()
        if result[0]:
            print("Correct!")
            count += 1
        else:
            print(f"'{result[2]}' is wrong answer ;(. Correct answer was '{result[1]}'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
