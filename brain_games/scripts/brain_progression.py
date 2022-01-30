#!/usr/bin/env python
from brain_games import main_logic as ml
from brain_games.games.progression_game import progression


def main():
    game_task = 'What number is missing in the progression?'
    ml.start_game(game_task, progression)


if __name__ == "__main__":
    main()
