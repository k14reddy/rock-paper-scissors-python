import random

youDict = {"r":1 , "p":0 , "s":-1}
Dict = {1:"Rock" , 0:"Paper" , -1:"Scissor"}
youstr = input("Enter your choice(r,p,s): ").lower()

if youstr not in youDict :
    print("Invalid input! Please enter 'r', 'p', or 's'.")
else :

    Computer = random.choice([1 , 0 , -1])
    you = youDict[youstr]

    print(f"Your choice : {Dict[you]}")
    print(f"Computer choice : {Dict[Computer]}")

    if Computer == you :
        print("Draw")

    else:
        if (Computer - you) % 3 == 1 :
            print("You Won!")
        else:
            print("You Lost!")
    
