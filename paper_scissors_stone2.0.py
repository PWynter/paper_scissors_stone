"""Paper,scissors,stone game.player selects an option,computer option is random """

# import random and the randint function to generate random numbers
from random import randint

# assign player an user input
player = input("rock (r), paper (p) or scissor (s)? ")

# print the user input, end tells python to end with a space not new line
print(player, "vs ", end="")

# selects random num from range
chosen = randint(1, 3)
# print(chosen)

# uses chosen variable and assigns computer a letter
if chosen == 1:
    computer = "r"
elif chosen == 2:
    computer = "p"
else:
    computer = "s"

# prints random letter thats been assigned to computer from using randint
print (computer)

# who wins
if player == computer:
    print("Draw")
elif player == "r" and computer == "s":
    print("Player wins!")
elif player == "r" and computer == "p":
    print("Computer wins!")

# who wins
elif player == "p" and computer == "r":
    print("Player wins!")
elif player == "p" and computer == "s":
    print("Computer wins!")

# who wins
elif player == "s" and computer == "r":
    print("Computer wins!")
elif player == "s" and computer == "p":
    print("Player wins!")
