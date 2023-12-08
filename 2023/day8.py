from io import TextIOWrapper


def part1(f: TextIOWrapper):
    line = f.readline()
    moves: str = ""
    destinations: dict[str, list[str]] = dict()
    while line:
        match line.split():
            case [dir]:
                moves = dir
            case [dest, "=", left, right]:
                destinations.update({dest: [left[1:-1], right[:-1]]})
        line = f.readline()
    count = 0
    current = "AAA"
    while current != "ZZZ":
        for move in moves:
            next = destinations[current]
            if move == "L":
                current = next[0]
            else:
                current = next[1]
            count += 1
    print(count)


with open("day8.txt", "r") as f:
    part1(f)
