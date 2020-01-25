from copy import deepcopy


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a*b)//gcd(a, b)


def tick():

    for i in range(len(Mpos)):
        for j in range(len(Mpos)):
            for p in Mpos[i]:
                if Mpos[i][p] < Mpos[j][p]:
                    Mvel[i][p] += 1
                elif Mpos[i][p] > Mpos[j][p]:
                    Mvel[i][p] -= 1

    for i in range(len(Mpos)):
        for k in Mpos[i]:
            Mpos[i][k] += Mvel[i][k]


Mpos = []
Mvel = []

for line in open("input.txt", "r").readlines():
    line = line.strip()
    line = line[1:-1]
    line = line.split(", ")
    moon = {}
    for e in line:
        k, v = e.split("=")
        moon[k] = int(v)
    Mpos.append(moon)
    Mvel.append({'x': 0, 'y': 0, 'z': 0})

start_Mpos = deepcopy(Mpos)
start_Mvel = deepcopy(Mvel)

part_1 = 0
for _ in range(1000):
    tick()

for i in range(len(Mpos)):
    pot = 0
    kin = 0
    for k in Mpos[i]:
        pot += abs(Mpos[i][k])
        kin += abs(Mvel[i][k])
    part_1 += (pot * kin)

print(part_1)

periods = [0, 0, 0]

Mpos = start_Mpos
Mvel = start_Mvel

for i in range(3):
    axis = ["x", "y", "z"][i]
    print("Calculating axis:", axis)
    t = 0
    seen = set()
    while True:
        tick()
        state = []
        for j in range(len(Mpos)):
            state.append(Mpos[j][axis])
            state.append(Mvel[j][axis])
        state = str(state)
        if state in seen:
            print("Seen:", state)
            periods[i] = t
            break

        seen.add(state)
        t += 1

print(periods)
print(lcm(lcm(periods[0], periods[1]), periods[2]))