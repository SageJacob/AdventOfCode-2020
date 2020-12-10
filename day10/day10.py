def part1(s):
    one = 0
    three = 1
    i = 0
    while i < max(s):
        if i + 1 in s:
            i += 1
            one += 1
        elif i + 2 in s:
            i += 2
        elif i + 3 in s:
            i += 3
            three += 1
        else:
            break
    return one * three

def part2(arr):
    dp = [0] * len(arr)
    dp[0] = 1
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] - arr[j] <= 3:
                dp[i] += dp[j]
    return dp[len(arr)-1]

x = open('input10.txt', 'r')
s = set()
for line in x:
    s.add(int(line))
print(part1(s))
arr = []
for line in s:
    arr.append(line)
arr.append(0)
arr.sort()
print(part2(arr))