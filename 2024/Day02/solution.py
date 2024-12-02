def is_safe(report, count_errors=False):

    report = report.split(" ")
    for i, r in enumerate(report):
        report[i] = int(r)

    tmp = 0

    # will be set to -1 for decreasing, and to 1 for increasing
    trend = 0
    errors = 0

    for i, level in enumerate(report):
        if i == 0:
            tmp = level
        if i == 1:
            if level > tmp:
                if tmp + 1 <= level <= tmp + 3:
                    trend = 1
                    tmp = level
            elif level < tmp:
                if tmp - 1 >= level >= tmp - 3:
                    trend = -1
                    tmp = level
            else:
                errors += 1
        if i > 1:
            if trend == 1:
                if not (tmp + 1 <= level <= tmp + 3):
                    errors += 1
            else:
                if not (tmp - 1 >= level >= tmp - 3):
                    errors += 1
            tmp = level

    if count_errors:
        return errors <= 1
    else:
        return errors == 0


with open("input.txt", "r") as input_file:
    input = input_file.readlines()

are_safe = 0
for inp in input:
    if is_safe(inp):
        are_safe += 1

print(are_safe)

error_calibration = 0
for inp in input:
    if is_safe(inp, count_errors=True):
        error_calibration += 1

print(error_calibration)
