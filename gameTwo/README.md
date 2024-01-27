# Custom Range Guessing Game

The **Custom Range Guessing Game** is a Python script that allows users to play a guessing game within a specified range. The user is prompted to input the lower and upper bounds of the number range, and the script generates a random number within that range. The game then provides feedback to the user after each guess, indicating whether the guess is too high, too low, or correct. The number of attempts allowed is calculated based on the range.

## Features

- **Custom Range:** Users can define the lower and upper bounds of the number range.
- **Random Number Generation:** The script generates a random number within the user-defined range using the `random` module.
- **Attempt Calculation:** The number of attempts allowed is calculated based on the range using logarithmic functions.
- **User Interaction:** The user is prompted to input their guesses, and the program provides feedback on each guess.
- **Game Outcome:** The script congratulates the user upon a correct guess or provides a message if the user couldn't guess within the allowed attempts.

## Usage

1. **Run the Program:**
   - Execute the Python script:
     ```bash
     python randomGuessingGame02.py
     ```

2. **Set the Number Range:**
   - Enter the lower and upper bounds when prompted.
   - The script will generate a random number within the specified range.

3. **Guess a Number:**
   - Enter your guess when prompted after the program displays "Guess a number."
   - Receive feedback on whether the guess is too high, too low, or correct.

4. **Winning the Game:**
   - Continue guessing until you correctly guess the secret number.
   - Upon a correct guess, the script will display a congratulatory message and the number of attempts.

5. **Exiting the Game:**
   - The game will automatically exit after the correct guess or after the allowed number of attempts.

## Sample Execution

Here's a sample execution of the game:

```
Enter Lower bound:- 1
Enter Upper bound:- 100

    You have only  7  chances to guess the integer!

Guess a number:- 50
You guessed too small!
Guess a number:- 75
You guessed too high!
Guess a number:- 62
You guessed too small!
Guess a number:- 68
Congratulations! You guessed it in  4  tries.
Good gaming!
```

Feel free to explore and modify the script to suit your preferences. If you encounter any issues or have suggestions for improvement, please refer to the feedback messages or check the source code for guidance.
