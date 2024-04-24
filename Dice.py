import random

# Define dice faces using ASCII art
dice_faces = [
    ["===========", "|         |", "|    O    |", "|         |", "==========="],
    ["===========", "|         |", "| O     O |", "|         |", "==========="],
    ["===========", "|    O    |", "|    O    |", "|    O    |", "==========="],
    ["===========", "| O     O |", "|         |", "| O     O |", "==========="],
    ["===========", "| O     O |", "|    O    |", "| O     O |", "==========="],
    ["===========", "| O     O |", "| O     O |", "| O     O |", "==========="]
]

print("This is a dice stimulator")

while True:
    # Generate a random number representing the dice face
    number = random.randint(1, 6)
    
    # Print the corresponding dice face using ASCII art
    for line in dice_faces[number - 1]:
        print(line)
    
    # Ask the user if they want to roll again
    x = input("Press y to roll again (or any other key to exit): ")
    if x.lower() != 'y':
        break
