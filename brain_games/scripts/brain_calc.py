#!/usr/bin/env python
from brain_games import main_logic as ml


def main():
    user_name = ml.welcome_message()
    print('What is the result of the expression?')
    ml.start_game("calc", user_name)


if __name__ == "__main__":
    main()
