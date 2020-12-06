def part1(x):
    s = set()
    count = 0
    empty = 0
    for line in x:
        line = line.strip('\n')
        if len(line) == 0:
            empty += 1
            count += len(s)
            s = set()
            continue
        for i in line:
            s.add(i)
    count += len(s)
    print(count)
    
def check(d, questions):
    count = 0
    for i in d:
        if d[i] == questions:
            count += 1
    return count

def part2(x):
    count = 0
    questions = 0
    d = {}
    for line in x:
        line = line.strip('\n')
        if len(line) == 0:
            count += check(d, questions)
            d = {}
            questions = 0
            continue
        questions += 1
        for i in line:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
    count += check(d, questions)
    print(count)

x = open('input6.txt', 'r')
part1(x)
x = open('input6.txt', 'r')
part2(x)