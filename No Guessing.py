import random
t=random.randint(0,100)
while True:
    uc=input("Guess the number or Q for quitting : ")
    if uc=='Q':
        break
    uc=int(uc)
    if (uc==t):
        print("Correct guess")
        break
    elif (uc<t):
        print("try a larger no")
    else:
        print("try a smaller no")
