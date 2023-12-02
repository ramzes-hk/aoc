def part1(lines: list[str]):
    limit = {"red": 12, "green": 13, "blue": 14}
    total = 0
    for line in lines:
        flag = True
        id = line.split(":")[0].split(" ")[1]
        handfuls = line.strip().split(":")[1].split(";")
        for handful in handfuls:
            cubes = handful.strip().split(",")
            cubes = [cube.strip().split(" ") for cube in cubes]
            for cube in cubes:
                if limit[cube[1]] < int(cube[0]):
                    flag = False
        if flag:
            total += int(id)
    print(total)


with open("day2.txt", "r") as f:
    lines = f.readlines()
part1(lines)
