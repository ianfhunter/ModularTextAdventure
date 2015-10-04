from prehistory import *

actions = {
    #Gathering Functions
    "bushes":gather_bushes,
    "wood":gather_wood,
    
    #Inspect
    "deer":inspect_deer,

    #Upgrade Functions
    "explore":explore,

    #Game Overs
    "remain":remain,

    #System functions
    "clear":clear,
    "error":error,
}
actions.setdefault("NO")