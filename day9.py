'''
    I understand that I can improve this program (for example, using a hashmap for the twoSum function
    to improve complexity from O(n^2) to O(n)). However, with advent of code, the speed at which you 
    find the answer is more important than efficiency (given the scope of the input) which is why I
    focused on the speed at which I write the function. I could certainly optimize my solution but
    prefer to keep the solution untouched for future reference.
'''

def twoSum(arr, target):
    for i in range(len(arr) - 2):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False

def part1(): 
    global target
    global preamble
    for i in range(preamble, len(nums)):
        if not twoSum(nums[i-preamble:i], nums[i]):
            print('part1:', nums[i])
            target = nums[i]
            break

def part2():
    global target
    curr_sum = 0
    for i in range(len(nums) - 2):
        curr_sum = nums[i]
        for j in range(i+1, len(nums)):
            curr_sum += nums[j]
            if curr_sum == target:
                print('part2:', min(nums[i:j+1])+max(nums[i:j+1]))
                exit()

x = open('input9.txt', 'r')
nums = []
for line in x:
    nums.append(int(line.strip('\n')))
target = 0
preamble = 25
part1()
part2()