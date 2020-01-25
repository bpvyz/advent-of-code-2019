with open('input.txt', 'r') as f:
    s = f.read()
    mem = [int(val) for val in s.split(',')]
mem[1], mem[2] = 12, 2

for opcode in range(0, len(mem), 4):
    # print(opcode)
    op, param1, param2, dest = mem[opcode], mem[opcode + 1], mem[opcode + 2], mem[opcode + 3]
    if op == 1:
        mem[dest] = mem[param1] + mem[param2]
    elif op == 2:
        mem[dest] = mem[param1] * mem[param2]
    else:
        assert op == 99
        break
# prints final list:
# print(magic)
print("value of index 0 is :", mem[0])