with open("input.txt") as file:
    inp = file.read().strip()

path1, path2 = inp.split("\n")
path1 = path1.split(",")
path2 = path2.split(",")

cur = [0,0]

dirs = {"R":(0,1),"L":(0,-1),"U":(1,1),"D":(1,-1)}

signals = {}

cur = [0,0]
steps = 0
for p in path1:
    d, v = p[0], int(p[1:])
    i, c = dirs[d]
    for _ in range(v):
        cur[i] += c
        steps += 1
        signals[tuple(cur)] = steps

ints = []

cur = [0,0]
steps = 0
for p in path2:
    d, v = p[0], int(p[1:])
    i, c = dirs[d]
    for _ in range(v):
        cur[i] += c
        steps += 1
        t = tuple(cur)
        if t in signals:
            ints.append((steps + signals[t],t))

print("Part 1:", min(abs(p[1][0]) + abs(p[1][1]) for p in ints))
print("Part 2:", min(p[0] for p in ints))