def part1(lines: list[str]):
    total = 0
    for line in lines:
        first: str = "0"
        last: str = "0"
        for char in line:
            if char.isdigit() and first == "0":
                first = char
                last = char
            elif char.isdigit():
                last = char
        total += int(first + last)
    print("\ntotal >>>>>", total)


def part2(lines: list[str]):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(lines)):
        string: str = ""
        for char in lines[i]:
            string += char
            for n in range(9):
                string = string.replace(numbers[n], str(n + 1) + numbers[n])
        lines[i] = string
        print(lines[i])
    part1(lines)


with open("day1.txt", "r") as f:
    lines = f.readlines()
    part2(lines)
