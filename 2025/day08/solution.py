import math

def calculate_Euclidean_distance(point1, point2):
    return math.sqrt(sum((point1[i] - point2[i])**2 for i in range(3)))

def main():
    filename = "tmp.txt"
    with open(filename, "r") as file:
        input = file.readlines()
    input = [list(map(int, line.strip().split(","))) for line in input]
    
    smallest = 1e10
    for point1 in input:
        for point2 in input:
            if point1 == point2:
                continue
            a = calculate_Euclidean_distance(point1, point2)
            if a < smallest:
                min = (point1, point2)
    print(min)

if __name__ == "__main__":
    main()