from io import TextIOWrapper


def part1(f: TextIOWrapper):
    seeds: list[int] = []
    line = f.readline()
    while line:
        maps: list[list[int]] = []
        match line.strip().split():
            case ["seeds:", *objects]:
                seeds = [int(n) for n in objects]
            case [_, "map:"]:
                map_line = f.readline().strip()
                while map_line:
                    maps.append([int(n) for n in map_line.split()])
                    map_line = f.readline().strip()
                for i, seed in enumerate(seeds):
                    for map in maps:
                        if map[1] <= seed < map[1] + map[2]:
                            seeds[i] = map[0] - map[1] + seed
        line = f.readline()
    print(min(seeds))


with open("day5.txt", "r") as f:
    part1(f)
