#!/usr/bin/env python
from brain_games import main_logic as ml
from brain_games.games.calc_game import calculate


def main():
    game_task = 'What is the result of the expression?'
    ml.start_game(game_task, calculate)


if __name__ == "__main__":
    main()
