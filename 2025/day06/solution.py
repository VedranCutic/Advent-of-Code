import numpy as np


def parse_part1(filename):
    with open(filename, "r") as file:
        input = file.readlines()
    input = [line.strip().split(" ") for line in input]
    new_input = []
    for i, line in enumerate(input):
        new_input.append([val for val in line if val != ""])
    new_input = np.matrix(new_input)
    return new_input


def calculate(numbers, operation):
    if operation == "+":
        return np.sum(numbers)
    else:
        return np.prod(numbers)


def parse_part2(filename):
    with open(filename, "r") as file:
        input = file.readlines()
    input = [[line.rstrip("\n")] for line in input]
    input = [list(row[0]) for row in input]
    input[-1].extend([""] * (len(input[0]) - len(input[-1])))
    input = np.matrix(input)
    return input


def main():
    filename = "input.txt"
    input = parse_part1(filename)
    input = input.T
    result = 0
    for math_question in input:
        numbers = math_question[:, :-1].astype(np.int64)
        operation = math_question[:, -1]
        if operation == "+":
            result += np.sum(numbers)
        else:
            result += np.prod(numbers)

    print(f"SOLUTION PART 1: {result}")

    input = parse_part2(filename)
    start = 0
    result = 0
    for col in range(input.shape[1]):
        if np.all(input[:-1, col] == " "):
            submatrix = np.array(input[:-1, start:col].T)
            numbers = [int("".join(num)) for num in submatrix]
            operation = input[-1, start]
            result += calculate(numbers, operation)
            start = col + 1
        elif col == input.shape[1] - 1:
            submatrix = np.array(input[:-1, start : col + 1].T)
            numbers = [int("".join(num)) for num in submatrix]
            operation = input[-1, start]
            result += calculate(numbers, operation)

    print(f"SOLUTION PART 2: {result}")


if __name__ == "__main__":
    main()
