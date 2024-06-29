import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("1 for Rock\n2 for Paper\n3 for Scissors")
print("--------------------------------------")

points = 0
turn = 0

while turn < 3:
    player_choice = int(input("Choice your mind : "))

    if player_choice < 1 or player_choice > 3:
        print("Involid Choice!!!")
        continue

    computer_choice = random.randint(1,3)
    print("--------------------------------------")

    print(f"you choice {str(RPS(player_choice)).replace('RPS.','')}.\ncomputer choice {str(RPS(computer_choice)).replace('RPS.','')}.")

    if player_choice == computer_choice:
        print("Tie.")
        print("--------------------------------------")
        turn += 1
        continue
    elif player_choice == 1 and computer_choice == 3:
        print("you win the Luck.")
        print("--------------------------------------")
        points += 1
        turn += 1
        continue
    elif player_choice == 2 and computer_choice == 1:
        print("you win the Luck.")
        print("--------------------------------------")
        points += 1
        turn += 1
        continue
    elif player_choice == 3 and computer_choice == 2:
        print("you win the Luck.")
        print("--------------------------------------")
        points += 1
        turn += 1
        continue
    else:
        print("you loss the Luck.")
        print("--------------------------------------")
        turn += 1
        continue

if points >= 2:
    print(f"your score is {points} and you win the match.")
else:
    print("you loss the match.")