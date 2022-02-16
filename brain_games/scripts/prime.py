#!/usr/bin/env python
from brain_games import main_logic as ml
from brain_games.games import prime


def main():
    ml.run_game(prime)


if __name__ == "__main__":
    main()
