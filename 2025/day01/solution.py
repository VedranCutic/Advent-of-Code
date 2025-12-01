with open("input.txt", "r") as file:
    rotations = [line.strip() for line in file.readlines()]


# PART 1 #

dial = 50
password = 0

for rotation in rotations:
    if rotation[0] == "L":
        dial = (dial - int(rotation[1:])) % 100
        if dial == 0:
            password += 1
    elif rotation[0] == "R":
        dial = (dial + int(rotation[1:])) % 100
        if dial == 0:
            password += 1

print(f"Solution to part 1 is: {password}")


# PART 2 # 

dial = 50
password = 0

for rotation in rotations:
    rotation_number = int(rotation[1:])
    full_passes = int(rotation_number / 100)
    partial_pass = rotation_number % 100
    password += full_passes

    if rotation[0] == "L":
        old_dial = dial
        dial = (dial - int(rotation_number)) % 100
        if dial == 0:
            password += 1
        elif old_dial < dial and old_dial != 0:
            password += 1
    elif rotation[0] == "R":
        old_dial = dial
        dial = (dial + int(rotation_number)) % 100
        if dial == 0:
            password += 1
        elif old_dial > dial and old_dial != 0:
            password += 1

print(f"Solution to part 2 is: {password}")