import random
import time


def gameWin(comp, you):
    if comp == you:
        return None

    elif comp == 'paper':
        if you == 'rock':
            return False
        elif you == 'scissors':
            return True

    elif comp == 'rock':
        if you == 'scissors':
            return False
        elif you == 'paper':
            return True

    elif comp == 'scissors':
        if you == 'paper':
            return False
        elif you == 'rock':
            return True

time.sleep(1)
print("-----------------------------------------")
print("The computer has chosen.")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'paper'
elif randNo == 2:
    comp = 'rock'
elif randNo == 3:
    comp = 'scissors'

time.sleep(1)
print("-----------------------------------------")
you = input("Your Turn: Rock, Paper, or Scissors? ").lower()
a = gameWin(comp, you)

time.sleep(1)
print("-----------------------------------------")
print(f"Computer chose {comp}")
print(f"You chose {you}")
print("-----------------------------------------")

if a == None:
    time.sleep(1)
    print("The game is a tie!")
    print("-----------------------------------------")
elif a:
    time.sleep(1)
    print("You Win!")
    print("-----------------------------------------")
else:
    time.sleep(1)
    print("You Lose!")
    print("-----------------------------------------")
