import random
import sys


secret_number= random.randint(1,100)
print("================== number guessing game ===============================")
print("guess the number between 1 to 100")
print("you have 3 attempt \n")
guess1=int(input("enter you number: "))
if guess1==secret_number:
    print("congratulation, you guessed the right number")
    sys.exit()
else:
    if guess1>secret_number:
        if guess1-secret_number<=10:
            print("low")
        else:
             print("too low")
    else:
        if secret_number-guess1<=10:
            print("high") 
        else:
             print("too high")  
guess2=int(input("enter you number: "))
if guess2==secret_number:
    print("congratulation, you guessed the right number")
    sys.exit()
else:
    if guess2>secret_number:
        if guess2-secret_number<=10:
            print("low")
        else:
             print("too low")
    else:
        if secret_number-guess2<=10:
            print("high") 
        else:
             print("too high")  
guess3=int(input("enter you number: "))
if guess3==secret_number:
    print("congratulation, you guessed the right number")
    sys.exit()
else:
    if guess3>secret_number:
        if guess3-secret_number<=10:
            print("low")
        else:
             print("too low")
    else:
        if secret_number-guess3<=10:
            print("high") 
        else:
             print("too high")              
print("the game is over")    
print(f"the the gueesed number is : {secret_number}")         