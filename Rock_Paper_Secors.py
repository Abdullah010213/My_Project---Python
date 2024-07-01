import random
from enum import Enum
import sys

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("1 for Rock\n2 for Paper\n3 for Scissors")
print("--------------------------------------")

turn = 0

def play_RPS():
    global turn
    your_points = 0
    computer_points = 0
    player_choice = int(input("Choice your mind : "))

    if player_choice < 1 or player_choice > 3:
        print("Involid Choice!!! Try again...")
        return play_RPS()

    computer_choice = random.randint(1,3)
    print("--------------------------------------")

    print(f"you choice {str(RPS(player_choice)).replace('RPS.','').title()}.\ncomputer choice {str(RPS(computer_choice)).replace('RPS.','').title()}.")

    def play_logic(player_choice, computer_choice):
        nonlocal your_points
        if player_choice == computer_choice:
            print("Tie.")
            print("--------------------------------------")
        elif player_choice == 1 and computer_choice == 3:
            print("you win the Luck.")
            print("--------------------------------------")
            your_points+=1
        elif player_choice == 2 and computer_choice == 1:
            print("you win the Luck.")
            print("--------------------------------------")
            your_points+=1
        elif player_choice == 3 and computer_choice == 2:
            print("you win the Luck.")
            print("--------------------------------------")
            your_points+=1
        else:
            print("you loss the Luck.")
            print("--------------------------------------")
            computer_choice+=1
    play_logic(player_choice,computer_choice)

    print("Play again...")
    while True:
        turn+=1
        ask = input("if you want to quit the game, press q otherwise press y\n => ")
        if ask == "q":
            print(f"you play {turn} times in this game")
            print(f"your score : {your_points}")
            print(f"computer score : {computer_points}")
            sys.exit("good play")
        elif ask == "y":
            play_RPS()
        else:
            print("involid choice! must type q or y.")
            continue

play_RPS()
