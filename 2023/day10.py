dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]
tubes = [["|", "7", "F"], ["-", "7", "J"], ["|", "L", "J"], ["-", "L", "F"]]


def clamp_pos(orig: list[int], dir: list[int], border: list[int]):
    return [max(0, min(border[i], orig[i] + dir[i])) for i in range(2)]


def begin(lines: list[str], pos: list[int]):
    next_pos: list[int] = []
    dir: list[int] = []
    for i, dir in enumerate(dirs):
        next_pos = clamp_pos(pos, dir, [len(lines[0]), len(lines)])
        if lines[next_pos[1]][next_pos[0]] in tubes[i]:
            break
    return (next_pos, dir)


def part_one(lines: list[str]):
    start = [0, 0]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != "S":
                continue
            start = [int(j), int(i)]
            break
    [pos, dir] = begin(lines, start)
    count = 0
    while lines[pos[1]][pos[0]] != "S":
        match [lines[pos[1]][pos[0]], dir]:
            case ["|", [0, 1]]:
                pos = [pos[0], pos[1] + 1]
            case ["|", [0, -1]]:
                pos = [pos[0], pos[1] - 1]
            case ["-", [1, 0]]:
                pos = [pos[0] + 1, pos[1]]
            case ["-", [-1, 0]]:
                pos = [pos[0] - 1, pos[1]]
            case ["7", [0, -1]]:
                pos = [pos[0] - 1, pos[1]]
                dir = [-1, 0]
            case ["7", [1, 0]]:
                dir = [0, 1]
                pos = [pos[0], pos[1] + 1]
            case ["F", [0, -1]]:
                dir = [1, 0]
                pos = [pos[0] + 1, pos[1]]
            case ["F", [-1, 0]]:
                dir = [0, 1]
                pos = [pos[0], pos[1] + 1]
            case ["L", [0, 1]]:
                dir = [1, 0]
                pos = [pos[0] + 1, pos[1]]
            case ["L", [-1, 0]]:
                dir = [0, -1]
                pos = [pos[0], pos[1] - 1]
            case ["J", [0, 1]]:
                dir = [-1, 0]
                pos = [pos[0] - 1, pos[1]]
            case ["J", [1, 0]]:
                dir = [0, -1]
                pos = [pos[0], pos[1] - 1]
        count += 1
        print(lines[pos[1]][pos[0]])
    print(count // 2 + 1)


with open("day10.txt", "r") as f:
    part_one(f.readlines())
