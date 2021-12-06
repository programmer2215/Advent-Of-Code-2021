with open("input.txt") as f:
    x = 0
    y = 0
    aim = 0
    for command in f:
        opcode, operand = command.split()
        operand = int(operand)
        if opcode == "forward":
            x += operand
            y += aim * operand
        elif opcode == "down":
            aim += operand
        else:
            aim -= operand
    print(x*y)
