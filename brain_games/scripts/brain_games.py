#!/usr/bin/env python
from brain_games import cli
from brain_games.scripts import main_logic as ml


def main():
    print('Welcome to the Brain Games!')
    print("!", __name__)
    print(ml.GAME_ROUND)
    cli.welcome_user()


if __name__ == "__main__":
    main()
