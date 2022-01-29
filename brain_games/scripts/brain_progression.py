#!/usr/bin/env python
from brain_games import main_logic as ml


def main():
    user_name = ml.welcome_message()
    print('What number is missing in the progression?')
    ml.start_game("progression", user_name)


if __name__ == "__main__":
    main()
