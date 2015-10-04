class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printWarn(msg,end="\n"):
    print(bcolors.WARNING + msg + bcolors.ENDC, end=end)

def printOKBlue(msg,end="\n"):
    print(bcolors.OKBLUE + msg + bcolors.ENDC, end=end)

def printOKGreen(msg,end="\n"):
    print(bcolors.OKGREEN + msg + bcolors.ENDC, end=end)

def printFail(msg,end="\n"):
    print(bcolors.FAIL + msg + bcolors.ENDC, end=end)

def printBold(msg,end="\n"):
    print(bcolors.BOLD + msg + bcolors.ENDC, end=end)

def printUnderline(msg,end="\n"):
    print(bcolors.UNDERLINE + msg + bcolors.ENDC, end=end)



