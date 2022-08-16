from simple_algorithms import *
from tryagain import run, ask

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

    match choose:
        case 0:
            print("\nGoodbye\n")
            sys.exit()
        case 1:
            run(fizz_buzz(), ask())

        case 2:
            run(count_char(), ask())

        case 3:
            run(is_anagram(), ask())

        case 4:
            run(palindrome(), ask())

        case 5:
            n = int(
                input('Type a amout of time in seconds what you want to do countdown: '))
            run(rec(n), ask())

        case 6:
            run(sequential_seek, ask())

        case other:
            print("\nIncorrect value! Try again.\n")
