from simple_algorithms import *
from tryagain import ask

import shutil
import sys

""" It is a program that connect all my alghoritms together and you choose what you wolud like to use"""

columns = shutil.get_terminal_size().columns  # Display title
for i in range(5):
    if i == 0 or i == 4:
        print()
    elif i == 2:
        print("* Alghoritm Chooser *".center(columns))
    else:
        print('**********************'.center(columns))


while True:                                                # Menu to choose alghoritm
    choose = int(input(
        """What would you like to check:\n
0 - Type if you want to quit,
1 - Char Counter,
2 - Fizzbuzz,
3 - Is Anagram,
4 - Is Palindrome,
5 - Reccuretion Countdown,
6 - Sequential Seek\n
Type a number from 0 to 6: """))
    print()

    match choose:
        case 0:
            print("\nGoodbye\n")
            sys.exit()
        case 1:
            while True:
                count_char()
                if ask():
                    break

        case 2:
            while True:
                fizz_buzz()
                if ask():
                    break

        case 3:
            while True:
                is_anagram()
                if ask():
                    break

        case 4:
            while True:
                palindrome()
                if ask():
                    break

        case 5:
            while True:
                n = int(
                    input('Type a amout of time in seconds what you want to do countdown: '))
                rec(n)
                if ask():
                    break

        case 6:
            while True:
                sequential_seek()
                if ask():
                    break

        case other:
            print("\nIncorrect value! Try again.\n")
