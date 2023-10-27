print("Welcome to the number guessing game")

import random
random_number = random.randint(0, 1000)
n_g = 0

while True:

    guesses_number = int(input("please enter number between 0 to 1000:"))
    n_g+=1

    if guesses_number < random_number:
        print("Please enter a larger number")
    if guesses_number > random_number:
        print("Please enter a smaller number")
    if guesses_number == random_number:
        print("You guessed the number correctly")
        break
print(random_number)
print("The number of your guesses", n_g)
