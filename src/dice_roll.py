import random

APP_title = """██████╗░██╗░█████╗░███████╗  ██████╗░░█████╗░██╗░░░░░██╗░░░░░
██╔══██╗██║██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██║░░░░░██║░░░░░
██║░░██║██║██║░░╚═╝█████╗░░  ██████╔╝██║░░██║██║░░░░░██║░░░░░
██║░░██║██║██║░░██╗██╔══╝░░  ██╔══██╗██║░░██║██║░░░░░██║░░░░░
██████╔╝██║╚█████╔╝███████╗  ██║░░██║╚█████╔╝███████╗███████╗
╚═════╝░╚═╝░╚════╝░╚══════╝  ╚═╝░░╚═╝░╚════╝░╚══════╝╚══════╝\n"""

options = range(1, 7)

def roll(unused):
    return random.choice(options)

#for option in options:
#    print(option)

print(APP_title)


while True:
    print(f"Dice rolled to: {roll(input("Press enter to roll the dice!"))}")