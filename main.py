from preroll import *
from actions import *

clear()

game = True

first_cycle = True
changeStatusState()

while not Status["GameOver"]:
    if first_cycle:
        print("### Welcome to The Expandable Universe. ###\n")
        first_cycle = False
    else:
       
        if Settings["clear"]:
            clear()
        else:
            print("\n\n")
        actions.setdefault(inp,error)()
        changeStatusState()
        if(Status["GameOver"]):
            break
    pre_display()
    inp = input().lower()

printWarn("Game Over.\n"
      "Thank you for playing."
    )

