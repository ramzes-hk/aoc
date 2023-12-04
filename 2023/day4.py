def part1(lines: list[str]):
    total = 0
    for line in lines:
        count = 0
        number = line.split(":")[1].split("|")
        winning = set(number[0].strip().replace("  ", " ").split(" "))
        my = number[1].strip().replace("  ", " ").split(" ")
        for num in my:
            if num in winning:
                count += 1
        if count != 0:
            total += 2 ** (count - 1)
    print(total)


def part2(lines: list[str]):
    total = 0
    wins: list[int] = [1 for _ in range(len(lines))]
    for i, line in enumerate(lines):
        count = 0
        number = line.split(":")[1].split("|")
        winning = set(number[0].strip().replace("  ", " ").split(" "))
        my = number[1].strip().replace("  ", " ").split(" ")
        for num in my:
            if num in winning:
                count += 1
        for j in range(1, count + 1):
            wins[i + j] += wins[i]
    for w in wins:
        total += w
    print(total)


with open("day4.txt", "r") as f:
    lines = f.readlines()
    part2(lines)
