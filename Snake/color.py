class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printcol(text,color):
    if color == "purple":
        return print(bcolors.OKBLUE + text + bcolors.ENDC,end = " ")
    elif color == "yellow":
        return print(bcolors.WARNING + text + bcolors.ENDC,end = " ")
    elif color == "cyan":
        return print(bcolors.OKCYAN + text + bcolors.ENDC,end = " ")
    elif color == "green":
        return print(bcolors.OKGREEN + text + bcolors.ENDC,end = " ")


