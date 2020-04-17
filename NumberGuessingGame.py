#Number Guessing game. will give hints.
import random
rn = random.randint(1,101)
#Welcome Screen
print("Hi! Welcome to my first game. This is a number guessing game. Guess a number between 1-100 and you will receive hints")

guess = int(input("Enter any whole number from 1 to 100\n"))

while guess != rn:
    print("Wrong you big dummy. Here is a hint.")
    if guess > rn:
        print("Less")
    else:
        print("More than")
    guess = int(input("Enter any whole number from 1 to 100\n"))

if guess == rn:
        print("Congrats you win")








