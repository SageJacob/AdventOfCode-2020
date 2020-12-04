def count1(fields, person)-> int:
    for field in fields:
        if field not in person:
            return 0
    return 1

def count2(fields, person)-> int:
    for field in fields:
        if field not in person:
            return 0
    byr = int(person['byr'])
    iyr = int(person['iyr'])
    eyr = int(person['eyr'])
    if byr < 1920 or byr > 2002:
        return 0
    if iyr < 2010 or iyr > 2020:
        return 0
    if eyr < 2020 or eyr > 2030:
        return 0
    unit = person['hgt'][len(person['hgt'])-2:]
    if unit != 'cm' and unit != 'in':
        return 0
    person['hgt'] = person['hgt'][:len(person['hgt'])-2]
    if unit == 'cm' and (int(person['hgt']) < 150 or int(person['hgt']) > 193):
        return 0
    if unit == 'in' and (int(person['hgt']) < 59 or int(person['hgt']) > 76):
        return 0
    if person['hcl'][0] != '#' or (not person['hcl'][1:].isalnum()):
        return 0
    eyes = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    if person['ecl'] not in eyes:
        return 0
    if not person['pid'].isnumeric() or len(person['pid']) != 9:
        return 0
    return 1

def part1(x, fields, person={}, counter=0)-> None:
    for line in x:
        line = line.strip('\n')
        if len(line) == 0:
            counter += count1(fields, person)
            person = {}
            continue
        words = line.split(' ')
        for word in words:
            person[word[0:3]] = word[4:]

    counter += count1(fields, person)
    print(counter)

def part2(x, fields, person={}, counter=0)-> None:
    for line in x:
        line = line.strip('\n')
        if len(line) == 0:
            counter += count2(fields, person)
            person = {}
            continue
        words = line.split(' ')
        for word in words:
            person[word[0:3]] = word[4:]

    counter += count2(fields, person)
    print(counter)

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
x = open("input4.txt", "r")
part1(x, fields)
x = open("input4.txt", "r")
part2(x, fields)