# python project 1 to play dimond paper scissors with computer


import random

computer = random.choice([-1, 0, 1])
youstr = input("enter your choice ")
youDict = {"d": 1, "p": -1, "s": 0,}
reverseDict = {1: "dimond", -1: "paper", 0: "scissors",}
you = youDict[youstr]

# by now we have

print(f"you chose {reverseDict[you]})\ncomputer chose {reverseDict[you]}")

if(computer == you):
     print("its a draw")
else :
    if(computer == 1 and you ==1):
        print("you win!")
        
    elif(computer == -1 and you ==0):
        print("you Lose!")
    
    elif(computer == -1 and you ==-1):
        print("you Lose!")
        
    elif(computer == 1 and you ==0):
        print("you win!")
    
    elif(computer == 0 and you ==-1):
        print("you win!")
    
    elif(computer == 0 and you ==1):
        print("you Lose!")
    
    elif(computer == -1 and you ==0):
        print("something went wrong!")