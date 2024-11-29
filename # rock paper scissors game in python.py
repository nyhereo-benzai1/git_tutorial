# rock paper scissors game in python 
import random 
while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    user = input("rock , paper or scissors?").lower()
    print("you chose = " + user)
    print("computer chose = " + computer ) 
    if (user == computer ):
        print("it's a tie! ")
    elif (user == "rock"):
        if (computer == "paper" ):
            print("computer won!")
        elif(computer == "scissors"):
            print("you won!")
    elif (user == "paper"):
        if (computer == "rock"):
            print("you won!")
        elif(computer == "scissors"):
            print("computer won!")
    elif (user == "scissors"):
        if (computer == "paper"):
            print("you won!")
        elif ( computer == "rock"):
            print(" computer won!")

    
    next_step = input("do you wnat to play again? (yes/no)").lower()
    if (next_step != "yes"):
        break 

    

        


    