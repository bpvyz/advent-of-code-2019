with open('input.txt', 'r') as f:
    data = f.read()

layers = [[[int(data[col+row*25+layer*150]) for col in range(25)] for row in range(6)] for layer in range(100)]

sumindex = 0
nr_of_zeroes = 150
for index, layer in enumerate(layers):
    curr = sum(row.count(0) for row in layer)
    if curr < nr_of_zeroes:
        print(f"NEW MINIMUM IN INDEX {index} - {curr} ZEROES")
        nr_of_zeroes = curr
        sumindex = index

nr_of_ones = sum(row.count(1) for row in layers[sumindex])
nr_of_twos = sum(row.count(2) for row in layers[sumindex])
part1 = nr_of_ones*nr_of_twos
print(part1)