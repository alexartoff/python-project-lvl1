#!/usr/bin/env python
from brain_games import main_logic as ml
from brain_games.games.gcd_game import find_gcd


def main():
    game_task = 'Find the greatest common divisor of given numbers.'
    ml.start_game(game_task, find_gcd)


if __name__ == "__main__":
    main()
