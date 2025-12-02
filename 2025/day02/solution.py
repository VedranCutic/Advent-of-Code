import re

regex_pattern = r"^(\d+)\1$"

with open("input.txt", "r") as file:
    input = file.readline()


# PART 1 #

result = 0

for ID_ranges in input.split(","):
    ID_ranges = ID_ranges.split("-")
    IDs = range(int(ID_ranges[0]), int(ID_ranges[1]) + 1, 1)
    for ID in IDs:
        if re.match(regex_pattern, str(ID)):
            result += ID

print(f"Solution to part 1 is: {result}")

# PART 2 #

regex_pattern = r"^(\d+)\1+$"

result = 0

for ID_ranges in input.split(","):
    ID_ranges = ID_ranges.split("-")
    IDs = range(int(ID_ranges[0]), int(ID_ranges[1]) + 1, 1)
    for ID in IDs:
        if re.match(regex_pattern, str(ID)):
            result += ID

print(f"Solution to part 2 is: {result}")