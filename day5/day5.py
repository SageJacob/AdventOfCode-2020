import math
def binary(x, one, other, end) -> int:
    start = 0
    for i in x:
        if i == one:
            end = math.floor((start + end) / 2)
        if i == other:
            start = math.ceil((start + end) / 2)
    if i == one:
        return end
    return start

def part1(x) -> int:
    maximum = 0
    count = 0
    for line in x:
        count += 1
        row = binary(line[:7], 'F', 'B', 127)
        col = binary(line[7:], 'L', 'R', 7)
        val = row * 8 + col
        maximum = max(maximum, val)
    return maximum

def part2(x) -> int:
    ids = []
    for line in x:
        row = binary(line[:7], 'F', 'B', 127)
        col = binary(line[7:], 'L', 'R', 7)
        val = row * 8 + col
        ids.append(val)
    ids = sorted(ids)
    length = len(ids)
    for i in range(length - 2):
        if ids[i+1] - ids[i] == 2:
            return ids[i+1] - 1

x = open("input5.txt", "r")
print(part1(x))
x = open("input5.txt", "r")
print(part2(x))