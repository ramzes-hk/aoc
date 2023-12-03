symbols = {"/", "*", "-", "#", "@", "=", "+", "%", "$", "&"}
directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]


class Number:
    def __init__(self, value: int, xb: int, xe: int, y: int) -> None:
        self.value = value
        self.xb = xb
        self.xe = xe
        self.y = y

    def __repr__(self) -> str:
        return f"{self.value} {self.xb} {self.xe} {self.y}\n"


def part1(lines: list[str]):
    width = len(lines[0]) - 1
    height = len(lines) - 1
    numbers: list[Number] = []

    for i, line in enumerate(lines):
        current_number = ""
        xb = 0
        y = i
        for j, char in enumerate(line):
            if char.isdigit():
                if current_number == "":
                    xb = j
                current_number += char
            elif not current_number == "":
                numbers.append(Number(int(current_number), xb, j - 1, y))
                current_number = ""
            else:
                continue
    total = 0
    for number in numbers:
        flag = False
        for x in range(number.xb, number.xe + 1):
            for [ver, hor] in directions:
                if (
                    lines[max(0, min(height, number.y + ver))][
                        max(0, min(width, x + hor))
                    ]
                    in symbols
                ):
                    total += number.value
                    flag = True
                    break
            if flag:
                break
    print(total)


with open("day3.txt", "r") as f:
    lines = f.readlines()
    # symbols: set[str] = set()
    # for line in lines:
    #     for char in line.strip():
    #         if char.isdigit() or char == '.':
    #             continue
    #         symbols.update(char)
    # print(symbols)
    part1(lines)
