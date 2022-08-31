# imports random so we can play the game.
import random

# creates a loop for the game.
while True:
    # creates a list so the only numbers that can show up are from 1-10.
    list_rand = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # gets a random number out of the list
    random_number = random.choice(list_rand)
    # gets the user's guess for the game
    choice = int(input("Type a number between 1-10 inclusive: "))
    # checks if the guess matches the randomly generated number
    if choice < 1 or choice > 10:
        print("Invalid input.")
    elif (choice == random_number):
        print("You win")
    else:
        print("The number was:", random_number, "and you picked", choice)
    # gets user input. Continue or stop playing?
    play = int(input("Would you like to play again? 1 - YES, 2 - NO: "))
    # checks the user input and breaks/continues
    if play == 2:
        break
    else:
        continue

#test