#!/usr/bin/env python
from brain_games import main_logic as ml
from brain_games.games import gcd


def main():
    ml.lets_play(gcd)


if __name__ == "__main__":
    main()
