import random  # Import the 'random' module for generating random numbers

def guessingGame():
    """Runs a simple guessing game where the user guesses a number between 1 and 100."""
    
    # Print a welcome message
    print("Welcome to the Guessing Game!")

    # Print information about the range of numbers
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100 and store it in the variable 'secretNumber'
    secretNumber = random.randint(1, 100)

    # Initialize a variable 'attemptsCount' to keep track of the number of guesses
    attemptsCount = 0

    # Start an infinite loop to repeatedly ask the user for guesses
    while True:  # Infinite loop until the correct guess
        # Get user input and convert it to an integer
        guess = int(input("Your guess: "))
        
        # Increment the 'attemptsCount' variable
        attemptsCount += 1

        # Compare the user's guess with the secret number
        if guess < secretNumber:
            # If the guess is too low, print a message and continue the loop
            print("Too low! Try again.")
        elif guess > secretNumber:
            # If the guess is too high, print a message and continue the loop
            print("Too high! Try again.")
        else:
            # If the guess is correct, print a congratulatory message and the number of attempts
            print(f"Congratulations! You guessed the correct number in {attemptsCount} attempts.")
            # Exit the loop, ending the game
            break

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the 'guessingGame' function if the script is run
    guessingGame()
