# Guessing Game

The **Guessing Game** is a simple Python script that implements a guessing game where the user tries to guess a randomly generated number between 1 and 100. The game provides feedback to the user after each guess, indicating whether the guess is too high, too low, or correct. The game continues until the user correctly guesses the secret number.

## Features

- **Random Number Generation:** The game generates a random number between 1 and 100 using the `random` module.
- **User Interaction:** The user is prompted to input their guesses, and the program provides feedback on each guess.
- **Attempt Tracking:** The script keeps track of the number of attempts the user makes before guessing the correct number.
- **Congratulations Message:** Upon a correct guess, the script congratulates the user and displays the number of attempts.

## Usage

1. **Run the Program:**
   - Execute the Python script:
     ```bash
     python randomGuessingGame01.py
     ```

2. **Guess a Number:**
   - Enter your guess when prompted after the program displays "Your guess."
   - Receive feedback on whether the guess is too high, too low, or correct.

3. **Winning the Game:**
   - Continue guessing until you correctly guess the secret number.
   - Upon a correct guess, the script will display a congratulatory message and the number of attempts.

4. **Exiting the Game:**
   - The game will automatically exit after the correct guess.

## Sample Execution

Here's a sample execution of the game:

```
Welcome to the Guessing Game!
I'm thinking of a number between 1 and 100.
Your guess: 50
Too low! Try again.
Your guess: 75
Too high! Try again.
Your guess: 62
Too low! Try again.
Your guess: 68
Too high! Try again.
Your guess: 65
Congratulations! You guessed the correct number in 5 attempts.
```

Feel free to explore and modify the script to suit your preferences. If you encounter any issues or have suggestions for improvement, please refer to the feedback messages or check the source code for guidance.
