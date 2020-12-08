
def part1(x):
    accumulator = 0
    length = len(arr)
    i = 0
    s = set()
    while i < length:
        if i in s:
            break
        s.add(i)
        if arr[i][0] == 'acc':
            accumulator += int(arr[i][1])
        if arr[i][0] == 'jmp':
            i += int(arr[i][1])
            continue
        i += 1
    print(accumulator)
    return arr

def alternate(instruct):
    if instruct == 'acc':
        return 'acc'
    if instruct == 'nop':
        return 'jmp'
    else:
        return 'nop'

def part2(arr):
    length = len(arr)
    accumulator = 0
    line = 0
    while line < length:
        i = 0
        d = {}
        # flip instruction
        arr[line][0] = alternate(arr[line][0])
        # check for infinite loop given the new instruction
        while i < length:
            if i not in d:
                d[i] = 0
            d[i] += 1
            # This number will probably need to be be tweaked depending on how many times you expect
            # the normal instructions to run. 
            if d[i] == 10:
                arr[line][0] = alternate(arr[line][0])
                break
            if arr[i][0] == 'acc':
                accumulator += int(arr[i][1])
            if arr[i][0] == 'jmp':
                i += int(arr[i][1])
                continue
            i += 1
        if i >= length:
            part1(arr)
            break
        line += 1
    
x = open('input8.txt', 'r')
arr = [line.split() for line in x]
part1(arr)
part2(arr)
