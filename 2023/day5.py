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


# def part2(f: TextIOWrapper):
#     line = f.readline()
#     seeds: list[list[int]] = []
#     while line:
#         maps: list[list[int]] = []
#         next_seeds: list[list[int]] = []
#         match line.strip().split():
#             case ["seeds:", *objects]:
#                 seeds = [[int(n) for n in objects[i : i + 2]] for i in range(0, len(objects), 2)]
#             case [_, "map:"]:
#                 map_line = f.readline().strip()
#                 while map_line:
#                     maps.append([int(n) for n in map_line.split()])
#                     map_line = f.readline().strip()
#                 counter = 0
#                 for seed in seeds:
#                     for map in maps:
#                         if map[1] <= seed[0] and map[1] + map[2] > seed[0] + seed[1]:
#                          elif map[1] > seed[0] and map[1] + map[2] > seed[0] + seed[1]:
#                              counter += 1
#                          elif map[1] <= seed[0] and map[1] + map[2] <= seed[0] + seed[1]:
#                              counter += 1
#                          elif map[1] > seed[0] and map[1] + map[2] <= seed[0] + seed[1]:
#                              counter += 1
#                 print(counter)
#
#     if next_seeds:
#         seeds = [[n for n in i] for i in next_seeds]
#     line = f.readline()
# print(seeds)


with open("day5.txt", "r") as f:
    part1(f)
