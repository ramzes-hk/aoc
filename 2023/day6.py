from io import TextIOWrapper


def part1(f: TextIOWrapper):
    line = f.readline()
    time: list[int] = []
    distance: list[int] = []
    while line:
        match line.split():
            case ["Time:", *objects]:
                time = [int(n) for n in objects]
            case ["Distance:", *objects]:
                distance = [int(n) for n in objects]
        line = f.readline()
    counters: list[int] = []
    for i, t in enumerate(time):
        count = 0
        for charge in range(t):
            if charge * (t - charge) > distance[i]:
                count += 1
        counters.append(count)
    total = 1
    for counter in counters:
        total *= counter
    print(total)


def part2(f: TextIOWrapper):
    line = f.readline()
    time = 0
    distance = 0
    while line:
        match line.split():
            case ["Time:", *objects]:
                time = int("".join(objects))
            case ["Distance:", *objects]:
                distance = int("".join(objects))
        line = f.readline()
    start = 0
    end = 0
    for t in range(time):
        if t * (time - t) > distance:
            start = t
            break
    for t in range(time, 0, -1):
        if t * (time - t) > distance:
            end = t
            break
    print(end - start + 1)


with open("day6.txt", "r") as f:
    part2(f)
