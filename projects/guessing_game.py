# guessing_game.py

import random

print("Welcome to the Number Guessing Game!")
player_name = input("Enter your name: ")

# Generate a random number between 1 and 50
number_to_guess = random.randint(1, 50)
attempts = 0

while True:
    guess = int(input("Guess the number (1-50): "))
    attempts += 1
    
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print(f"Congratulations {player_name}! You guessed it in {attempts} attempts.")
        break
