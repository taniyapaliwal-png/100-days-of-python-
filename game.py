
import random

print ("welcome to Rock Paper Scissors Game")

choices = ["rock", "paper", "scissors"]

user = input ("Enter rock, paper, or scissors;").lower()
computer = random.choice(choices)

print("Computer;", computer)

#Tie case
if user == computer:
    print("It's a tie!")

# Your winning cases 
elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("Computer wins!")
    
