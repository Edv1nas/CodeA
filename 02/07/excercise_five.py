# create a number guessing game from 1-10, with random library. (IDEA FOR LATER MAYBE)

import random


random_number = random.randint(1, 10)

guess_number = int(input("Please guess number: "))

if guess_number == random_number:
    print(f"Congrats, you guessed random number! random number is {random_number}.")

else:
    print(f"Congrats, you are wrong, good luck next time, random number is {random_number}.")