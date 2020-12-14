x = open('input11.txt', 'r')
arr = []
for line in x:
    line = line.strip('\n')
    arr.append(line)

def countOccupied(arr):
    counter = 0
    for i in arr:
        if i == '#':
            counter += 1
    return counter
    
def inbounds(arr, i, j):
    counter = []
    outer = 0
    for k in range(i - 1, i + 2):
        for l in range(j - 1, j + 2):
            if k == i and l == j:
                continue
            if k >= 0 and l >= 0 and k < len(arr) and l < len(arr[0]):
                counter.append(arr[k][l])
    return counter 
def show(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end='')
        print()
    print()
changed = 1
while changed > 0:
    new_arr = []
    changed = 0
    show(arr)
    for i in range(len(arr)):
        row = []
        for j in range(len(arr[0])):
            if arr[i][j] == '.':
                row.append('.')
                continue
            occupied = inbounds(arr, i, j)
            if arr[i][j] == 'L' and countOccupied(occupied) == 0:
                row.append('#')
                #arr[i] = arr[i][0:j] + '#' + arr[i][j+1:]
                changed += 1
            elif arr[i][j] == '#' and countOccupied(occupied) >= 4:
                row.append('L')
                #arr[i] = arr[i][0:j] + 'L' + arr[i][j+1:]
                changed += 1
            else:
                row.append(arr[i][j])
        new_arr.append(row)
    arr = new_arr
    show(arr)
counter = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == '#':
            counter += 1
print(counter)