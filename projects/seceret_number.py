



import random


secret = random.randint(1, 100)
print("Secret number is:", secret)

guess = input("Enter a number between 1 and 100 (or 'q' to quit):")
print("You typed: ", guess)


# try:
#     number = int(guess)
#     print("Converted to number: ", number)
# except ValueError:
#     print("That was not a valid number!")
    
# # if number < secret:
#     print("Too Low!")
# elif number > secret:
#     print("Too high!")
# else:
#     print("Correct!")
    
attempts = 0

# attempts += 1
# print("Number of attempts so far: ", attempts)


while True:
    guess = input("Enter a number between 1 and 100 (or 'q' to quit)")
    
    if guess == "q":
        print("You gave up! The secret was:", secret)
        break
    
    try:
        number = int(guess)
        attempts += 1
        
        if number < secret:
            print("Too low!")
        elif number > secret:
            print("Too high!")
        else:
            print("Correct! You guessed it in", attempts, "attempts.")
            break
    except ValueError:
        print("Please enter a valid whole number!")