import random

options = range(1, 7)

def roll(unused):
    return random.choice(options)

for option in options:
    print(option)

while True:
    print(roll(input("Press enter to roll the dice!")))