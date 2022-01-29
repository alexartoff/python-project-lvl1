#!/usr/bin/env python
from brain_games import main_logic as ml


def main():
    user_name = ml.welcome_message()
    print('Find the greatest common divisor of given numbers.')
    ml.start_game("gcd", user_name)


if __name__ == "__main__":
    main()
