from status import *

def pre_display():
    display_stats()
    display_description()
    display_prompt()

def display_stats():
    print("===Status===")
    ShowStat("Health")
    ShowStat("Food")
    ShowStat("Wood")
    print("============\n")


def display_description():
    print(Status["Details"])

def display_prompt():
    print(Status["Prompt"])

def ShowStat(item):
    if Status[item] != 0:
        print(item,": ",Status[item])