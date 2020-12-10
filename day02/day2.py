x = open('input2.txt', 'r')

def part1(x):
    for line in x:
        string = line.split(' ')
        boundaries = string[0].split('-')
        low, hi = int(boundaries[0]), int(boundaries[1])
        letter = string[1][0]
        curr = 0
        for i in string[2]:
            if i == letter:
                print(f'here: {i, letter}')
                curr += 1
        if curr >= low and curr <= hi:
            print(low, hi, curr)
            valid += 1
    return valid

def part2(x):
    valid = 0
    for line in x:
        string = line.split(' ')
        boundaries = string[0].split('-')
        low, hi = int(boundaries[0]), int(boundaries[1])
        letter = string[1][0]
        count = 0
        if string[2][low-1] == letter:
            count += 1
        if string[2][hi-1] == letter:
            count += 1
        if count == 1:
            valid += 1
    return valid
