def beam_emmition(beams, manifold):
    if not manifold:
        return 0
    splits = 0
    for i, location in enumerate(manifold[0]):
        if location == "^" and i in beams:
            beams.remove(i)
            beams.add(i - 1)
            beams.add(i + 1)
            splits += 1
    return splits + beam_emmition(beams=beams, manifold=manifold[1:])


def beam_timelines(manifold):
    new_beams = [0] * len(manifold[0])
    new_beams[manifold[0].index("S")] = 1
    result = 1
    for i in range(1, len(manifold)):
        for j, location in enumerate(manifold[i]):
            if location == "^" and new_beams[j] > 0:
                new_beams[j - 1] += new_beams[j]
                new_beams[j + 1] += new_beams[j]
                result += new_beams[j]
                new_beams[j] = 0
    return result


def main():
    filename = "input.txt"
    with open(filename) as file:
        input = file.readlines()
    input = [line.strip() for line in input]

    beams = set()
    length = len(input[0])
    for i in range(length):
        if input[0][i] == "S":
            beams.add(i)
            break
    tachyon_splits = beam_emmition(beams=beams, manifold=input[1:])
    print(f"SOLUTION PART 1: {tachyon_splits}")
    timelines = beam_timelines(manifold=input)
    print(f"SOLUTION PART 2: {timelines}")


if __name__ == "__main__":
    main()
