import itertools


def part_one(lines: list[str]):
    lines = [line.strip() for line in lines]
    hor_space = [n for n, line in enumerate(lines) if not "#" in line]
    ver_space = [i for i, col in enumerate(zip(*lines)) if not "#" in col]
    for i in reversed(hor_space):
        lines.insert(i, "." * len(lines[i]))
    lines = ["".join(line) for line in zip(*lines)]
    for i in reversed(ver_space):
        lines.insert(i, "." * len(lines[i]))
    lines = ["".join(line) for line in zip(*lines)]
    glxs: list[list[int]] = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "#":
                glxs.append([i, j])
    combs = list(itertools.combinations(glxs, 2))
    total = 0
    for [y1, x1], [y2, x2] in combs:
        total += abs(y2 - y1) + abs(x2 - x1)
    print(total)


with open("day11.txt", "r") as f:
    part_one(f.readlines())
