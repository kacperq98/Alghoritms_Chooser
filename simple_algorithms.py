import matplotlib.pyplot as plt
from time import sleep as sp
from tryagain import ask

""" FizzBuzz Algorithm"""


def fizz_buzz():
    lowerRange = int(input("Type the lower boundry of the range: "))
    upperRange = int(input("Type the upper boundry of the range: "))
    print()

    for i in range(lowerRange, upperRange+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    print()
    return True


"""Check if is an anagram"""


def is_anagram():
    word1 = input("Type first word: ")
    word2 = input("Type second word: ")

    word1 = word1.lower().strip()
    word2 = word2.lower().strip()

    if sorted(word1) == sorted(word2):
        return print(f"{word2.capitalize()} is an anagram of {word1}.\n")
    else:
        return print(f"{word2.capitalize()} is not an anagram of {word1}.\n")


"""Check if is a palindrome"""


def palindrome():
    while True:

        word = input("Type a word you would check: ")
        word = word.lower()
        if word[::-1] == word:
            return print(f"This word ({word}) is a palindrome.")
        else:
            return print(f"This word {word}) is not a palindrome.")


"""A countdown function"""


def rec(n):
    print(n)
    sp(1)
    n -= 1
    if n == -1:
        # print('0')
        return print('END!')
    return rec(n)


"""A seek a number in indicated range"""


def sequential_seek():
    while True:

        borders = input(
            "Enter the lower and upper limits, separating them with a dash:")
        print()
        borders = borders.split("-")

        if len(borders) != 2:
            print("Inavlid inputs. Try again.")

        else:
            lowerBorder = int(borders[0])
            upperBorder = int(borders[1])

        if lowerBorder >= upperBorder:
            print("Inavlid inputs. Try again.")

        else:
            break
    n = int(input("Type the number to found in range:"))
    print()
    found = False

    for i in range(lowerBorder, upperBorder):
        if i == n:
            found = True
            break

    if found:
        print(f"Found {n} in the indicated range.")
        return found
    else:
        print(f"Didn't found {n} in the indicated range.")
        return found


""" An alghoritm to check a amount of letters, digits and special signs in string"""


def count_char():
    while True:
        # Input a string and create an empty lists for signs
        phrase = input("Enter a string: ")
        print()
        # Delete a blank space from string
        phrase = phrase.replace(" ", "")
        listOfChars = []
        listOfNums = []
        listOfSpecialSigns = []
        countDict = {}                          # Dictionary for counted characters

        for sign in phrase:                     # Create sorting a list of characters and add them to the list
            if sign.isdigit():
                listOfNums.append(sign)
            elif sign.isalpha():
                listOfChars.append(sign)
            else:
                listOfSpecialSigns.append(sign)

        listOfNums = sorted(listOfNums)
        listOfChars = sorted(listOfChars)
        listOfChars = listOfChars+listOfNums + \
            listOfSpecialSigns     # Join all list of signs

        for char in listOfChars:
            if char in countDict:
                countDict[char] += 1
            else:
                countDict[char] = 1
        i = 0
        for key, value in countDict.items():
            if i < len(countDict) - 1:
                print(f"{key}:{value},", end=" ")
            else:
                print(f"{key}:{value}.")
            i += 1

        plotChoice = input("Wolud you like to plot a chart ? (Y/N): ")
        if plotChoice.upper() == "Y":
            plotChart(countDict)
        return True


def plotChart(countDict):  # draw a plot wuth use a matplotlib library
    x = countDict.keys()
    y = countDict.values()

    plt.plot(x, y)
    plt.grid(True)
    plt.xlabel("Signs")
    plt.ylabel("Amout")
    plt.title("Amout of signs")
    plt.show()
