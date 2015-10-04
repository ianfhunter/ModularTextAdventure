from status import *
from printing import *
from provider import *

def gather_bushes():
    printBold("ACTION: ","")
    print("You rummage around and find some berries")
    printOKGreen("FOOD +1")

    Status["Food"]+=1

def gather_wood():
    printBold("ACTION: ","")
    print("It is easy to pick up the debris around the opening, but the quality is poor and of little use.")
    printOKGreen("WOOD +0.5")

    Status["Wood"]+=0.5

def remain():
    if Status["Stage"] == 0:
        printBold("ACTION: ","")
        print("You decide to turn over and the small glimpse of evolution recedes,\n"
              "waiting another hundred thousand years to try again.")
        Status["GameOver"] = True
    else:
        error()

def explore():
    if Status["Stage"] == 0:
        printBold("ACTION: ","")
        if rollDice():
            print("You wander " + randDirection() + "wards for a while and discover a clearing in the woods\n"\
                "made so by some enormous beast that has toppled several trees")
            Status["Stage"] = 1
        else:
            print("You wander " + randDirection() + "wards for a while but discover nothing of note\n"\
                  "There are some strange tracks in the ground, but you find it hard to follow.")
        printFail("FOOD -2")
        Status["Food"]-=2

    else:
        error()

def inspect_deer():
    printBold("ACTION: ","")
    print("You clambor over to the freshly killed carcass of a deer.\n"
          "The smell of fresh blood lingers in the air.\n"
          "The deer lies upon a mound of stones, which glisten red in the sun.")
    Status["Stage"] = 2