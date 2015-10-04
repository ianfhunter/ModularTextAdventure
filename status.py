import os
from printing import *

Status = {
    "Details":  "N/A",
    "Prompt": "N/A",
    "Health": 100,
    "Food": 0,
    "Wood": 0,
    "GameOver": False,
    "Stage":0
}

Settings = {
    "clear": True,
}

#Settings Functions
def error():
    print("This command is not available.")

def clear():
#    os.system('cls')
    os.system('clear')

def autoclear():
    Settings["clear"] = True


#Game Story
def changeStatusState():
    if Status["Stage"] == 0 and Status["Food"] < 5:
        Status["Details"] = "As you idly sit in a large oak tree, your musings take a deeper turn.\n"\
                "Suddenly the world becomes more than just a given background.\n"\
                "It becomes a question - Why am I here? What is this earth? Was it always here?\n"\
                "Your brain begins to hurts and you need to eat. There are some fruit bushes nearby. \n"
        Status["Prompt"] = "Possible Actions: (bushes) (remain)"

    if Status["Stage"] == 0 and Status["Food"] > 5:
        Status["Details"] = "You grow sick of fruit, and the repeated monotony of the gathering\n"\
                            "'Surely, there must be more to this world' you muse.\n"\
                            "You decide to leave your perch and see if you can discover something more interesting.\n"
        Status["Prompt"] = "Possible Actions: (bushes) (explore)"

    elif Status["Stage"] == 1:
        Status["Details"] = "The carnage the beast has made is immense. Wood is strewn everywhere.\n"\
                            "A deer carcass lies nearby in a pool of maroon\n"\
                            "From what you can tell, the beast is long gone - but you make a note to be prepared to retreat anyway.\n"
        Status["Prompt"] = "Possible Actions: (bushes) (wood) (deer)"

    elif Status["Stage"] == 2:
        Status["Details"] = "The carnage the beast has made is immense. Wood is strewn everywhere.\n"\
                            "A deer carcass lies nearby on a pile of glistening red rocks.\n"\
                            "From what you can tell, the beast is long gone - but you make a note to be prepared to retreat anyway.\n"
        Status["Prompt"] = "Possible Actions: (bushes) (wood) (deer) (skin_deer)"


#GENERAL INFO
    if not Status["GameOver"]:
        if Status["Food"] < 5:
            printFail("Your stomach rumbles as you grow hungry")
        if Status["Food"] < 0:
            printFail("You collapse with hunger")