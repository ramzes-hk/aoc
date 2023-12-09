def part_one(lines: list[str]):
    total = 0
    for line in lines:
        arr = [int(n) for n in line.split()]
        last = []
        while any(arr):
            last.append(arr[-1])
            arr = [arr[i] - arr[i - 1] for i in range(1, len(arr))]
        total += sum(last)
    print(total)


def part_two(lines: list[str]):
    total = 0
    for line in lines:
        arr = [int(n) for n in line.split()]
        last = []
        while any(arr):
            last.append(arr[0])
            arr = [arr[i] - arr[i - 1] for i in range(1, len(arr))]
        curr = 0
        while last:
            val = last.pop()
            curr = val - curr
        total += curr
    print(total)


with open("day9.txt", "r") as f:
    part_two(f.readlines())
