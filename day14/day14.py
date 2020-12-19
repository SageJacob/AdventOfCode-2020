
def convert(number):
    number = str(bin(number))
    number = number[2:]
    return number

def apply_mask(mask, number):
    number = convert(number)
    number = '0' * (36 - len(number)) + number
    number = list(number)
    for i in range(len(mask)):
        if mask[i] == 'X':
            continue
        number[i] = mask[i]
    number = ''.join(number)
    decimal = int(number, 2)
    return decimal

def counting_helper(number, i):
    binary = convert(i)
    binary = '0' * (number.count('X') - len(binary)) + binary
    index = 0
    number = list(number)
    for j in range(len(number)):
        if number[j] == 'X':
            number[j] = binary[index]
            index += 1
    number = ''.join(number)
    decimal = int(number, 2)
    return decimal

def counting(number, count):
    arr = []
    for i in range(count):
        arr.append(counting_helper(number, i))
    return arr

def apply_mask2(mask, number):
    number = convert(number)
    number = '0' * (36 - len(number)) + number
    number = list(number)
    for i in range(len(mask)):
        if mask[i] == 'X':
            number[i] = 'X'
        elif mask[i] == '1':
            number[i] = '1'
        else:
            continue
    number = ''.join(number)
    count = number.count('X')
    count = 2 ** count
    arr = counting(number, count)
    return arr


def part(file, part):
    arr = {}
    res = {}
    for line in file:
        line = line.strip()
        if line.startswith('mask = '):
            tokens = line.split()
            mask = tokens[2]
        else:
            tokens = line.split()
            address = int(tokens[0][4:len(tokens[0])-1])
            number = tokens[len(tokens)-1]
            if part == 1:
                arr[address] = apply_mask(mask, int(number))
            if part == 2:
                address = apply_mask2(mask, address)
                for i in address:
                    res[i] = int(number)
    if part == 1:
        ans = 0
        for i in arr:
            ans += arr[i]
        print(ans)
    else:
        ans = 0
        for i in res:
            ans += res[i]
        print(ans)

file = open('input14.txt', 'r')
part(file, 1)
file = open('input14.txt', 'r')
part(file, 2)