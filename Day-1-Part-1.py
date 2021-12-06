with open("input.txt") as f:
    count = 0
    previous = 0
    for i in f:
        current = int(i.strip())
        if previous != 0 and current > previous:
            count += 1
        previous = current
    print(count)
