from itertools import groupby
from itertools import product


def is_valid(line: list[str], dmgd: list[int]) -> bool:
    counter = [list(g) for _, g in groupby(line)]
    return True if [len(g) for g in counter if "#" in g] == dmgd else False


def part_one(lines: list[str]):
    total = 0
    for line in lines:
        [springs, dmgd] = line.split()
        springs = list(springs)
        dmgd = [int(n) for n in dmgd.split(",")]
        pos = [i for i, char in enumerate(line) if char == "?"]
        combs = product("#.", repeat=len(pos))
        for comb in combs:
            for i, p in enumerate(pos):
                springs[p] = comb[i]
            if is_valid(springs, dmgd=dmgd):
                total += 1
    print(total)


with open("day12.txt", "r") as f:
    part_one(f.readlines())
