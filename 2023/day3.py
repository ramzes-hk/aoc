symbols = {"/", "*", "-", "#", "@", "=", "+", "%", "$", "&"}
directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]


class Number:
    def __init__(self, value: int, xb: int, xe: int, y: int) -> None:
        self.value = value
        self.xb = xb
        self.xe = xe
        self.y = y
        self.checked = False

    def __repr__(self) -> str:
        return f"{self.value} {self.xb} {self.xe} {self.y}\n"


def numberify(lines: list[str]) -> list[Number]:
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
    return numbers


def clamp(n: int, m: int) -> int:
    return max(0, min(m, n))


def part1(lines: list[str]):
    width = len(lines[0]) - 1
    height = len(lines) - 1
    numbers = numberify(lines)

    total = 0
    for number in numbers:
        flag = False
        for x in range(number.xb, number.xe + 1):
            for [ver, hor] in directions:
                sx = clamp(x + ver, width)
                sy = clamp(number.y + hor, height)
                if lines[sy][sx] in symbols:
                    total += number.value
                    flag = True
                    break
            if flag:
                break
    print(total)


def part2(lines: list[str]):
    numbers = numberify(lines)
    height = len(lines) - 1
    width = len(lines[0]) - 1
    total = 0

    for number in numbers:
        if number.checked:
            continue
        number.checked = True
        flag = False
        for x in range(number.xb, number.xe + 1):
            for [ver, hor] in directions:
                sy = clamp(number.y + ver, height)
                sx = clamp(x + hor, width)
                if lines[sy][sx] == "*":
                    for [ver, hor] in directions:
                        star_y = clamp(sy + ver, height)
                        star_x = clamp(sx + hor, width)
                        for star_number in numbers:
                            if star_number.checked:
                                continue
                            if (
                                star_number.y == star_y
                                and star_x in range(star_number.xb, star_number.xe + 1)
                                and not star_number.checked
                            ):
                                total += number.value * star_number.value
                                star_number.checked = True
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
    part2(lines)
