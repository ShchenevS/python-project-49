#!/usr/bin/env python3
import brain_games.engine
from brain_games.games import gcd


def main():
    brain_games.engine.engine(gcd)


if __name__ == '__main__':
    main()
