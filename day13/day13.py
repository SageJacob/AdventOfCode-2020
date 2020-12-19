def part1(original_number, nums):
    new_number = original_number - 1
    while True:
        new_number += 1
        for i in nums:
            if new_number % i == 0:
                return i * (new_number - original_number)

def part2(buses, start_ID, start_Time):
    while True:
        if len(buses) == 0:
            return start_Time
        for time_stamp, busID in buses[1:]:
            if (start_Time + time_stamp) % busID:
                break
            else:
                start_ID *= busID
                buses.remove((time_stamp, busID))
                break
        if len(buses) == 1:
            return start_Time
        start_Time += start_ID


x = open('input13.txt', 'r')
file = []
for i in x:
    file.append(i)
original_number = int(file[0])
nums = [int(i) for i in file[1].split(',') if i != 'x']
file = file[1].split(',')
arr = [(i, int(k)) for i, k in enumerate(file) if k != 'x']

print(part1(original_number, nums))
print(part2(arr, arr[0][1], arr[0][0]))
