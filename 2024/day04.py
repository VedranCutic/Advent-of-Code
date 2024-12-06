with open("input.txt", "r") as file:
    input = file.readlines()


def check_task1(c1, c2, c3):
    return c1 == "M" and c2 == "A" and c3 == "S"


def check_tas2():
    return


sum = 0
for i, line in enumerate(input):
    for j, character in enumerate(line):
        if character == "X":
            # HORIZONTAL BACKWARDS
            if j >= 3:
                if check_task1(line[j - 1], line[j - 2], line[j - 3]):
                    sum += 1
            # HORIZONTAL
            if len(line) - j > 3:
                if check_task1(line[j + 1], line[j + 2], line[j + 3]):
                    sum += 1

            # VERTICAL BACKWARDS
            if i >= 3:
                if check_task1(input[i - 1][j], input[i - 2][j], input[i - 3][j]):
                    sum += 1
            # VERTICAL
            if len(input) - i > 3:
                if check_task1(input[i + 1][j], input[i + 2][j], input[i + 3][j]):
                    sum += 1

            # DIAGONAL UPPER LEFT
            if j >= 3 and i >= 3:
                if check_task1(
                    input[i - 1][j - 1], input[i - 2][j - 2], input[i - 3][j - 3]
                ):
                    sum += 1
            # DIAGONAL UPPER RIGHT
            if len(line) - j > 3 and i >= 3:
                if check_task1(
                    input[i - 1][j + 1], input[i - 2][j + 2], input[i - 3][j + 3]
                ):
                    sum += 1
            # DIAGONAL BOTTOM LEFT
            if j >= 3 and len(input) - i > 3:
                if check_task1(
                    input[i + 1][j - 1], input[i + 2][j - 2], input[i + 3][j - 3]
                ):
                    sum += 1
            # DIAGONAL BOTTOM RIGHT
            if len(line) - j > 3 and len(input) - i > 3:
                if check_task1(
                    input[i + 1][j + 1], input[i + 2][j + 2], input[i + 3][j + 3]
                ):
                    sum += 1


print(f"Task 1: {sum}")


sum = 0


def check_task2(c1, c2, c3, c4):
    return (
        c1 == "A"
        and c2 == "S"
        and ((c3 == "M" and c4 == "S") or (c3 == "S" and c4 == "M"))
    )


for i, line in enumerate(input):
    for j, character in enumerate(line):
        if character == "M":
            # DIAGONAL UPPER LEFT
            if j >= 2 and i >= 2:
                if check_task2(
                    input[i - 1][j - 1],
                    input[i - 2][j - 2],
                    input[i][j - 2],
                    input[i - 2][j],
                ):
                    sum += 1
            # DIAGONAL UPPER RIGHT
            if len(line) - j > 2 and i >= 2:
                if check_task2(
                    input[i - 1][j + 1],
                    input[i - 2][j + 2],
                    input[i - 2][j],
                    input[i][j + 2],
                ):
                    sum += 1
            # DIAGONAL BOTTOM LEFT
            if j >= 2 and len(input) - i > 2:
                if check_task2(
                    input[i + 1][j - 1],
                    input[i + 2][j - 2],
                    input[i + 2][j],
                    input[i][j - 2],
                ):
                    sum += 1
            # DIAGONAL BOTTOM RIGHT
            if len(line) - j > 2 and len(input) - i > 2:
                if check_task2(
                    input[i + 1][j + 1],
                    input[i + 2][j + 2],
                    input[i + 2][j],
                    input[i][j + 2],
                ):
                    sum += 1


print(f"Task 2: {sum / 2}")
