#importing random function
import random

#______global variables______
#taking the number of players that will be playing the game.
number_of_players=int(input("How many players are playing the game?\n"))

#asking the number of dies that will be used in the game
number_of_dies=int(input("How many dies will be rolled in this game?\n"))

#variable to check the number of turns each player got
turns=0

#variable to check if the game is over or not
valid=True

#function to start the game
def play():
    global turns
    global valid
    while valid:
        turns+=1
        flip_player()
        check=input("\nIs the game over? Y/N\n")
        check=check.upper()
        if check=="N" or check=="n":
            pass
        else:
            valid=False
    return

#function to roll the die
def roll():
    temp_number_of_dies=number_of_dies
    while temp_number_of_dies!=0:
        print(random.randint(1,6),end=" ")
        temp_number_of_dies-=1
    return

#function to switch to the next player's turn
def flip_player():
    temp_number_of_players=1
    while temp_number_of_players!=number_of_players+1:
        print(f"\nPlayer {temp_number_of_players}\'s turn:")
        roll()
        temp_number_of_players+=1
    return

#calling the function play() to play the game
play()
print(f"Each player got {turns} number of turns in this game.")