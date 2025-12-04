import numpy as np

with open("input.txt") as file:
    inputs = file.readlines()
banks = [input.strip() for input in inputs]

# PART 1 # 

total_joltage = 0
for bank in banks:
    battery = np.array([int(b) for b in bank])
    battery_sorted_indexes = battery.argsort()[::-1]
    battery_sorted = battery[battery_sorted_indexes]

    if battery_sorted_indexes[0] < battery_sorted_indexes[1]:
        total_joltage += int(f"{battery_sorted[0]}{battery_sorted[1]}")
    elif battery_sorted_indexes[0] == len(bank) - 1:
        total_joltage += int(f"{battery_sorted[1]}{battery_sorted[0]}")
    else:
        first_battery = int(battery_sorted[0])
        second_battery = -99
        for value, index in zip(battery_sorted[1:], battery_sorted_indexes[1:]):
            if int(value) > second_battery and index > battery_sorted_indexes[0] or int(value) == first_battery:
                second_battery = int(value)
        total_joltage += int(f"{first_battery}{second_battery}")

print(f"SOLUTION FOR PART1: {total_joltage}")


total_joltage = 0
for bank in banks:
    battery = np.array([int(b) for b in bank])
    battery_sorted_indexes = battery.argsort()[::-1]
    battery_sorted = battery[battery_sorted_indexes]
    break


# PART 2 # 

total_joltage = 0

def find_max_index(battery, length=2):
    max = -1
    new_max_i = -1
    for i, b in enumerate(battery):
        if len(battery) - i < length:
            break
        if b > max:
            max = b
            new_max_i = i
    return [max], battery[new_max_i + 1:]


for bank in banks:
    battery = np.array([int(b) for b in bank])
    max_i = 0
    joltage = []
    length = 13
    while len(joltage) != 12:
        max, battery = find_max_index(battery, length - 1)
        length -= 1
        joltage.extend(max)
    joltage = [str(jolt) for jolt in joltage]
    total_joltage += int("".join(joltage))

print(f"SOLUTION FOR PART2: {total_joltage}")
