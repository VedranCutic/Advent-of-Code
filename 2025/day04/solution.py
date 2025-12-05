import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
from matplotlib.colors import BoundaryNorm, ListedColormap

def parse(filename):
    input_matrix = []
    with open(filename, "r") as file:
        lines = file.readlines()
    horizontal_filler = ["." for _ in range(len(lines[0]) + 1)]
    input_matrix.append(horizontal_filler)
    for line in lines:
        new_line = ["."]
        new_line.extend([sign for sign in line.strip()])
        new_line.append(".")
        input_matrix.append(new_line)

    input_matrix.append(horizontal_filler)
    parsed = np.matrix(input_matrix)
    return parsed


def find_removable(matrix):
    # Finds number of rolls to remove and
    # returns that number and a new matrix with removed
    # rolls

    result = 0
    new_matrix = np.copy(matrix)
    for i in range(1, matrix.shape[0] - 1):
        for j in range(1, matrix.shape[1] - 1):
            if matrix[i, j] != "@":
                continue
            tmp = matrix[i - 1: i + 2, j - 1: j + 2]
            if np.count_nonzero(tmp == "@") - 1 < 4:
                new_matrix[i, j] = "."
                result += 1

    return result, new_matrix


def create_gif(matrices):

    fig, ax = plt.subplots(facecolor="black")

    cmap = ListedColormap(["black", "gray", "red"])
    norm = BoundaryNorm([0, 1, 2, 3], cmap.N)

    sns.heatmap(matrices[0], cmap=cmap, norm=norm,
                cbar=False, square=True, ax=ax)
    ax.set_xticks([])
    ax.set_yticks([])

    def update(frame):
        ax.clear()
        sns.heatmap(matrices[frame], cmap=cmap, norm=norm,
                    cbar=False, square=True, ax=ax)
        ax.set_xticks([])
        ax.set_yticks([])
        return ax,

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=len(matrices),
        blit=False
    )

    ani.save("part2.gif", writer="pillow", fps=10)


def main():
    matrix = parse(filename="input.txt")

    result1, new_matrix = find_removable(matrix)
    print(f"SOLUTION FOR PART 1: {result1}")

    result2 = 0
    result = -99
    matrices = []
    new_matrix = np.copy(matrix)
    while result != 0:
        matrices.append(new_matrix == "@")
        result, result_matrix = find_removable(new_matrix)
        if result != -99:
            matrices.append(np.where((result_matrix == ".") & (new_matrix == "@"), 2, result_matrix == "@"))
        new_matrix = result_matrix
        result2 += result
    print(f"SOLUTION FOR PART 2: {result2}")

    create_gif(matrices)


if __name__ == "__main__":
    main()