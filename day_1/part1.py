fuel = 0
with open("input.txt") as f:
    for line in f:
        fuel += (int(int(line)/3-2))
print("fuel required = ",fuel)