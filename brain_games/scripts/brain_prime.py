#!/usr/bin/env python
from brain_games import main_logic as ml
from brain_games.games.prime_game import is_prime


def main():
    game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    ml.start_game(game_task, is_prime)


if __name__ == "__main__":
    main()
