with open('input.txt', 'r') as f:
    data = f.read()

layers = [[[int(data[col+row*25+layer*150]) for col in range(25)] for row in range(6)] for layer in range(100)]
image = [['' for n in range(25)] for m in range(6)]

row, col = 0, 0
while row * col != 125:
    if col % 25 == 0 and col != 0:
        col = 0
        row += 1
    for layer in layers:
        if layer[row][col] == 1:
            image[row][col] = "*"
            col += 1
            break
        elif layer[row][col] == 0:
            image[row][col] = " "
            col += 1
            break
        else:
            continue
for elem in image:
    print(elem)