import math
import itertools

MAX_CONNECTIONS = 10


# collection of all the points keyed to their x,y,z values
def create_collection(input: list):
    collection = {}
    for i in range(len(input)):
        collection[i] = input[i]
    return collection


def calculate_Euclidean_distance(point1, point2):
    return math.sqrt(sum((point1[i] - point2[i]) ** 2 for i in range(3)))


def main():
    filename = "input.txt"
    with open(filename, "r") as file:
        input = file.readlines()
    input = [list(map(int, line.strip().split(","))) for line in input]

    collection = create_collection(input)
    combinations = itertools.combinations(collection, 2)

    # this is a list that saves the smalles distance between two points
    euclidean_distances = []
    for c in combinations:
        hash1, hash2 = c
        p1 = collection[hash1]
        p2 = collection[hash2]
        dist = calculate_Euclidean_distance(p1, p2)
        euclidean_distances.append((dist, hash1, hash2))
    euclidean_distances_sorted = sorted(euclidean_distances, key=lambda x: x[0])

    connections = []
    used_points = set()
    for connection in euclidean_distances_sorted[:MAX_CONNECTIONS]:
        # start
        if not connections:
            p1, p2 = connection[1:]
            used_points.add(p1)
            used_points.add(p2)
            connections.append({p1, p2})

        else:
            p1, p2 = connection[1:]
            if p1 in used_points or p2 in used_points:
                for i, c in enumerate(connections):
                    if p1 in c or p2 in c:
                        connections[i].add(p1)
                        connections[i].add(p2)
                        used_points.add(p1)
                        used_points.add(p2)
            else:
                used_points.add(p1)
                used_points.add(p2)
                connections.append({p1, p2})

    # some circuits(sets) have same boxes and they should be connected
    # into one new circuit
    merged = []
    found = True
    while found:
        for circuit1 in connections:
            found = None
            for circuit2 in merged:
                if circuit1 & circuit2:
                    circuit2 |= circuit1
                    found = circuit2
                    break

            if not found:
                merged.append(circuit1)
            # transitive overlap

    sizes = []
    for c in merged:
        sizes.append(len(c))

    print(sizes)
    print(f"SOLUTION PART1: {math.prod(sizes)}")


if __name__ == "__main__":
    main()
