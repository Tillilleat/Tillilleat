# Stone Paper Scissors
import random

'''O = stone, P = paper, X = scissors'''

def gameWin(cmp,play):
    if cmp == play:
        return None
    elif cmp == 'o':
        if play == 'x':
            return False
        elif play == 'p':
            return True
    elif cmp == 'x':
        if play == 'p':
            return False
        elif play == 'o':
            return True
    elif cmp == 'p':
        if play == 'o':
            return False
        elif play == 'x':
            return True

print("Computer's Turn : Stone(o), Paper(p), Scissors(x)..!")
rand = random.randint(1,3)
if rand == 1:
    cmp = 'o'
elif rand == 2:
    cmp = 'x'
elif rand == 3:
    cmp = 'p'

play = input("Your turn : Stone(o), Paper(p), Scissors(x)..!  ")
s = gameWin(cmp,play)

print(f"Computer chose : {cmp}")
print(f"You chose : {play}")

if s == None:
    print("the game was tie.! (*_*!) ")
elif s:
    print("You Won..!!")
else:
    print("You Lose.! better luck next time.! XD")
print("______________________________________________________________________")