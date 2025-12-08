import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
from matplotlib.colors import BoundaryNorm, ListedColormap, LogNorm


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
    matrices_visualization = []
    tmp = np.zeros((len(manifold), len(manifold[0])))
    matrices_visualization.append(tmp.copy())
    new_beams = [0] * len(manifold[0])
    new_beams[manifold[0].index("S")] = 1
    tmp[0] = np.array(new_beams)
    matrices_visualization.append(tmp.copy())
    result = 1
    for i in range(1, len(manifold)):
        for j, location in enumerate(manifold[i]):
            if location == "^" and new_beams[j] > 0:
                new_beams[j - 1] += new_beams[j]
                new_beams[j + 1] += new_beams[j]
                result += new_beams[j]
                new_beams[j] = 0
        tmp[i] = np.array(new_beams)
        matrices_visualization.append(tmp.copy())
    return result, matrices_visualization


def create_gif(matrices):

    matrices = [np.array(m, dtype=float) + 1e-10 for m in matrices]
    fig, ax = plt.subplots(facecolor="#0d1117")
    cmap = "cividis"
    sns.heatmap(
        matrices[0], cmap=cmap, norm=LogNorm(), cbar=False
    )  # or "plasma", "magma", "cividis"
    ax.set_xticks([])
    ax.set_yticks([])

    def update(frame):
        ax.clear()
        sns.heatmap(
            matrices[frame],
            cmap=cmap,
            norm=LogNorm(),
            cbar=False,
            square=True,
            ax=ax,
        )
        ax.set_xticks([])
        ax.set_yticks([])
        return (ax,)

    ani = animation.FuncAnimation(fig, update, frames=len(matrices), blit=False)

    ani.save("day07.gif", writer="pillow", fps=25)


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
    timelines, matrices_vis = beam_timelines(manifold=input)
    print(f"SOLUTION PART 2: {timelines}")
    create_gif(matrices_vis)


if __name__ == "__main__":
    main()
