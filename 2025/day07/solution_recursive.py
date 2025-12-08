MEMO = {}


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


def beam_timelines(beam, manifold):
    if not manifold:
        return 1
    
    if (beam, tuple(manifold)) in MEMO:
        return MEMO[beam, tuple(manifold)]

    for i, location in enumerate(manifold[0]):
        if location == "^" and beam == i:
            left = beam_timelines(beam - 1, manifold[1:])
            right = beam_timelines(beam + 1, manifold[1:])
            result = left + right
            break
    else:
        result = beam_timelines(beam, manifold[1:])
    
    MEMO[beam, tuple(manifold)] = result
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
            beam = i
            break
    tachyon_splits = beam_emmition(beams=beams, manifold=input[1:])
    print(f"SOLUTION PART 1: {tachyon_splits}")
    timelines = beam_timelines(beam=beam, manifold=input[1:])
    print(f"SOLUTION PART 2: {timelines}")


if __name__ == "__main__":
    main()
