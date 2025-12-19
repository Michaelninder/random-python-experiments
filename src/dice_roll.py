import random

APP_title = """██████╗░██╗░█████╗░███████╗  ██████╗░░█████╗░██╗░░░░░██╗░░░░░
██╔══██╗██║██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██║░░░░░██║░░░░░
██║░░██║██║██║░░╚═╝█████╗░░  ██████╔╝██║░░██║██║░░░░░██║░░░░░
██║░░██║██║██║░░██╗██╔══╝░░  ██╔══██╗██║░░██║██║░░░░░██║░░░░░
██████╔╝██║╚█████╔╝███████╗  ██║░░██║╚█████╔╝███████╗███████╗
╚═════╝░╚═╝░╚════╝░╚══════╝  ╚═╝░░╚═╝░╚════╝░╚══════╝╚══════╝\n"""

options = range(1, 7)

rolls = []

def roll(unused):
    roll = random.choice(options)
    rolls.append(roll)
    return roll

def getAverage(list):
    total = 0
    #for item in list:
    #    total += item
    for num in list:
        total += int(num)
    return total / len(list)

#for option in options:
#    print(option)

print(APP_title)


while True:
    print(f"Dice rolled to: {roll(input("Press enter to roll the dice!"))}\nAverage roll is now {getAverage(rolls)}")