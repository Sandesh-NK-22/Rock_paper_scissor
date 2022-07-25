import random

def game():
    player=input("r for 'rock', s for 'scissor', p for 'paper' Whats your choice? ")

    computer = random.choice(['r', 'p', 's'])

    print("Computers choice - ",computer)

    if player == computer:
        print("Its a Tie!!")

    if winner(player,computer):
        print("You Won!!!")
    else:
        print("You Loose!!")

def winner(user,opponent):
    if(user == 'r' and opponent == 's') or (user == 'p' and opponent == 'r') or (user == 's' and opponent == 'p'):
        return True
game()