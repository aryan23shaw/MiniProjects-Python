import random

def roll_two_dice():
    return random.randint(1, 6), random.randint(1, 6)

dice1, dice2 = roll_two_dice()
print(f"Dice 1: {dice1}, Dice 2: {dice2}")
