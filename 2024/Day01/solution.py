input = []

with open("input.txt", "r") as input_file:
    input = input_file.readlines()

left_list = []
right_list = []

for line in input:
    tmp = line.split("   ")
    left_list.append(int(tmp[0]))
    right_list.append(int((tmp[1]).strip()))

left_list = sorted(left_list)
right_list = sorted(right_list)

solution = 0
for i in range(len(left_list)):
    solution += abs(left_list[i] - right_list[i])

print(f"Task 1: {solution}")


similarity = 0
left_list_dict = {}
right_list_dict = {}

for i in range(len(left_list)):
    if left_list[i] not in left_list_dict:
        left_list_dict[left_list[i]] = 1
    else:
        left_list_dict[left_list[i]] += 1
    if right_list[i] not in right_list_dict:
        right_list_dict[right_list[i]] = 1
    else:
        right_list_dict[right_list[i]] += 1

for i in range(len(left_list)):
    if left_list[i] in right_list_dict:
        similarity += left_list[i] * right_list_dict[left_list[i]]

print(f"Task 2: {similarity}")
