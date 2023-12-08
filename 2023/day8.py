from io import TextIOWrapper
from math import gcd


def lcm(a, b):
    """Calculate the Least Common Multiple of two numbers."""
    return a * b // gcd(a, b)


def lcd(array):
    """Find the Lowest Common Denominator (LCD) for an array of numbers."""
    # Initialize the result with the first number in the array
    result = array[0]
    for i in range(1, len(array)):
        result = lcm(result, array[i])
    return result


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


def part2(f: TextIOWrapper):
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
    current = [key for key in destinations.keys() if key[2] == "A"]
    node_counters = [0 for _ in range(len(current))]

    for i in range(len(current)):
        while current[i][2] != "Z":
            for move in moves:
                next = destinations[current[i]]
                if move == "L":
                    current[i] = next[0]
                else:
                    current[i] = next[1]
                node_counters[i] += 1
    print(lcd(node_counters))


with open("day8.txt", "r") as f:
    part2(f)
