import prompt
import brain_games.even
import brain_games.calc


def engine(purpose):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    match purpose:
        case 'even':
            brain_games.even.question()
        case 'calc':
            brain_games.calc.question()
    count = 0
    while count < 3:
        match purpose:
            case 'even':
                result = brain_games.even.function()
            case 'calc':
                result = brain_games.calc.function()
        if result[0]:
            print("Correct!")
            count += 1
        else:
            print(f"'{result[2]}' is wrong answer ;(. Correct answer was '{result[1]}'.")
            print(f"Let's try again,{name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
