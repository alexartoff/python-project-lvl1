#!/usr/bin/env python
from brain_games import main_logic as ml


def main():
    user_name = ml.welcome_message()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    ml.start_game("prime", user_name)


if __name__ == "__main__":
    main()
