import random

number = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Guess a number (1-10): "))
    
    if guess == number:
        print("Correct! You guessed it.")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")
    
    attempts -= 1

if guess != number:
    print("Out of attempts! The number was", number)
