#!/usr/bin/env python
from brain_games import main_logic as ml
from brain_games.games.even_game import is_even


def main():
    game_task = 'Answer "yes" if the number is even, otherwise answer "no".'
    ml.start_game(game_task, is_even)


if __name__ == "__main__":
    main()
