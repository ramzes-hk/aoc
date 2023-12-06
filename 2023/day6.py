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


with open("day6.txt", "r") as f:
    part1(f)
