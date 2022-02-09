#!/usr/bin/env python
from brain_games import main_logic as ml
from brain_games.games import progression


def main():
    ml.start_game(progression)


if __name__ == "__main__":
    main()
