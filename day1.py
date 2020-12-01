x = open('input1.txt', 'r')
arr = {}
for line in x:
    arr[int(line)] = int(line)
def part1(arr):
    for i in arr:
        if 2020 - arr[i] in arr:
            print(i*(2020-arr[i]))

def part2(arr):
    for i in arr:
        bal = 2020 - arr[i]
        for j in arr:
            if arr[i] != arr[j]:
                if bal - arr[j] in arr:
                    print(arr[i] * arr[j] * (bal - arr[j]))

part2(arr)