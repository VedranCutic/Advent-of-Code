with open("input.txt", "r") as file:
    input = file.readlines()

input = [line.strip() for line in input]


list_of_fresh = []
for i, line in enumerate(input):
    try:
        a, b = map(int, line.strip().split("-"))
        list_of_fresh.append((a, b - a))
    except Exception:
        i += 1
        break

list_of_available = []
result = 0
for j in range(i, len(input)):
    for k in range(len(list_of_fresh)):
        if int(input[j]) > list_of_fresh[k][0] and  \
             int(input[j]) - list_of_fresh[k][0] <= list_of_fresh[k][1]:
            result += 1
            break

print(f"SOLUTION FOR PART 1: {result}")

list_of_ranges = []
for i, line in enumerate(input):
    try:
        a, b = map(int, line.strip().split("-"))
        list_of_ranges.append((a, b))
    except Exception:
        i += 1
        break
list_of_ranges = sorted(list_of_ranges)
result = 0
for i, (a, b) in enumerate(list_of_ranges):
    if i == 0:
        start = a
        end = b
        result += end - start + 1
    else:
        if a <= end:
            start = end
            if b <= end:
                continue
            end = b
            result += end - start
        else:
            start = a
            end = b
            result += end - start + 1


print(f"SOLUTION FOR PART 2: {result}")