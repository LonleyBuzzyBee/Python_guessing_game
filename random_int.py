# section 11 guessing game
# handle user guesses
#   if they guess correct, tell them they won
#       otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!

import random
# random_number = random.randint(1,10) # numbers 1 - 10
#
# guess = input("Guess a number between 1 and 10, inclusive: ")

play_again = 'y'

    # guess = int(guess)
while play_again == 'y':
    random_number = random.randint(1,10) # numbers 1 - 10
    guess = input("Guess a number between 1 and 10, inclusive: ")
    while guess != random_number:
        if guess in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                if int(guess) > random_number:
                    state = "Guess lower!"
                    print(state)
                    guess = input("Try again. Guess a number between 1 and 10, inclusive: ")
                elif int(guess) < random_number:
                    state = "Guess higher!"
                    print(state)
                    guess = input("Try again. Guess a number between 1 and 10, inclusive: ")
                else:
                    print(f"Your guess of {guess} is correct")
                    play_again = input("Would you like to play again? (y/n): ")
                    if play_again == 'y':
                        random_number = random.randint(1,10)
                        guess = input("Guess a number between 1 and 10, inclusive: ")
                    else:
                        print("Thanks for playing!")
                        break
        else:
            print("Not an integer or between 1-10, guess again.")
            guess = input("Guess a number between 1 and 10, inclusive: ")
