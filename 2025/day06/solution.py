import numpy as np


def parse(filename):
    with open(filename, "r") as file:
        input = file.readlines()
    input = [line.strip().split(" ") for line in input]
    new_input = []
    for i, line in enumerate(input):
        print(line)
        new_input.append([val for val in line])
    # new_input = np.matrix(new_input)
    return new_input


def main():
    input = parse("tmp.txt")
    print(input)
    input = input.T
    result = 0
    for math_question in input:
        numbers = math_question[:, : - 1].astype(np.int64)
        operation = math_question[:, -1]
        if operation == "+":
            result += np.sum(numbers)
        else:
            result += np.prod(numbers)
        print(result)

    print(f"SOLUTION PART 1: {result}")


if __name__ == "__main__":
    main()
