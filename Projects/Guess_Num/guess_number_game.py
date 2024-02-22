'''this is game where gamer try guess secret number'''

import random

# this function check input value(must be integer)
def input_only_number():
    while True:
        gamer_choice = input("Enter your guess: ")
        print()
        try:
            guess = int(gamer_choice)
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.\n")
        except ValueError:
            print("Allowed only integer number.")
            print("Please enter a valid number between 1 and 100.\n")


def game():
    # now we generate random number from 1 to 100
    secret_number = random.randint(1, 100)
    
    # count attempts
    count_attempts = 0

    print()
    print("Welcome to Game!")
    print("Try guess number from 1 to 100\n")
    
    while True:
        # Get the player's guess with input validation
        guess = input_only_number()
        
        # Increment the attempts
        count_attempts += 1
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"YESSS! You do it this in {count_attempts} attempts.\n")
            break
        elif guess < secret_number:
            print("Too low! Try again.\n")
        else:
            print("Too high! Try again.\n")


#==========>RUN GAME<==============
game()
