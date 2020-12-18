x = open('input12.txt', 'r')
arr = []

for line in x:
    line = line.strip('\n')
    arr.append(line)

d = {'N': 90, 'S': 270, 'E': 0, 'W': 180}

def forward(angle, units, horizontal, vertical):
    if angle == d['N']:
        vertical += units
    if angle == d['S']:
        vertical += -units
    if angle == d['E']:
        horizontal += units
    if angle == d['W']:
        horizontal += -units
    return vertical, horizontal

def letters(letter, units, horizontal, vertical):
    if letter == 'N':
        vertical += units
    if letter == 'S':
        vertical += -units
    if letter == 'E':
        horizontal += units
    if letter == 'W':
        horizontal += -units
    return vertical, horizontal

def rotate(angle, letter, units):
    if letter == 'R':
        angle += 360
        angle -= units
        return angle % 360
    if letter == 'L':
        angle += units
        return angle % 360

def part1(arr):
    vertical, horizontal = 0, 0
    angle = 0
    for direction in arr:
        letter = direction[0]
        units = int(direction[1:])
        if letter == 'F':
            vertical, horizontal = forward(angle, units, horizontal, vertical)
        elif letter == 'L' or letter == 'R':
            angle = rotate(angle, letter, units)
        else:
            vertical, horizontal = letters(letter, units, horizontal, vertical)

    print(abs(vertical) + abs(horizontal))


def perform_rotation(units, add_horizontal, add_vertical):
    if units == 90:
        add_horizontal, add_vertical = add_vertical, -add_horizontal
    # On 180, both signs change ([1,0] on a unit circle to [-1, 0])
    if units == 180:
        add_horizontal, add_vertical = -add_horizontal, -add_vertical
    if units == 270:
        add_horizontal, add_vertical = -add_vertical, add_horizontal
    return add_horizontal, add_vertical


def part2(arr):
    add_horizontal, add_vertical = 10, 1 # waypoint_horizontal = horizontal + add_horizontal
    horizontal, vertical = 0, 0
    for direction in arr:
        letter = direction[0]
        units = int(direction[1:])
        if letter == 'F':
            vertical += add_vertical * units
            horizontal += add_horizontal * units
        elif letter == 'L' or letter == 'R':
            # Make both rotations go the same way
            if letter == 'L':
                units = -units % 360
            add_horizontal, add_vertical = perform_rotation(units, add_horizontal, add_vertical)
        else:
            add_vertical, add_horizontal = letters(letter, units, add_horizontal, add_vertical)

    print(abs(vertical) + abs(horizontal))
part1(arr)
part2(arr)
