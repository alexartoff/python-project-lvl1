#!/usr/bin/env python
from brain_games import main_logic as ml
from brain_games.games import even


def main():
    ml.run_game(even)


if __name__ == "__main__":
    main()
