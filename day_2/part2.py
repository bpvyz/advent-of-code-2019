with open('input.txt', 'r') as f:
    s = f.read()
    bmem = [int(val) for val in s.split(',')]
bmem[1], bmem[2] = 12, 2

for noun in range(100):
    for verb in range(100):
        mem = [val for val in bmem]
        mem[1] = noun
        mem[2] = verb
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
        if mem[0] == 19690720:
            print('noun:', noun, 'verb:', verb)
            print("100 * noun + verb:", 100 * noun + verb)