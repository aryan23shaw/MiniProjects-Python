import random

def roll_dice():
    return random.randint(1, 6)

print("Simulating dice rolls:")
for _ in range(5):
    print(f"Dice roll: {roll_dice()}")
