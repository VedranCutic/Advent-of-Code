with open("test.txt", "r") as file:
    input = file.read()


rules = input.split("\n\n")[0].split("\n")
updates = input.split("\n\n")[1].split("\n")

ordering_after = {}
for rule in rules:
    first = rule.split("|")[0]
    second = rule.split("|")[1]
    if first not in ordering_after:
        ordering_after[first] = [second]
    else:
        ordering_after[first].append(second)

ordering_before = {}
for rule in rules:
    first = rule.split("|")[1]
    second = rule.split("|")[0]
    if first not in ordering_before:
        ordering_before[first] = [second]
    else:
        ordering_before[first].append(second)

print(ordering_after)
print(ordering_before)

correct_updates = 0
for update in updates:
    elements = update.split(",")
    correct = 0
    for element in elements:
        if element in ordering_after and element in ordering_before:
            for after in ordering_after[element]:
                if after not in elements[0 : elements.index(element)]:
                    for before in ordering_before[element]:
                        if before not in elements[elements.index(element) + 1 :]:
                            correct += 1
        elif element in ordering_after:
            for after in ordering_after[element]:
                if after not in elements[0 : elements.index(element)]:
                    correct += 1
        elif element in ordering_before:
            for before in ordering_before[element]:
                if before not in elements[elements.index(element) + 1 :]:
                    correct += 1
        else:
            correct += 1

    if correct == len(elements):
        print(update)
        correct_updates += 1

print(correct_updates)
