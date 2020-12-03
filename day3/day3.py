x = open("input3.txt", "r")
arr = []
for line in x:
    arr.append(line.strip('\n'))
def part1(arr):
    row, col = len(arr), len(arr[0])
    i, j = 0, 0
    trees = 0
    while i < row and j < col:
        if arr[i][j] == '#':
            trees += 1
        i += 1
        j += 3
        if j >= col:
            j = j - col
    print(trees)

def part2(arr):
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    row, col = len(arr), len(arr[0])
    nums = []
    for slope in slopes:
        i, j = 0, 0
        trees = 0
        while i < row and j < col:
            if arr[i][j] == '#':
                trees += 1
            i += slope[1]
            j += slope[0]
            if j >= col:
                j = j - col
        nums.append(trees)
    ans = 1
    for i in nums:
        ans *= i
    print(ans)

part1(arr)
part2(arr)