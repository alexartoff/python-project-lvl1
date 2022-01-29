#!/usr/bin/env python
from brain_games import main_logic as ml


def main():
    user_name = ml.welcome_message()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    ml.start_game("even", user_name)


if __name__ == "__main__":
    main()
