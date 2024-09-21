import random
target = random.randint(1,100)

while True:
    userChoice = int(input("Guess the number :"))
   
    if(userChoice == target ):
        print("Sucess: correct Guess!!")
        break
    elif(userChoice < target):
        print("your number is small. Take Bigger number")

    else:
        print("your number is big.Take smaller number ")
        
print("---- GAME OVER ----") 
    
