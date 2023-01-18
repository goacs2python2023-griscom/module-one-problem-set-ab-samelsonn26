import random

def rolldice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print("Die 1 =", die1)
    print("Die 2 =", die2)
    if die1+die2 == 6 or die1+die2 == 7 or die1+die2 == 8:
        print("win")
    else:
        print("lose")

rolldice()