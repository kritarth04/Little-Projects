import random as rd

print(" Rock  Paper  Scissor".center(140))

def win(comp,user):
    if comp == user:
        print(" It is a draw match !!")
    elif comp == 0 and user == 1:
        print(" You Won !! ")
    elif comp == 1 and user == 2:
        print(" You Won !! ")
    elif comp == 2 and user == 0:
        print("You Won !! ")
    elif user == 3:
        return 0
    else:
        print("Your Lose !! ")

i = int(input("How many rounds do you wanna play ! "))
while (i > 0):

    user = int(input("What do you choose !! 0 -- Stone  1 -- Paper 2 -- Scissor \n "))
    comp = rd.randint(0,2)

    print("Computer took ", comp)
    print(f"You took {user} ")
    win(comp,user)
    i -= 1
    
    

