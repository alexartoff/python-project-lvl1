#!/usr/bin/env python
from brain_games import main_logic as ml
from brain_games.games import calc


def main():
    ml.lets_play(calc)


if __name__ == "__main__":
    main()
