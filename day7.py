x = open('input7.txt', 'r')
def makeInput(part):
    bags = {}
    for line in x:
        line = line.split()
        # Dead-end colors
        if 'no' in line:
            bags[line[0]+line[1]] = {}
        # Colors that lead somewhere
        else:
            original_word = line[0]+line[1]
            if original_word not in bags.keys():
                bags[line[0]+line[1]] = []
            start = 3
            # add the other colors to the color at the beginning (original_word)
            for i in range(start, len(line)):
                if line[i].startswith('bag') and (line[i-2] + line[i-1]) not in bags[original_word]:
                    if part == 2:
                        bags[original_word].append([int(line[i-3]), line[i-2] + line[i-1]])
                    else:
                        bags[original_word].append(line[i-2] + line[i-1])
    return bags

def part1(bags):
    bags = makeInput(1)
    contains = {'shinygold'}
    added = 1
    while added > 0:
        added = 0
        for bag in bags:
            if bag in contains:
                continue
            for i in bags[bag]:
                if i in contains:
                    added += 1
                    contains.add(bag)
    print(len(contains)-1)

def findCount(bags, curr_bag):
        num = 0
        for bag in bags[curr_bag]:
            num += bag[0] + (bag[0] * findCount(bags, bag[1]))
        return num

def part2(x):
    bags = makeInput(2)
    print(findCount(bags, 'shinygold'))

x = open('input7.txt', 'r')
part1(x)
x = open('input7.txt', 'r')
part2(x)