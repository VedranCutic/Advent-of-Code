import re

with open("input.txt", "r") as file:
    input = file.readlines()

pattern = r"mul\([0-9]*,[0-9]*\)"

mul_sum = 0
for line in input:
    matches = re.findall(pattern, line)
    for match in matches:
        mul_sum += int(match.split(",")[0].split("(")[1]) * int(
            match.split(",")[1].split(")")[0]
        )


print(f"Task 1: {mul_sum}")


mul_sum = 0

altered_pattern = r"mul\([0-9]*,[0-9]*\)|do\(\)|don't\(\)"

count = True
for line in input:
    matches = re.findall(altered_pattern, line)
    for match in matches:
        if count and match.startswith("mul"):
            mul_sum += int(match.split(",")[0].split("(")[1]) * int(
                match.split(",")[1].split(")")[0]
            )
        elif count and match == "don't()":
            count = False
        elif not count and match == "do()":
            count = True

print(f"Task 2: {mul_sum}")
