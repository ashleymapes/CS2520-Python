'''
Ashley Mapes
Lab 2
This program will play rock paper scissors with the user and state the winner

'''
import random

print("Welcome to rock paper scissors!\n")

# run program until user ends it
while True:
    # validate user input
    while True:
        userChoice = input("Please enter your play! ('rock', 'paper', 'scissors'): ").lower()
        if userChoice == "rock" or userChoice == "paper" or userChoice == "scissors":
            break
        else:
            print("Invalid response, please try again.\n")
    
    # randomly assign computers choice
    compChoice = random.choice(["rock", "paper", "scissors"])
    print("beeboop beeboop, computer chooses.... ", compChoice)
    print()
    
    # case of tie
    if userChoice == compChoice:
        print("Tie!")
    
    else:
        match userChoice:
            # user is rock
            case "rock":
                if compChoice == "paper":
                    print("You lose")
                elif compChoice == "scissors":
                    print("You win!")
            # user is paper
            case "paper":
                if compChoice == "rock":
                    print("You win!")
                elif compChoice == "scissors":
                    print("You lose")
            # user is scissors
            case "scissors":
                if compChoice == "rock":
                    print("You lose")
                elif compChoice == "paper":
                    print("You win!")
            # if all else fails
            case _:
                print("something went wrong...")
    
    # ask the user to play again and validate input
    while True:
        playAgain = input("Would you like to play again? (yes/no) ").lower()
        if playAgain == "yes" or playAgain == "no":
            break
        else:
            print("Invalid response, please try again.\n")
    
    # break if user does not want to play
    if playAgain == "no":
        break

print("Program is done.")

'''
TESTING:
(losing case)
Welcome to rock paper scissors!

Please enter your play! ('rock', 'paper', 'scissors'): paper
beeboop beeboop, computer chooses....  scissors

You lose
Would you like to play again? (yes/no) no
Program is done.

(tie)
Welcome to rock paper scissors!

Please enter your play! ('rock', 'paper', 'scissors'): paper
beeboop beeboop, computer chooses....  paper

Tie!
Would you like to play again? (yes/no) no
Program is done.

(winning case)
Welcome to rock paper scissors!

Please enter your play! ('rock', 'paper', 'scissors'): scissors
beeboop beeboop, computer chooses....  paper

You win!
Would you like to play again? (yes/no) no
Program is done.
'''