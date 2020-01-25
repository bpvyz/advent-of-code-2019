with open('input.txt', 'r') as f:
    s = f.read()
    mem = [int(val) for val in s.split(',')]
print(mem)
opcode = 0
step = 4
while opcode < len(mem):
    op, param1, param2, dest = mem[opcode], mem[opcode + 1], mem[opcode + 2], mem[opcode + 3]
    if op == 1:
        mem[dest] = mem[param1] + mem[param2]
        step = 4
    elif op == 2:
        mem[dest] = mem[param1] * mem[param2]
        step = 4
    elif op == 3:
        onlyinput = int(input("Enter TEST value: "))
        mem[param1] = onlyinput
        step = 2
        print(mem)
    elif op == 4:
        print(mem[param1])
        step = 2
    elif op == 99:
        break
    else:
        pass
    print(op)
    opcode = opcode + step