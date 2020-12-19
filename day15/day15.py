def game(limit):
    if limit > 2020:
        print('This will take about a minute')
    nums = [17,1,3,16,19,0]
    nums.insert(0, 0)
    previous_num = 0
    d = {}
    counter = 1
    while counter <= limit:
        # Add all elements into dict except last element
        if counter < len(nums):
            if counter > 1:
                d[str(previous_num)] = counter
            previous_num = nums[counter]

        # If last element, or any new number, not in dict, add it to dict and sett current turn to 0
        elif str(previous_num) not in d:
            d[str(previous_num)] = counter
            previous_num = 0

        elif str(previous_num) in d:
            num = counter - d[str(previous_num)]
            d[str(previous_num)] = counter
            previous_num = num

        counter += 1

    print(previous_num)

game(2020)
game(30000000)