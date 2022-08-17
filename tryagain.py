def ask():
    again = input("Would you like to try again? (Y/N): ")
    print()
    if again.upper() == "Y" or again.upper() == "N":
        if again.upper() == "N":
            print("\nGoodbye\n")
            return True
        return False
    else:
        print("Incorrect value!")
        return ask()
