with open("input.txt") as f:
    nums = [int(i.strip()) for i in f]
    count = 0
    prev = None
    for i in range(0, len(nums) - 2):
        cur = sum(nums[i:i+3])
        if prev != None and cur > prev:
            count += 1
        prev = cur
    print(count)
