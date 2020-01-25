fuelsum = 0
with open("input.txt") as f:
    for line in f:
        fuel += (int(int(line)/3-2))
    for line in f:
        mmass = int(line)
        while mmass > 6:
            temp = mmass // 3 - 2
            fuelsum += temp
            mmass = temp
    print("fuel required = ", fuelsum)

