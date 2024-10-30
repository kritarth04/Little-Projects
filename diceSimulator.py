import random as rn

def check_no(num):
    if num == 1:
        print("+-------+""\n" "|       |""\n" "|   •   |""\n" "|       |""\n" "+-------+")
    if num == 2:
        print("+-------+""\n" "| •     |""\n" "|       |""\n" "|     • |""\n" "+-------+")
    if num == 3:
        print("+-------+""\n" "| •     |""\n" "|   •   |""\n" "|     • |""\n" "+-------+")
    if num == 4:
        print("+-------+""\n" "| •   • |""\n" "|       |""\n" "| •   • |""\n" "+-------+")
    if num == 5:
        print("+-------+""\n" "| •   • |""\n" "|   •   |""\n" "| •   • |""\n" "+-------+")
    if num == 6:
        print("+-------+""\n" "| •   • |""\n" "| •   • |""\n" "| •   • |""\n" "+-------+")

def __main__():
    while True:
        print("Press 'Enter' To Roll Dice")
        input()
        num = rn.randint(1,6)
        check_no(num)
        continue
    else:
        exit()

__main__()

