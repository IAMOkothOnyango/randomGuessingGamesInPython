import random
import math

# Requesting user input for the lower bound of the number range
lowerBound = int(input("Enter Lower bound:- "))

# Requesting user input for the upper bound of the number range
upperBound = int(input("Enter Upper bound:- "))

# Generating a random number within the specified range
secretNumber = random.randint(lowerBound, upperBound)

# Informing the user about the number of attempts they have based on the range
print("\n\tYou have only ", 
      round(math.log(upperBound - lowerBound + 1, 2)),
      " chances to guess the integer!\n")

# Initializing the counter for the number of guesses
guessCount = 0

# Loop for user guesses, limited by the calculated number of chances
while guessCount < math.log(upperBound - lowerBound + 1, 2):
    guessCount += 1

    # Taking the user's guess as input
    userGuess = int(input("Guess a number:- "))

    # Checking conditions based on the user's guess
    if secretNumber == userGuess:
        print("Congratulations! You guessed it in ", guessCount, " tries.")
        # Exiting the loop once the correct guess is made
        break
    elif secretNumber > userGuess:
        print("You guessed too small!")
    elif secretNumber < userGuess:
        print("You guessed too high!")

# Displaying a message if the user couldn't guess within the allowed attempts
if guessCount >= math.log(upperBound - lowerBound + 1, 2):
    print("\nThe number was %d" % secretNumber)
    print("\tBetter Luck Next time!")

# End of the game message
print("Good gaming!")
