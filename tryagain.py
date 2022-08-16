def ask():
    again = input("Would you like to try again? (Y/N): ")
    if again.upper() == "Y" or again.upper() == "N":
        if again.upper() == "N":
            print("\nGoodbye\n")
            return False
        else: 
            return True
    else:
        print("Incorrect value!")
        return ask()
    
def run(function, ask):
    while True:
        function
        if not ask:
            break