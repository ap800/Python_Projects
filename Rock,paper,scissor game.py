#Rock,paper and scissors in Python
 
import random
while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock,paper,scissors?: ").lower()

    if player==computer:
        print("Computer: ",computer)
        print("Player",player)
        print("It's a tie!!!")
    elif player=="rock":
        if computer=="paper":
            print("Computer: ",computer)
            print("Player",player)
            print("You lose!!!")
        if computer=="scissors":
            print("Computer: ",computer)
            print("Player",player)
            print("You win!!!")
    elif player=="scissors":
        if computer=="rock":
            print("Computer: ",computer)
            print("Player",player)
            print("You lose!!!")
        if computer=="paper":
            print("Computer: ",computer)
            print("Player",player)
            print("You win!!!")
    elif player=="paper":
        if computer=="scissors":
            print("Computer: ",computer)
            print("Player",player)
            print("You lose!!!")
        if computer=="rock":
            print("Computer: ",computer)
            print("Player",player)
            print("You win!!!")
    
    play_again = input("Would you like to play again??? (yes/no): ").lower()
    if play_again!="yes":
        break

print("Thank you for playing the game!!!")