with open("input.txt") as f:
    x = 0
    y = 0
    for command in f:
        opcode, operand = command.split()
        if opcode == "forward":
            x += int(operand)
        elif opcode == "down":
            y += int(operand)
        else:
            y -= int(operand)
    print(x*y)
