#!/usr/bin/env python3
import brain_games.engine
from brain_games.games import calc


def main():
    brain_games.engine.run_games(calc)


if __name__ == '__main__':
    main()
