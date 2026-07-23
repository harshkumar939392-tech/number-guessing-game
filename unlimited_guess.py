import random
secret_number= random.randint(1,100)
attempts = 0 

print("================== number guessing game ===============================")
print("guess the number between 1 to 100")

while True:
    guess= int(input("enter your number: "))
    attempts +=1
    if guess==secret_number:
        print("you guessed the right number ")
        print(f"you guessed in {attempts} attempts")
        break
    
    elif guess>secret_number:
        if guess-secret_number<=10:
                    print("low")
        else:
                     print("too low")
    else :
        if  secret_number-guess<=10:
                print("high") 
        else:
                 print("too high")  
   
print(f"the correct number was {secret_number}")   
print("thanks for playing")              
             