import random
def randDirection():
    r = random.randrange(0,3)
    dr = "North"
    if r == 0:
        dr = "South"
    if r == 1:
        dr = "West"
    if r == 2:
        dr = "East"
    return dr

def rollDice():
    if random.randrange(0,5):
        return True
    else:
        return False

def coinFlip():
    if random.randrange(0,1):
        return True
    else:
        return False