def countOccupied(arr):
    counter = 0
    for i in arr:
        if i == '#':
            counter += 1
    return counter

def inbound(arr, k, l):
    if k >= 0 and l >= 0 and k < len(arr) and l < len(arr[0]):
        return True
    return False
  
def count_possible_adjacent(arr, i, j):
    counter = []
    outer = 0
    for k in range(i - 1, i + 2):
        for l in range(j - 1, j + 2):
            if k == i and l == j:
                continue
            if inbound(arr, k, l):
                counter.append(arr[k][l])
    return counter

def get_occupied(arr, k, l, k_change, l_change):
    while inbound(arr, k, l) and arr[k][l] == '.':
        l += l_change
        k += k_change
    if inbound(arr, k, l):
        return arr[k][l]

def count_viewable(arr, i, j):
    res = []
    k, l = i, j
    todo = [-1, 0, 1]
    for k_change in todo:
        for l_change in todo:
            if k_change == 0 and l_change == 0:
                continue
            res.append(get_occupied(arr, k+k_change, l+l_change, k_change, l_change))
    return res

def main(arr, part): 
    maxOccupied = 4 if part == 1 else 5
    changed = 1
    while changed > 0:
        new_arr = []
        changed = 0
        for i in range(len(arr)):
            row = []
            for j in range(len(arr[0])):
                if arr[i][j] == '.':
                    row.append('.')
                    continue
                occupied = count_possible_adjacent(arr, i, j) if part == 1 else count_viewable(arr, i, j)
                if arr[i][j] == 'L' and countOccupied(occupied) == 0:
                    row.append('#')
                    changed += 1
                elif arr[i][j] == '#' and countOccupied(occupied) >= maxOccupied:
                    row.append('L')
                    changed += 1
                else:
                    row.append(arr[i][j])
            new_arr.append(row)
        arr = new_arr
    counter = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == '#':
                counter += 1
    print(counter)

x = open('input11.txt', 'r')
arr = []
for line in x:
    line = line.strip('\n')
    arr.append(line)

main(arr, 1)
main(arr, 2)
