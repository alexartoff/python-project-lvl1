#!/usr/bin/env python
from brain_games import main_logic as ml
from brain_games.games import gcd


def main():
    ml.start_game(gcd)


if __name__ == "__main__":
    main()
